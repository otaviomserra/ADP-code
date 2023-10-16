import os
import csv
import pandas as pd
from datetime import datetime

FabrikVerbindung = pd.read_excel("FabrikVerbindung.xlsx", index_col=0)


class ProcessRequest:
    def __init__(self, date, lane, timestamp):
        # Uses the given origin lane and takes the appropriate target lane from the Excel file
        self.origin_lane = lane
        self.date = date
        # List of possible target lanes (only to account for S001.M003.02.03 which has a lot of them)
        self.target_lanes = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane,
                                                 "target_lane_address"].iloc[0].split(",")
        self.process = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "process_name"].iloc[0]
        self.variant = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "lane_inventar"].iloc[0]
        self.menge = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "box_capacity"].iloc[0]

        # Events: used to create the process log, put_time is empty for now because the request is still active
        self.pick_time = timestamp
        self.put_time = 0
        self.duration = 0

        # Exit code: 1 when request is active, 0 when request is completed, 2 when request is canceled
        self.exit_code = 1

    def resolve(self, lane, timestamp):
        self.put_time = timestamp
        # Calculate here the difference in timestamps
        # self.duration = self.put_time - self.pick_time
        # Mark the request as resolved

        # Parse the timestamps into datetime objects
        format_string = "%H:%M:%S"
        time_A = datetime.strptime(self.put_time, format_string)
        time_B = datetime.strptime(self.pick_time, format_string)

        # Calculate the time difference
        time_difference = time_A - time_B

        # Extract the time difference components (hours, minutes, seconds)
        hours, remainder = divmod(time_difference.total_seconds(), 3600)
        minutes, seconds = divmod(remainder, 60)

        # Format the time difference as "hh:mm:ss"
        self.duration = "{:02d}:{:02d}:{:02d}".format(int(hours), int(minutes), int(seconds))

        # Specifically for Messen and TransportLieferung (variant is only known at the end):
        if self.origin_lane in ["S001.M002.01.01", "S001.M002.01.02", "S001.M003.02.03"]:
            self.variant = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "lane_inventar"].iloc[0]

        self.exit_code = 0

    def cancel(self, lane, timestamp):
        # self.duration = timestamp - self.put_time
        # Mark the request as canceled; the system should then remove it from the list without
        # creating a new process log

        self.put_time = timestamp
        # Parse the timestamps into datetime objects
        format_string = "%H:%M:%S"
        time_A = datetime.strptime(self.put_time, format_string)
        time_B = datetime.strptime(self.pick_time, format_string)

        # Calculate the time difference
        time_difference = time_A - time_B

        # Extract the time difference components (hours, minutes, seconds)
        hours, remainder = divmod(time_difference.total_seconds(), 3600)
        minutes, seconds = divmod(remainder, 60)

        # Format the time difference as "hh:mm:ss"
        self.duration = "{:02d}:{:02d}:{:02d}".format(int(hours), int(minutes), int(seconds))

        # Specifically for Messen and TransportLieferung (variant is only known at the end):
        if self.origin_lane in ["S001.M002.01.01", "S001.M002.01.02", "S001.M003.02.03"]:
            self.variant = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "lane_inventar"].iloc[0]

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
                header = ["date", "pick_time", "put_time", "origin_lane", "target_lane",
                          "duration", "variant", "menge", "exit_code"]
                csv_writer.writerow(header)

        with open(log_path, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            # Append this instance of the process
            process_to_append = [self.date, self.pick_time, self.put_time, self.origin_lane, lane,
                                 self.duration, self.variant, self.menge, self.exit_code]
            csv_writer.writerow(process_to_append)

        print("Process log created :D at")
        print(log_path)
