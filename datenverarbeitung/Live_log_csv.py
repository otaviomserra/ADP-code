import os
import pandas as pd
import json
import time
from threading import Lock  # Import Lock from threading module
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class LogToCSVConverter:
    def __init__(self, log_filename, csv_filename):
        self.log_filename = log_filename
        self.csv_filename = csv_filename

    def convert(self):
        # Creating path for csv files
        # if not os.path.exists('datenverarbeitung/csv-logs'):
        #     os.makedirs('datenverarbeitung/csv-logs')
        # log_path = os.path.join('logs', self.log_filename)
        # csv_path = os.path.join('datenverarbeitung/csv-logs', self.csv_filename)

        ### TESTANDO, VOLTAR PRO ANTERIOR AQUI TAMBÉM
#<<<<<<< HEAD
        if not os.path.exists('csv-logs'):
            os.makedirs('csv-logs')
        log_path = os.path.join(self.log_filename)
        csv_path = os.path.join('csv-logs', self.csv_filename)
#=======
        if not os.path.exists('csv_logs'):
            os.makedirs('csv_logs')
        log_path = os.path.join(self.log_filename)
        csv_path = os.path.join('csv_logs', self.csv_filename)
#>>>>>>> b21a672ed710f71ef38bbdfcd0fe82ca89ea0f5b

        log_data = open(log_path, 'r')

        # Working with the log structure itself

        # Correcting first the problem with lines in the log
        # When there is an error message, the message is printed in differents lines in the log
        # Removing the different lines in the code which does not start with the time stamp
        corrected_lines = []
        for line in log_data:
            if line.startswith("["):
                corrected_lines.append(line)
            else:
                corrected_lines[-1] += line

        # Separating the data between date, time stamp, type, module and message
        # Removing the quotes from each column
        # Minor modifications into the Message
        data = []
        for line in corrected_lines:
            split = line.split(' ', 4)
            split[0] = split[0][1:]
            split[1] = split[1][:-1]
            split[2] = split[2][1:-1]
            split[3] = split[3][1:-1]
            split[4] = split[4].replace('\n', '')
            split[4] = split[4][1:-1]
            data.append(split)

        df = pd.DataFrame(data, columns=['Date', 'Hour', 'Type', 'Module', 'Message'])

        # Saving the csv files
        df.to_csv(csv_path, index=False)
        # df.to_excel('/csv-logs/df_teste.xlsx')

        print(f"Transformação concluída. Arquivo '{self.csv_filename}' gerado.")


def convert_log_on_update(log_filename, csv_filename):
    converter = LogToCSVConverter(log_filename, csv_filename)
    converter.convert()


class LogFileHandler(FileSystemEventHandler):
    def __init__(self, log_filename, csv_filename):
        self.log_filename = log_filename
        self.csv_filename = csv_filename

    def on_modified(self, event):
        if event.is_directory:
            return
        if event.src_path == self.log_filename:
            print(f"'{self.log_filename}' updated. Starting log conversion.")
            convert_log_on_update(self.log_filename, self.csv_filename)
            print("Log conversion completed.")


#<<<<<<< HEAD

#=======
#>>>>>>> b21a672ed710f71ef38bbdfcd0fe82ca89ea0f5b
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


class ExcelFileHandler(FileSystemEventHandler):
    def __init__(self, excel_filename, processor):
        self.excel_filename = excel_filename
        self.processor = processor

    def on_modified(self, event):
        if event.is_directory:
            return
        if event.src_path == self.excel_filename:
            self.process_modified_excel()

    def process_modified_excel(self):
        print(f"'{self.excel_filename}' modified. Starting data processing.")
        with program_lock:
            self.processor.load_dataframe()
            self.processor.filter_and_clean_dataframe()
            self.processor.process_dataframe()
            self.processor.save_processed_dataframe(csv_file_path)
        print("Data processing completed.")

#<<<<<<< HEAD
#=======

#>>>>>>> b21a672ed710f71ef38bbdfcd0fe82ca89ea0f5b
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


#<<<<<<< HEAD

if __name__ == "__main__":
    log_filename = r"C:\Users\Otavio\Desktop\TUDa\Freedom Plan\ADP Digitaler Schatten\Code\datenverarbeitung\teste.log"
    csv_filename = r'C:\Users\Otavio\Desktop\TUDa\Freedom Plan\ADP Digitaler Schatten\Code\datenverarbeitung\csv-logs\log_transformado.csv'
#=======
if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath('Live_log_csv'))

    raw_logs_path = os.path.join(current_directory, 'raw_logs')
    clean_logs_path = os.path.join(current_directory, 'csv_logs')
    kafka_logs_path = os.path.join(current_directory, 'kafka_logs')

    # List the files in the raw_logs folder
    raw_files = os.listdir(raw_logs_path)

    # Initialize most_recent_file and most_recent_mtime
    most_recent_file = None
    most_recent_mtime = 0

    # Filter out directories and get the most recent file
    for raw_file in raw_files:
        raw_file_path = os.path.join(raw_logs_path, raw_file)
        if os.path.isfile(raw_file_path):
            file_mtime = os.path.getmtime(raw_file_path)
            if file_mtime > most_recent_mtime:
                most_recent_mtime = file_mtime
                log_filename = raw_file_path

    # Extract the base filename without the extension (.log)
    parts = raw_file_path.split("\\")
    log_name = parts[-1].split(".")[0]  # Get the first part before the dot (.) in the last part

    csv_filename = 'cleaned_' + log_name + '.csv'
    kafka_filename = 'kafka_' + log_name + '.csv'
#>>>>>>> b21a672ed710f71ef38bbdfcd0fe82ca89ea0f5b

    event_handler = LogFileHandler(log_filename, csv_filename)
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(log_filename))
    observer.start()
    program_lock = Lock()
#<<<<<<< HEAD
    logger_path = csv_filename
    csv_file_path = r'C:\Users\Otavio\Desktop\TUDa\Freedom Plan\ADP Digitaler Schatten\Code\datenverarbeitung\kafka-logs\live_kafka.csv'
    monitor_excel_file(logger_path)

#=======
    logger_path = ''.join(['csv_logs\\', csv_filename])

    csv_file_path = ''.join(['kafka_logs\\', kafka_filename])

    monitor_excel_file(logger_path)
#>>>>>>> b21a672ed710f71ef38bbdfcd0fe82ca89ea0f5b

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

#<<<<<<< HEAD
    observer.join()
#=======
    observer.join()

#>>>>>>> b21a672ed710f71ef38bbdfcd0fe82ca89ea0f5b
