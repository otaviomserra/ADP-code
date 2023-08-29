import pandas as pd
import numpy as np
import os
import re
import time
from threading import Lock
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Global lock to ensure only one instance of the program runs at a time
program_lock = Lock()

class LogFileHandler(FileSystemEventHandler):
    def __init__(self, path):
        self.path = path

    def on_modified(self, event):
        # Check if it's a file modification event and the modified file is 'teste.log'
        if event.is_directory:
            return
        if event.src_path == self.path:
            self.process_log_file()

    def process_log_file(self):
        with program_lock:
            # Read and process the log file
            log_data = open(self.path, 'r')
            corrected_lines = []
            for line in log_data:
                if line.startswith("["):
                    corrected_lines.append(line)
                else:
                    corrected_lines[-1] += line
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

            # Creating path for csv files
            if not os.path.exists('csv-logs'):
                os.makedirs('csv-logs')

            # Saving the csv files
            df.to_csv('csv-logs/df_teste.csv', index=False)
            df.to_excel('csv-logs/df_teste.xlsx')
            log_data.close()

def monitor_log_file(log_path):
    event_handler = LogFileHandler(log_path)
    observer = Observer()
    observer.schedule(event_handler, path=log_path)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    log_file_path = 'teste.log'
    monitor_log_file(log_file_path)
    print('rodou')