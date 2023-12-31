# This script is the main for the work with the data
# In here are the observers for the Log file generated by Neoception,
# after detecting a change in it, it filters the message and alocate the data in a Dataframe (kafka logs)
# kafka logs are the events logs and the info got from Neoception
# After it filters it out, and by each detection it runs both functions for inventory and processes
# This happens in the excel file handler (which works on onmodified)
# For future works, the system can get more robust by separating the observers and creating a real Main which would do that
# Another observation is that the time format for log is 12h, so there is a temporary fix to add hours if its earlier than 7 (operation time from 7 in the morning until 18h59)
import os
import pandas as pd
import json
import time
from threading import Lock  # Import Lock from threading module
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from process_requests import *
from InventarDataDistribution import *
from process_data import *
from datetime import datetime
import numpy as np
import pytz

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
        if not os.path.exists('csv_logs'):
            os.makedirs('csv_logs')
        log_path = os.path.join(self.log_filename)
        csv_path = os.path.join('csv_logs', self.csv_filename)

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

    def save_processed_dataframe(self, csv_file_path):
        if self.df is None:
            raise ValueError("DataFrame not loaded or processed.")

        self.df.to_csv(csv_file_path, index=False)


class ExcelFileHandler(FileSystemEventHandler):
    def __init__(self, excel_filename, processor):
        super().__init__()
        self.excel_filename = excel_filename
        self.processor = processor
        self.last_event_time = None
        self.min_time_interval = 1

    def on_modified(self, event):
        if event.is_directory:
            return

        # Ignore duplicate events
        current_time = time.time()
        if self.last_event_time is None or (current_time - self.last_event_time) >= self.min_time_interval:
            self.last_event_time = current_time
            if event.src_path == self.excel_filename:
                self.process_modified_excel()

            print("\n\n\n\n\n\n\n")
            modification_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("OBSERVER EVENT: ", end="")
            print(event)
            print("THIS EVENT WAS DETECTED AT " + modification_timestamp)
            # FIXING DUPLICATES
            if event.event_type == "modified":
                date, lane, timestamp, event_type = read_kafka_lane_time_event(csv_file_path)
                print(event_type)
                Inventar = Lane(lane, date, timestamp, event_type)
                if event_type == 'CARRIER_ACTION_PICK':
                    print('entrou no pick')
                    if lane not in ["S001.M001.01.01, S001.M001.01.02"]:  # Fraesplatz doesn't generate requests
                        requests.append(ProcessRequest(date, lane, timestamp))
                    for request in requests:
                        print(request.target_lanes)
                        print(lane)
                        print(requests)
                    # Current structure cannot model the first two inventories
                    if lane not in ["S001.M001.01.01, S001.M001.01.02", "S001.M002.01.01, S001.M002.01.02"]:
                        Inventar.pick_event()

                elif event_type == 'CARRIER_ACTION_PUT':
                    print('entrou no put')
                    print(requests)
                    for request in requests:
                        print(request.target_lanes)
                        print(lane)
                        if lane in request.target_lanes:
                            request.resolve(lane, timestamp)
                            request.generate_process_log(lane)
                            requests.remove(request)
                            print('rodou put request')
                            break
                    # Current structure cannot model the first two inventories
                    if lane not in ["S001.M001.01.01, S001.M001.01.02", "S001.M002.01.01, S001.M002.01.02"]:
                        Inventar.put_event()
                Inventar.save_dashboard_format()

    def process_modified_excel(self):
        print(f"'{self.excel_filename}' modified. Starting data processing.")
        with program_lock:
            self.processor.load_dataframe()
            self.processor.filter_and_clean_dataframe()
            self.processor.process_dataframe()
            self.processor.save_processed_dataframe(csv_file_path)

        print("Data processing completed.")
        print("Kafka .csv generated. Data processing completed.")


############################################################################
# FEHLERMELDUNG
############################################################################

# READ EVERY SHEET IN THE FILE AT LEAST ONCE
current_dir = os.path.dirname(__file__)
process_excel_path = os.path.join(current_dir, "Digital_Button.xlsm")
# Sheets for error logs
df_fertigung = pd.read_excel(process_excel_path, sheet_name='LogData(Fertigung)')
df_montage = pd.read_excel(process_excel_path, sheet_name='LogData(Montage)')

# Sheets for process logs
df_saegen = pd.read_excel(process_excel_path, sheet_name='LogData(Saegen)')
df_drehen = pd.read_excel(process_excel_path, sheet_name='LogData(Drehen)')
df_waschen = pd.read_excel(process_excel_path, sheet_name='LogData(Waschen)')


def handle_error(error_df):
    # Obtains the target lane where the piece would have gone to
    if error_df["Bauteil"].iloc[0] == "FB01":
        target_lane = "S001.M003.02.01"
    elif error_df["Bauteil"].iloc[0] == "FB02":
        target_lane = "S001.M003.02.02"
    else:
        target_lane = "S001.M003.02.03"

    # Timestamp of when the error happened
    timestamp = error_df["Uhrzeit"].iloc[0]

    # Looks for the earliest request with the target_lane and cancels it
    for request in requests:
        if target_lane in request.target_lanes:
            request.cancel(timestamp, target_lane)
            request.generate_process_log(target_lane)
            requests.remove(request)
            break


