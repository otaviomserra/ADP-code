import os
import time
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define the paths to the Excel files and the directory for CSV files
excel_file_paths = ['Start Saegen.xlsx', 'Start Drehen.xlsx']
csv_mapping = {
    'Start Saegen.xlsx': 'Prozesse/Saegen/Saegen.csv',
    'Start Drehen.xlsx': 'Prozesse/Drehen/Drehen.csv',
}

# Function to generate a CSV file path based on the Excel file name
def get_csv_file_path(excel_file_path):
    if excel_file_path in csv_mapping:
        return csv_mapping[excel_file_path]
    else:
        return None

# Function to append the last row of an Excel file to a CSV file
def append_last_row_to_csv(excel_file_path, csv_file_path):
    if csv_file_path is None:
        return

    df = pd.read_excel(excel_file_path)
    last_row = df.iloc[-1:]
    if not os.path.exists(csv_file_path):
        last_row.to_csv(csv_file_path, index=False)
    else:
        last_row.to_csv(csv_file_path, mode='a', header=False, index=False)

# Watchdog event handler to monitor file modifications
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path in excel_file_paths:
            print(f"{event.src_path} has been modified.")
            csv_file_path = get_csv_file_path(event.src_path)
            append_last_row_to_csv(event.src_path, csv_file_path)

# Create the observer and set up the event handler
event_handler = MyHandler()
observer = Observer()
for excel_file_path in excel_file_paths:
    observer.schedule(event_handler, path=os.path.dirname(excel_file_path), recursive=False)

# Start monitoring the directory
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
