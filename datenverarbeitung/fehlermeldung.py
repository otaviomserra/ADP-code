import time
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler




# Define the Excel file path and sheet name
excel_file_path = 'Reject_Button.xlsm'
messen_fehler_sheet = 'LogData(Fertigung)'

# Read the Excel file initially
df_fertigung = pd.read_excel(excel_file_path, sheet_name=messen_fehler_sheet)

requests = []


# Function that cancels a request if an error is detected
def handle_error(error_df):
    # Obtains the target lane where the piece would have gone to
    




    return 0


# Define a custom event handler for file system changes
class ErrorFileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == excel_file_path:
            # Reload the Excel file
            global df_fertigung
            df_fertigung = pd.read_excel(excel_file_path, sheet_name=messen_fehler_sheet)

            # Get the current number of rows
            current_row_count_fertigung = df_fertigung.shape[0]

            # Check if new rows have been added
            if current_row_count_fertigung > len(df_fertigung):
                new_rows_fertigung = df_fertigung.iloc[len(df_fertigung):]
                print("New lines added:")
                print(new_rows_fertigung)


# Create an observer to monitor file changes
observer = Observer()
event_handler = ErrorFileHandler()
observer.schedule(event_handler, path='.', recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()