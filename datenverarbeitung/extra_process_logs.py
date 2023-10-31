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


def reformat_data(process, new_instance_df):
    # Obtain date
    raw_date = new_instance_df["Datum"].values[0]
    # Reformat date into DD.MM.YYYY
    input_date = datetime.strptime(raw_date, "%A, %B %d, %Y")
    date = input_date.strftime("%d.%m.%Y")

    # Obtain start and end times
    pick_time = str(new_instance_df["Start"].values[0])
    put_time = str(new_instance_df["End"].values[0])
    print(pick_time)
    print(put_time)

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

    try:
        # Obtain variant
        variant = new_instance_df["Bauteil"].values[0].replace("-", "").replace("0", "")  # Translating from Jungmu
    except:
        variant = "FB1"

    # Obtain quantity
    if process == "Montage":
        menge = 1
    elif ("FK" in variant) or (variant == "FB1"):
        menge = 8
    else:
        menge = 4

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


def log_error(process, variant, fehler_df):
    # Log for Fehlproduktionsquote
    current_directory = os.path.dirname(os.path.abspath(__file__))
    relative_path = os.path.join("..", "Werk", "Prozesse", process, process + ".csv")
    log_path = os.path.join(current_directory, relative_path)

    process_log = pd.read_csv(log_path)
    # Change the last exit code matching the variant to 2
    filtered_df = process_log[(process_log['variant'] == variant) & (process_log['exit_code'] == 0)]
    last_index = filtered_df.index[-1]
    process_log.at[last_index, 'exit_code'] = 2

    process_log.to_csv(log_path, index=False)

    # Log for Ausschuss/Nacharbeitsquote
    if process != "Montage":
        today = process_log.tail(1)["date"].iloc[0]
        processes_today = process_log[process_log["date"] == today]

        input_date = datetime.strptime(today, "%d.%m.%Y")
        reformatted_today = input_date.strftime("%A, %B %d, %Y")

        filtered_fehler_df = fehler_df[(fehler_df["Datum"] == reformatted_today) &
                                       (fehler_df["Bauteil"].str[:2] == variant[:2])]
        nacharbeits_df = filtered_fehler_df[filtered_fehler_df["Ausschusstyp"] == "Nacharbeitsteil"]
        num_nacharbeit = nacharbeits_df.shape[0]
        ausschuss_df = filtered_fehler_df[filtered_fehler_df["Ausschusstyp"] == "Ausschussteil"]
        num_ausschuss = ausschuss_df.shape[0]

        num_total = processes_today.shape[0]

        try:
            nacharbeitsquote = num_nacharbeit / num_total
            ausschussquote = num_ausschuss / num_total
        except ZeroDivisionError:
            nacharbeitsquote = 0
            ausschussquote = 0

        current_directory = os.path.dirname(os.path.abspath(__file__))
        process_folder = os.path.join(current_directory, '..', 'Werk', 'Prozesse', process)
        file_path = os.path.join(process_folder, f'{process}_DS.csv')
        write_kpi(file_path, "Nacharbeitsquote", int(100*nacharbeitsquote))
        write_kpi(file_path, "Ausschussquote", int(100*ausschussquote))
        write_kpi(file_path, "Fehlproduktionsquote", int(100*(nacharbeitsquote + ausschussquote)))


try:
    while True:
        time1 = datetime.now()
        print(f"Time 1 is {time1}")
        workbook = app.books.open(process_excel_path, read_only=True)
        for sheet in workbook.sheets:
            current_state = sheet.used_range.address
            if current_state != sheet_states[sheet.name]:
                # The sheet has changed
                print(f"Change detected in sheet '{sheet.name}'")
                # Add your logic to handle the change here
                # Generating process logs
                if sheet.name in ["LogData(Saegen)", "LogData(Drehen)", "LogData(Waschen)", "LogData(Montagezeit)"]:
                    print("Found the sheet")
                    # Extract process name
                    prefix = "LogData("
                    suffix = ")"
                    process_name = sheet.name[len(prefix):-len(suffix)]
                    if process_name == "Montagezeit":
                        process_name = "Montage"

                    # Extract the new line and use it to generate the process logs
                    process_df = pd.read_excel(process_excel_path, sheet_name=sheet.name)
                    new_row = process_df.tail(1)

                    # Use the new row to generate process logs
                    process_to_append = reformat_data(process_name, new_row)
                    generate_process_log(process_name, process_to_append)

                    # Update the sheet state
                    sheet_states[sheet.name] = current_state

                elif sheet.name == "LogData(Fertigung)":
                    process_df = pd.read_excel(process_excel_path, sheet_name=sheet.name)
                    new_row = process_df.tail(1)

                    variant = new_row["Bauteil"].values[0].replace("-", "").replace("0", "")
                    process_per_variant = {"FS1": "Saegen", "FS2": "Saegen", "FB1": "Fraesen", "FB2": "Fraesen",
                                           "FK1": "Drehen", "FK2": "Drehen", "FK3": "Drehen", "FK4": "Drehen",
                                           "FK5": "Drehen", "FK6": "Drehen", "FK7": "Drehen", "FK8": "Drehen"}

                    log_error(process_per_variant[variant], variant, process_df)
                    print(f"Error logged for {process_per_variant[variant]}")

                    # Update the sheet state
                    sheet_states[sheet.name] = current_state

                elif sheet.name == "LogData(Montage)":
                    process_df = pd.read_excel(process_excel_path, sheet_name=sheet.name)
                    new_row = process_df.tail(1)

                    log_error("Montage", "FB1", process_df)
                    print("Error logged for Montage")

                    # Update the sheet state
                    sheet_states[sheet.name] = current_state

                else:
                    pass
        workbook.close()
        time2 = datetime.now()
        print(f"Time 2 is {time2}")
        time.sleep(10)

except KeyboardInterrupt:
    pass
finally:
    app.quit()
