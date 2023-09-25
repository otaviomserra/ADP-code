import os.path
import time
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define the Excel file path and sheet name
excel_file_path = 'Reject_Button.xlsm'
messen_fehler_sheet = 'LogData(Fertigung)'

# Read the Excel file initially
df_fertigung = pd.read_excel('Reject_Button.xlsm', sheet_name='LogData(Fertigung)')

requests = []


# Function that cancels a request if an error is detected
def handle_error(error_df):
    # Obtains the target lane where the piece would have gone to
    if error_df["Bauteil"].iloc[0] == "FB01":
        target_lane = "S001.M003.02.01"
    elif error_df["Bauteil"].iloc[0] == "FB02":
        target_lane = "S001.M003.02.02"
    else:
        target_lane = "S001.M003.02.03"

    # Looks for the earliest request with the target_lane and cancels it
    for request in requests:
        if request.target_lane == target_lane:
            request.cancel()
            requests.remove(request)
            break


# Define a custom event handler for file system changes
class ErrorFileHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__(self)
        self.last_event_time = None
        self.min_time_interval = 1

    def on_modified(self, event):
        if event.is_directory:
            return

        current_time = time.time()
        if self.last_event_time is None or (current_time - self.last_event_time) >= self.min_time_interval:
            self.last_event_time = current_time
            if event.src_path == excel_file_path:
                # Reload the Excel file
                global df_fertigung
                df_fertigung = pd.read_excel('Reject_Button.xlsm', sheet_name='LogData(Fertigung)')

                # Get the current number of rows
                current_row_count_fertigung = df_fertigung.shape[0]

                # Check if new rows have been added and removes a request if true
                if current_row_count_fertigung > len(df_fertigung):
                    new_rows_fertigung = df_fertigung.iloc[len(df_fertigung):]
                    handle_error(new_rows_fertigung)


# Create an observer to monitor file changes
observer = Observer()
error_handler = ErrorFileHandler()
observer.schedule(error_handler, path=os.path.dirname('Reject_Button.xlsm'), recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()