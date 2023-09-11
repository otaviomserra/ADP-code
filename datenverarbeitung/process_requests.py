import pandas as pd

FabrikVerbindung = pd.read_excel("FabrikVerbindung.xlsx", index_col=0)


class ProcessRequest:
    def __init__(self, lane, timestamp):
        # Uses the given origin lane and takes the appropriate target lane from the Excel file
        self.origin_lane = lane
        self.target_lane = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "target_lane_address"].iloc[0]
        self.process = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "process_name"].iloc[0]

        # Events: used to create the process log, put_time is empty for now because the request is still active
        self.pick_time = timestamp
        self.put_time = 0
        self.duration = 0

        # Exit code: 1 when request is active, 0 when request is completed, 2 when request is canceled
        self.exit_code = 1

    def resolve(self, timestamp):
        self.put_time = timestamp
        # Calculate here the difference in timestamps
        self.duration = self.put_time - self.pick_time
        # Mark the request as resolved
        self.exit_code = 0

    def cancel(self, timestamp):
        self.duration = timestamp - self.put_time
        # Mark the request as canceled; the system should then remove it from the list without
        # creating a new process log
        self.exit_code = 2

    def generate_process_log(self):
        print(self.process)  # Placeholder
        # Append the process (duration, lanes, name) to whatever format Klint is using