def generate_other_processes(process, newrows_df):
    # LOGS FOR DREHEN, SAEGEN, WASCHEN
    return 0


class ErrorFileHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.last_event_time = None
        self.min_time_interval = 1

    def on_modified(self, event):
        if event.is_directory:
            return

        # Protection against duplicate detections
        current_time = time.time()
        if self.last_event_time is None or (current_time - self.last_event_time) >= self.min_time_interval:
            self.last_event_time = current_time
            if event.src_path == process_excel_path:
                # Reload the Excel file
                global df_fertigung
                df_fertigung = pd.read_excel(process_excel_path, sheet_name='LogData(Fertigung)')

                # Get the current number of rows
                current_row_count_fertigung = df_fertigung.shape[0]

                # Check if new rows have been added and removes a request if true
                if current_row_count_fertigung > len(df_fertigung):
                    new_rows_fertigung = df_fertigung.iloc[len(df_fertigung):]
                    handle_error(new_rows_fertigung)


##################################################################


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


def read_kafka_lane_time_event(kafka_path):
    try:
        df = pd.read_csv(kafka_path)

        if df.empty:
            print("Empty exception!")
            return None  # The CSV file is empty.

        last_row = df.iloc[-1]

        if len(last_row) < 3:
            print("Too short exception!")
            return None  # The last row doesn't have enough columns.


        ######## MODIFICAR APÓS O CHICO
        date = last_row.iloc[0]
        timestamp = last_row.iloc[1]
        # Correct from 12h format to 24h format
        hour = int(timestamp[:2])
        if hour < 7:
            hour += 12
            hour = str(hour)
            timestamp = hour + timestamp[2:]

        """
        # Defina os fusos horários
        print("Just before defining timezones")
        utc_timezone = pytz.timezone('UTC')
        berlin_timezone = pytz.timezone('Europe/Berlin')
        print("Just after defining timezones")

        # Combine a coluna 'Date' e 'Hour' em uma coluna de data e hora
        datetime_str = date + ' ' + timestamp
        print(datetime_str)
        datetime_obj = datetime.strptime(datetime_str, '%d/%b/%Y %H:%M:%S')
        print(datetime_obj)
        print("Just before assigning datetime_utc")
        datetime_utc = utc_timezone.localize(datetime_obj)

        # Converta para o fuso horário de Berlim e salve em variáveis
        datetime_berlin = datetime_utc.astimezone(berlin_timezone)
        print("Just after assigning datetime_berlin")

        # Separe a data e o horário e salve em variáveis
        date_berlin = str(datetime_berlin.strftime('%d/%b/%Y'))
        print(date_berlin)
        hour_berlin = str(datetime_berlin.strftime('%H:%M:%S'))
        print(hour_berlin)
        """
        event_type = last_row.iloc[6]
        lane = last_row.iloc[-1]

        return date, lane, timestamp, event_type
    except FileNotFoundError:
        print("File not found exception!")
        return None  # Handle file not found exception
    except Exception as e:
        print("Something else is fucky!")
        return None  # Handle other exceptions


if __name__ == "__main__":
    global requests
    requests = []

    current_directory = os.path.dirname(os.path.abspath('datenverarbeitung_main'))
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
    parts = log_filename.split("\\")
    log_name = parts[-1].split(".")[0]  # Get the first part before the dot (.) in the last part

    print(log_filename)
    csv_filename = 'cleaned_' + log_name + '.csv'
    kafka_filename = 'kafka_' + log_name + '.csv'

    logger_path = ''.join(['csv_logs\\', csv_filename])

    csv_file_path = ''.join(['kafka_logs\\', kafka_filename])

    event_handler = LogFileHandler(log_filename, csv_filename)

    ################################################
    # REPLACING THE OLD MONITOR_EXCEL_FILE FUNCTION
    processor = DataFrameProcessor(logger_path)
    excel_event_handler = ExcelFileHandler(logger_path, processor)
    error_handler = ErrorFileHandler()  # Fehlermeldung
    # excel_observer = Observer()

    # excel_observer.schedule(excel_event_handler, path=os.path.dirname(logger_path))
    # excel_observer.start()
    ###################################

    # Observer checks 3 paths
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(log_filename))
    observer.schedule(excel_event_handler, path=os.path.dirname(logger_path), recursive=True)
    # observer.schedule(error_handler, path=os.path.dirname(process_excel_path), recursive=True)  # unused
    observer.start()
    program_lock = Lock()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
#####################################################
# REQUESTS
#####################################################


#    if event_type == "CARRIER_ACTION_PUT":
#        for request in requests:
#            if request.target_lane == "we just got a put event from this":
#                request.resolve("timestamp")
#                request.generate_process_log()
#    elif event_type == "CARRIER_ACTION_PICK":
#        requests.append(ProcessRequest(
    #        "timestamp", "LANE"))

    # PROZESSVERFOLGERUNG
