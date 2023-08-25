import pandas as pd
import json


class DataFrameProcessor:
    def __init__(self, logger_path):
        self.logger_path = logger_path
        self.df = None

    def load_dataframe(self):
        self.df = pd.read_excel(self.logger_path)

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


# Usage - Main
logger_path = "D:\Francisco - Dados\Documentos\GitHub\ADP-code\datenverarbeitung\csv-logs\df_teste.xlsx"
csv_file_path = "TESTElogs.csv"


processor = DataFrameProcessor(logger_path)
processor.load_dataframe()
processor.filter_and_clean_dataframe()
processor.process_dataframe()
processor.save_processed_dataframe(csv_file_path)