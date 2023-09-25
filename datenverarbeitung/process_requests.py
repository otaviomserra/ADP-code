import os
import csv
import pandas as pd

FabrikVerbindung = pd.read_excel("FabrikVerbindung.xlsx", index_col=0)


class ProcessRequest:
    def __init__(self, date, lane, timestamp):
        # Uses the given origin lane and takes the appropriate target lane from the Excel file
        self.origin_lane = lane
        self.date = date
        lanes_string = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "target_lane_address"].iloc[0]
        self.target_lanes = lanes_string.split(",")
        self.process = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "process_name"].iloc[0]
        self.variant = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "variant"].iloc[0]

        # Events: used to create the process log, put_time is empty for now because the request is still active
        self.pick_time = timestamp
        self.put_time = 0
        self.duration = 0

        # Exit code: 1 when request is active, 0 when request is completed, 2 when request is canceled
        self.exit_code = 1

    def resolve(self, timestamp):
        self.put_time = timestamp
        # Calculate here the difference in timestamps
        # self.duration = self.put_time - self.pick_time
        # Mark the request as resolved
        self.exit_code = 0

    def cancel(self, timestamp):
        # self.duration = timestamp - self.put_time
        # Mark the request as canceled; the system should then remove it from the list without
        # creating a new process log
        self.exit_code = 2

    def generate_process_log(self, lane):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        relative_path = os.path.join("..", "Werk", "Prozesse", self.process, self.process + ".csv")
        log_path = os.path.join(current_directory, relative_path)

        # Check if the CSV file exists
        if not os.path.exists(log_path):
            with open(log_path, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                # Header row
                header = ["date", "pick_time", "put_time", "origin_lane", "target_lane", "duration", "variant"]
                csv_writer.writerow(header)

        with open(log_path, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            # Append this instance of the process
            process_to_append = [self.date, self.pick_time, self.put_time, self.origin_lane, lane,
                                 self.duration, self.variant]
            csv_writer.writerow(process_to_append)

        print("Process log created :D at")
        print(log_path)
