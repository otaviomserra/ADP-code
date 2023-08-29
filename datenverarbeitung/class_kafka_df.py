import os
import pandas as pd
import json
import time
from threading import Lock  # Import Lock from threading module
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



class DataFrameProcessor:
    def __init__(self, logger_path):
        self.logger_path = logger_path
        self.csv_file_path = csv_file_path
        self.df = None

    def load_dataframe(self):
        self.df = pd.read_csv(self.logger_path)

    def filter_and_clean_dataframe(self):
        if self.df is None:
            raise ValueError("DataFrame not loaded. Call load_dataframe first.")

        self.df = self.df[self.df.apply(lambda row: any('KAFKA' in str(cell) for cell in row), axis=1)].drop(
            columns=['Type', 'Module'], errors='ignore')

    def extract_json_info(self, row):
        content = row.split('[content=')[1][:-1]  # Extract the content portion
        content_json = json.loads(content)
        header = content_json['header']
        body = content_json['body']['action']['carrier']

        topic = row.split('[topic=')[1].split(']')[0]  # Extract topic

        trace_id = header['traceId']
        id_value = header['id']
        org_id = header['organisationId']

        carrier_action = body['carrierActionType']
        carrier_id = body['carrierId']
        current_count = body['currentCount']
        lane_address = body['laneAddress']

        return topic, trace_id, id_value, org_id, carrier_action, carrier_id, current_count, lane_address

    def process_dataframe(self):
        if self.df is None:
            raise ValueError("DataFrame not loaded. Call load_dataframe first.")

        self.df['ExtractedData'] = self.df['Message'].apply(self.extract_json_info)
        extracted_data = self.df['ExtractedData'].apply(pd.Series)
        extracted_data.columns = ['Topic', 'traceId', 'id', 'organisationId', 'carrierActionType', 'carrierId',
                                  'currentCount', 'laneAddress']
        self.df = pd.concat([self.df, extracted_data], axis=1)
        self.df.drop(columns=['Message', 'ExtractedData'], inplace=True)
        self.df.drop(self.df.columns[0], axis=1, inplace=True)

    def save_processed_dataframe(self, csv_file_path):
        if self.df is None:
            raise ValueError("DataFrame not loaded or processed.")

        self.df.to_csv(csv_file_path, index=False)



    def process_modified_excel(self):
        print(f"'{self.excel_filename}' modified. Starting data processing.")
        with program_lock:
            self.processor.load_dataframe()
            self.processor.filter_and_clean_dataframe()
            self.processor.process_dataframe()
            self.processor.save_processed_dataframe("processed_data.csv")
        print("Data processing completed.")

def monitor_excel_file(logger_path):
    processor = DataFrameProcessor(logger_path)
    excel_event_handler = ExcelFileHandler(logger_path, processor)
    excel_observer = Observer()

    excel_observer.schedule(excel_event_handler, path=os.path.dirname(logger_path))
    excel_observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:

        excel_observer.stop()

    excel_observer.join()

if __name__ == "__main__":
    program_lock = Lock()

    logger_path = "csv-logs\log_transformado.csv"
    csv_file_path = 'kafka-logs\live_kafka'
    monitor_excel_file(logger_path)
    print('rodou')