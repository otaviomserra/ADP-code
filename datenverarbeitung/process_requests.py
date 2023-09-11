import os
import pandas as pd
import json
import time
from threading import Lock  # Import Lock from threading module
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

FabrikVerbindung = pd.read_excel("FabrikVerbindung.xlsx", index_col=0)
print(FabrikVerbindung.head())

class ProcessRequest:
    def __init__(self, lane):
        self.origin_lane = lane
        self.target_lane = lane

        # Events: used to create the process log
        self.pick_event = 0
        self.put_event = 0
        self.duration = 0

        # Exit code: 1 when request is active, 0 when request is completed, 2 when request is canceled
        self.exit_code = 1

    def resolve(self, event):
        self.put_event = event
        # Calculate here the difference in timestamps
        self.duration = event
        # Mark request as resolved
        self.exit_code = 0

    def cancel(self, timestamp):
        self.duration = timestamp
        # Mark request as canceled; the system should then remove it from the list without
        # creating a new process log
        self.exit_code = 2

    def generate_process_log(self):
        print("batata")
        # Append the process (duration, lanes, name) to whatever format Klint is using
