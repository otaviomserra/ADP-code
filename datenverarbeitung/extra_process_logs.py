import xlwings as xw
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os.path
import csv
from datetime import datetime
import pythoncom
import win32com
from calculate_process_kpis import *

# I don't even know what this is, but the app crashes without it
xl = win32com.client.Dispatch("Excel.Application", pythoncom.CoInitialize())

# Excel file to be monitored
current_dir = os.path.dirname(__file__)
process_excel_path = os.path.join(current_dir, "Digital_Button.xlsm")
# Open a process to monitor the excel sheets
app = xw.App(visible=False)

# Track the initial state of each sheet
sheet_states = {}
workbook = app.books.open(process_excel_path, read_only=True)
for sheet in workbook.sheets:
    sheet_states[sheet.name] = sheet.used_range.address
workbook.close()
print(sheet_states)


def reformat_data(new_instance_df):
    # Obtain date
    raw_date = new_instance_df["Datum"].values[0]
    # Reformat date into DD.MM.YYYY
    input_date = datetime.strptime(raw_date, "%A, %B %d, %Y")
    date = input_date.strftime("%d.%m.%Y")

    # Obtain start and end times
    pick_time = str(new_instance_df["Start"].values[0])
    put_time = str(new_instance_df["End"].values[0])

    # Origin and target lanes are completely irrelevant for this
    origin_lane = ""
    lane = ""

    # Obtain duration
    time_A = datetime.strptime(pick_time, "%H:%M:%S")
    time_B = datetime.strptime(put_time, "%H:%M:%S")

    time_difference = time_B - time_A

    hours, remainder = divmod(time_difference.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)

    duration = "{:02d}:{:02d}:{:02d}".format(int(hours), int(minutes), int(seconds))

    # Obtain variant
    variant = new_instance_df["Bauteil"].values[0].replace("-", "").replace("0", "")  # Translating from Jungmu

    # Obtain quantity (depends on variant, how would we do this?)
    menge = 4  # Placeholder

    process_to_append = [date, pick_time, put_time, origin_lane, lane, duration, variant, menge, 0]
    return process_to_append


def generate_process_log(process, process_to_append):
    # First, generate the process.csv in MY format.
    current_directory = os.path.dirname(os.path.abspath(__file__))
    relative_path = os.path.join("..", "Werk", "Prozesse", process, process + ".csv")
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
        csv_writer.writerow(process_to_append)

    print("Process log created :D at")
    print(log_path)

    # Calculate kpis
    print(process_to_append[6])
    calculate_process_kpis(process, process_to_append[6], process_to_append[0], process_to_append[2])

    return 0


"""
class ErrorFileHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.last_event_time = None
        self.min_time_interval = 1

    def on_modified(self, event):
        if event.is_directory:
            return

        # Protection against duplicate events
        current_time = time.time()
        if self.last_event_time is None or (current_time - self.last_event_time) >= self.min_time_interval:
            self.last_event_time = current_time

            if event.src_path == process_excel_path:
                # Detects changes in the excel file and shows which sheet was modified
                for sheet in workbook.sheets:
                    current_state = sheet.used_range.address
                    if current_state != sheet_states[sheet.name]:
                        # The sheet has changed
                        print(f"Change detected in sheet '{sheet.name}'")

                        # Generating process logs
                        if sheet.name in ["LogData(Saegen), LogData(Drehen), LogData(Waschen)"]:
                            # Extract process name
                            prefix = "LogData("
                            suffix = ")"
                            process_name = sheet.name[len(prefix):-len(suffix)]

                            # Extract the new line and use it to generate the process logs
                            process_df = pd.read_excel(process_excel_path, sheet_name=sheet.name)
                            new_row = process_df.tail(1)

                            # Use the new row to generate process logs
                            process_to_append = reformat_data(new_row)
                            generate_process_log(process_name, process_to_append)

                            # Update the sheet state
                            sheet_states[sheet.name] = current_state

                        elif sheet.name in ["LogData(Fertigung)", "LogData(Montage)"]:
                            # This can also be used to implement error logs. Not sure if I'll do it here
                            # or if I'll continue to do it the way I did before.
                            pass

                        else:
                            pass
"""

try:
    while True:
        workbook = app.books.open(process_excel_path, read_only=True)
        for sheet in workbook.sheets:
            current_state = sheet.used_range.address
            if current_state != sheet_states[sheet.name]:
                # The sheet has changed
                print(f"Change detected in sheet '{sheet.name}'")
                # Add your logic to handle the change here
                # Generating process logs
                if sheet.name in ["LogData(Saegen)", "LogData(Drehen)", "LogData(Waschen)"]:
                    print("Found the sheet")
                    # Extract process name
                    prefix = "LogData("
                    suffix = ")"
                    process_name = sheet.name[len(prefix):-len(suffix)]

                    # Extract the new line and use it to generate the process logs
                    process_df = pd.read_excel(process_excel_path, sheet_name=sheet.name)
                    new_row = process_df.tail(1)

                    # Use the new row to generate process logs
                    process_to_append = reformat_data(new_row)
                    generate_process_log(process_name, process_to_append)

                    # Update the sheet state
                    sheet_states[sheet.name] = current_state

                elif sheet.name in ["LogData(Fertigung)", "LogData(Montage)"]:
                    # This can also be used to implement error logs. Not sure if I'll do it here
                    # or if I'll continue to do it the way I did before.
                    pass

                else:
                    pass
        workbook.close()
        time.sleep(30)

except KeyboardInterrupt:
    pass
finally:
    app.quit()


"""
# Create an observer to monitor file changes
observer = Observer()
error_handler = ErrorFileHandler()
observer.schedule(error_handler, path=os.path.dirname(process_excel_path), recursive=True)
observer.start()
print("bibo")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
"""