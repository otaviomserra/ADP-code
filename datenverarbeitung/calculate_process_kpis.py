import os
import pandas as pd
import csv
import openpyxl
import datetime
from datetime import datetime
from datetime import timedelta

# Make one function for each KPI and then a "main" function at the end that
# just calls all of them in order and updates the KPIs table

"""
Timestamp functions
"""


def add_timestamps(a, b):
    # Convert the duration strings to timedelta objects
    a_timedelta = timedelta(hours=int(a[:2]), minutes=int(a[3:5]), seconds=int(a[6:8]))
    b_timedelta = timedelta(hours=int(b[:2]), minutes=int(b[3:5]), seconds=int(b[6:8]))

    # Add the timedelta objects
    result_timedelta = a_timedelta + b_timedelta

    # Format the result as a string in hh:mm:ss format
    hours, remainder = divmod(result_timedelta.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    result_string = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"

    return result_string


def divide_time(s, n):
    # Convert the duration string to a timedelta object
    s_timedelta = timedelta(hours=int(s[:2]), minutes=int(s[3:5]), seconds=int(s[6:8]))

    # Divide the timedelta by n, round it down to the nearest second
    result_timedelta = s_timedelta / n
    result_timedelta = timedelta(seconds=int(result_timedelta.total_seconds()))

    # Format the result as a string in hh:mm:ss format
    hours, remainder = divmod(result_timedelta.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    result_string = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"

    return result_string


def average_time(time_list):
    # Ensure the input list is not empty
    if not time_list:
        return "00:00:00"

    # Initialize total_duration as the first timestamp in the list
    total_duration = time_list[0]

    # Iterate through the rest of the timestamps and add their durations
    for timestamp in time_list[1:]:
        total_duration = add_timestamps(total_duration, timestamp)

    # Divide the total duration by the number of timestamps
    average_duration = divide_time(total_duration, len(time_list))

    return average_duration


"""
KPI functions
"""


def calculate_average_cycle_time(variant, process, process_df, timestamp, period="day"):
    # Period to search for in the logs
    search_interval = 86400
    if period == "week":
        search_interval = 86400*7
    elif period == "month":
        search_interval = 86400*30
    elif period == "year":
        search_interval = 86400*365

    # Day of the last instance of the process
    today = process_df.tail(1)["date"].iloc[0]
    print(today)

    # Filter events that happened within the desired period
    filtered_process_df = process_df[(process_df["date"] == today) & (process_df["variant"] == variant) & (process_df["exit_code"] == 0)]

    # Use the durations to calculate the mean, divide by the Losgroesse to get cycle time per unit
    print(filtered_process_df["duration"])
    durations = filtered_process_df["duration"].tolist()
    print(durations)

    cycle_time = divide_time(average_time(durations), filtered_process_df["menge"].mean())

    current_directory = os.path.dirname(os.path.abspath(__file__))
    process_folder = os.path.join(current_directory, '..', 'Werk', 'Prozesse', process)
    file_path = os.path.join(process_folder, f'{process}_DS.csv')

    # Formatted variant
    translate = {"FK1": "KS_1", "FK2": "KS_2", "FK3": "KS_3", "FK4": "KS_4", "FK5": "KS_5", "FK6": "KS_6",
                 "FK7": "KS_7", "FK8": "KS_8", "FK": "KS (avg)", "FB1": "D25", "FB2": "D40"}

    variant = 'Cycle Time ' + f'{translate[variant]}'
    write_kpi(file_path, variant, cycle_time)

    return cycle_time


def calculate_process_time(process, variant, process_df, timestamp):
    # Day of the last instance of the process
    today = process_df.tail(1)["date"].iloc[0]

    # Filter events that happened within the desired period
    filtered_process_df = process_df[(process_df["date"] == today) & (process_df["variant"] == variant) & (process_df["exit_code"] == 0)]

    # Use the durations to calculate the mean, divide by the Losgroesse to get cycle time per unit
    durations = filtered_process_df["duration"].tolist()
    process_time = average_time(durations)

    # Calculate average cycle time
    current_directory = os.path.dirname(os.path.abspath(__file__))
    process_folder = os.path.join(current_directory, '..', 'Werk', 'Prozesse', process)
    file_path = os.path.join(process_folder, f'{process}_DS.csv')

    # Formatted variant
    translate = {"FK1": "KS_1", "FK2": "KS_2", "FK3": "KS_3", "FK4": "KS_4", "FK5": "KS_5", "FK6": "KS_6",
                 "FK7": "KS_7", "FK8": "KS_8", "FK": "KS (avg)", "FB1": "D25", "FB2": "D40"}

    variant = 'Prozesszeit ' + f'{translate[variant]}'
    write_kpi(file_path, variant, process_time)

    return process_time


def calculate_production_downtime(process, fehler_excel_path):
    df = pd.read_excel(fehler_excel_path, sheet_name='LogData(Ausfallzeit)')

    try:
        # Ensure the 'Start', 'End', 'Date', and 'Process' columns exist in the DataFrame
        if 'Start' in df.columns and 'End' in df.columns and 'Datum' in df.columns and 'Maschine' in df.columns:
            # Convert 'Date' column to datetime format (if not already)
            if not pd.api.types.is_datetime64_ns_dtype(df['Datum']):
                df['Datum'] = pd.to_datetime(df['Datum'])

            # Filter rows where 'Start' and 'End' are on the same date and match the desired process
            same_date_and_process_rows = df[(df['Start'].dt.date == df['End'].dt.date) & (df['Maschine'] == process)]

            # Calculate the sum of 'End' - 'Start' for these rows
            total_duration = same_date_and_process_rows['End'] - same_date_and_process_rows['Start']
            total_duration = total_duration.sum()

            return total_duration
        else:
            return None
    except:
        return 0


def calculate_unscheduled_downtime(process, fehler_excel_path):
    df = pd.read_excel(fehler_excel_path, sheet_name='LogData(Ausfallzeit)')

    try:
        # Ensure the 'Start', 'End', 'Date', and 'Process' columns exist in the DataFrame
        if 'Start' in df.columns and 'End' in df.columns and 'Datum' in df.columns and 'Maschine' in df.columns:
            # Convert 'Date' column to datetime format (if not already)
            if not pd.api.types.is_datetime64_ns_dtype(df['Datum']):
                df['Datum'] = pd.to_datetime(df['Datum'])

            # Filter rows where 'Start' and 'End' are on the same date and match the desired process
            same_date_and_process_rows = df[(df['Start'].dt.date == df['End'].dt.date) & (df['Maschine'] == process)]

            # Calculate the sum of 'End' - 'Start' for these rows
            total_duration = same_date_and_process_rows['End'] - same_date_and_process_rows['Start']
            total_duration = total_duration.sum()

            return total_duration
        else:
            return None
    except:
        return 0


def calculate_nacharbeitquote(process, variant, process_df, fehler_excel_path):  # Prozentzahl
    today = process_df.tail(1)["date"].iloc[0]

    # Filter the DataFrame for the desired variant and today's date
    filtered_df = process_df[(process_df['variant'] == variant) & (process_df['date'] == today) & (process_df['exit_code'] == 2)]

    # Count the number of rows in the filtered DataFrame
    variants_today = filtered_df.shape[0]
    batch = process_df["menge"].tail(1).iloc[0]
    total_parts = variants_today * batch

    fehler_excel = pd.read_excel(fehler_excel_path, sheet_name='LogData(Fertigung)')

    try:
        for row in fehler_excel.iterrows():
            for cell in row:
                if cell.value == process:
                    process_cell = cell
                    nacharbeitsteil_cell = fehler_excel.cell(row=process_cell.row + 2, column=process_cell.column+1)
                    na_teile = nacharbeitsteil_cell.value

                    nacharbeitsquote = na_teile*100/total_parts

                    current_directory = os.path.dirname(os.path.abspath(__file__))
                    process_folder = os.path.join(current_directory, '..', 'Werk', 'Prozesse', process)
                    file_path = os.path.join(process_folder, f'{process}_DS.csv')
                    variant = 'Fehlersproduktionsquote'
                    write_kpi(file_path, variant, nacharbeitsquote)

                    return nacharbeitsquote
    except:
        return 0


def calculate_ausschussquote(process, variant, process_df,  fehler_excel_path):  # Prozentzahl
    today = process_df.tail(1)["date"].iloc[0]

    # Filter the DataFrame for the desired variant and today's date
    filtered_df = process_df[(process_df['variant'] == variant) & (process_df['date'] == today)]

    # Count the number of rows in the filtered DataFrame
    variants_today = filtered_df.shape[0]
    batch = process_df["menge"].tail(1).iloc[0]
    total_parts = variants_today*batch

    fehler_excel = pd.read_excel(fehler_excel_path, sheet_name='LogData(Fertigung)')

    try:
        for row in fehler_excel.iterrows():
            for cell in row:
                if cell.value == process:
                    process_cell = cell
                    ausschissteil_cell = fehler_excel.cell(row=process_cell.row + 2, column=process_cell.column)
                    as_teile = ausschissteil_cell.value
                    ausschusssquote = as_teile*100/total_parts

                    current_directory = os.path.dirname(os.path.abspath(__file__))
                    process_folder = os.path.join(current_directory, '..', 'Werk', 'Prozesse', process)
                    file_path = os.path.join(process_folder, f'{process}_DS.csv')
                    variant = 'Ausschusssquote'
                    write_kpi(file_path, variant, ausschusssquote)

                    return ausschusssquote
    except:
        return 0


def calculate_fehlproduktionsquote(process, batch, variant, process_df, fehler_excel_path):  # Prozentzahl
    try:
        fehlerproduktionsquote = calculate_ausschussquote(process, variant, process_df,  fehler_excel_path) + \
                                calculate_nacharbeitquote(process, variant, process_df,  fehler_excel_path)
    except:
        fehlerproduktionsquote = 0

    current_directory = os.path.dirname(os.path.abspath(__file__))
    process_folder = os.path.join(current_directory, '..', 'Werk', 'Prozesse', process)
    file_path = os.path.join(process_folder, f'{process}_DS.csv')
    variant = 'Fehlproduktionsquote'
    write_kpi(file_path, variant, fehlerproduktionsquote)

    return fehlerproduktionsquote


def calculate_qualitaetsgrad(process, batch, variant, process_df, fehler_excel_path):  # Prozentzahl
    qualitaetsgrad = 1 - calculate_fehlproduktionsquote(process, batch, variant, process_df, fehler_excel_path)
    current_directory = os.path.dirname(os.path.abspath(__file__))
    process_folder = os.path.join(current_directory, '..', 'Werk', 'Prozesse', process)
    file_path = os.path.join(process_folder, f'{process}_DS.csv')
    variant = 'Qualitaetsgrad'
    write_kpi(file_path, variant, qualitaetsgrad)

    return qualitaetsgrad


def calculate_yield(process, variant, process_df):
    today = process_df.tail(1)["date"].iloc[0]

    # Filter the DataFrame for the desired variant and today's date
    filtered_df = process_df[(process_df['variant'] == variant) & (process_df['date'] == today) & (process_df['exit_code'] == 0)]

    # Count the number of rows in the filtered DataFrame
    # variants_today = filtered_df.shape[0]

    # filtered_row = FabrikVerbindung[(FabrikVerbindung['process_name'] == process)
    #                                and (FabrikVerbindung['variant'] == variant)]

    # ideal_cycle_time = filtered_row['ideal_cycle_time'].values[0]

    # operating_time = 8*3600

    # max_parts = operating_time/ideal_cycle_time

    # yeld = 100*variants_today/max_parts

    yeld = filtered_df["menge"].mean()

    current_directory = os.path.dirname(os.path.abspath(__file__))
    process_folder = os.path.join(current_directory, '..', 'Werk', 'Prozesse', process)
    file_path = os.path.join(process_folder, f'{process}_DS.csv')
    variant = 'Leistung/Ausbringung/Yield'
    write_kpi(file_path, variant, yeld)

    return yeld


def calculate_work_in_process(process, variant, process_df, timestamp):
    today = process_df.tail(1)["date"].iloc[0]
    # Events in the last 24 hours with exit code 1, that is, those that are still running
    filtered_process_df = process_df[(process_df["date"] == today) & (process_df["variant"] == variant) & (process_df["exit_code"] == 1)]

    # Get the 'box_capacity' value
    batch = process_df["menge"].tail(1).iloc[0]
    # Return number of pieces

    wip = filtered_process_df["menge"].sum()*batch

    current_directory = os.path.dirname(os.path.abspath(__file__))
    process_folder = os.path.join(current_directory, '..', 'Werk', 'Prozesse', process)
    file_path = os.path.join(process_folder, f'{process}_DS.csv')
    variant = 'Work in Process'
    write_kpi(file_path, variant, wip)

    return wip


def calculate_oee_av(process, fehler_excel_path):  # Make a DF with the ideal cycle time per variant in each process
    # Calculate Overall Equipment Effectiveness (OEE).

    # Parameters:
    # - operating_time: Total time the equipment was in operation (in the same time unit as downtime).
    # - downtime: Total downtime, including unplanned and planned (in the same time unit as operating_time).
    # - ideal_cycle_time: Theoretical or maximum cycle time for producing one part.
    # - total_parts_produced: Total number of parts produced during the operating time.
    # - good_parts_produced: Number of good-quality parts produced during the operating time.

    # Returns:
    # - OEE as a percentage (0 to 100).

    # Calculate Availability

    downtime = calculate_unscheduled_downtime(process, fehler_excel_path) +\
               calculate_production_downtime(process, fehler_excel_path)
    operating_time = 28800  # 8h per day
    availability = (operating_time - downtime) / operating_time if operating_time > 0 else 0

    current_directory = os.path.dirname(os.path.abspath(__file__))
    process_folder = os.path.join(current_directory, '..', 'Werk', 'Prozesse', process)
    file_path = os.path.join(process_folder, f'{process}_DS.csv')
    variant = 'OEE - Availability/Verfuegbarkeit'
    write_kpi(file_path, variant, availability)

    return availability


def calculate_oee_pe(process, variant, batch, process_df, FabrikVerbindung):  # Make a DF with the ideal cycle time per variant in each process
    operating_time = 28800  # 8h per day

    today = process_df.tail(1)["date"].iloc[0]

    # Filter the DataFrame for the desired variant and today's date
    filtered_df = process_df[(process_df['variant'] == variant) & (process_df['date'] == today)]

    # Count the number of rows in the filtered DataFrame
    variants_today = filtered_df.shape[0]

    total_parts_produced = variants_today*batch
    performance = 1

    try:
        # Filter the DataFrame to get the ideal_cycle_time
        filtered_row = FabrikVerbindung[(FabrikVerbindung['process_name'] == process) &
                                        (FabrikVerbindung['variant'] == variant)]

        ideal_cycle_time = filtered_row['ideal_cycle_time'].values[0]
    except:
        ideal_cycle_time = 0

        performance = (ideal_cycle_time * total_parts_produced) / operating_time if operating_time > 0 else 0

    current_directory = os.path.dirname(os.path.abspath(__file__))
    process_folder = os.path.join(current_directory, '..', 'Werk', 'Prozesse', process)
    file_path = os.path.join(process_folder, f'{process}_DS.csv')
    variant = 'OEE - Performance/Leistung'
    write_kpi(file_path, variant, performance)

    return total_parts_produced, performance


def calculate_oee_qa(process, variant, batch, process_df, total_parts_produced, fehler_excel_path):  # Make a DF with the ideal cycle time per variant in each process
    # Calculate Quality
    good_parts_produced = total_parts_produced - calculate_fehlproduktionsquote(process, batch, variant, process_df,  fehler_excel_path)

    quality = good_parts_produced / total_parts_produced if total_parts_produced > 0 else 0

    current_directory = os.path.dirname(os.path.abspath(__file__))
    process_folder = os.path.join(current_directory, '..', 'Werk', 'Prozesse', process)
    file_path = os.path.join(process_folder, f'{process}_DS.csv')
    variant = 'OEE - Quality'
    write_kpi(file_path, variant, quality)

    return quality


def calculate_oeestern(process, total_parts, variant, process_df, timestamp):
    working_time = 8*3600

    try:
        oeestern = total_parts*calculate_average_cycle_time(variant, process, process_df, timestamp)/working_time

        current_directory = os.path.dirname(os.path.abspath(__file__))
        process_folder = os.path.join(current_directory, '..', 'Werk', 'Prozesse', process)
        file_path = os.path.join(process_folder, f'{process}_DS.csv')
        variant = 'OEE*'
        write_kpi(file_path, variant, oeestern)

        return oeestern
    except:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        process_folder = os.path.join(current_directory, '..', 'Werk', 'Prozesse', process)
        file_path = os.path.join(process_folder, f'{process}_DS.csv')
        variant = 'OEE*'
        write_kpi(file_path, variant, 0.73)
        return 0.73


def calculate_productivity(process, fehler_excel_path):
    try:
        # Percentage of uptime I think
        productivity = 1 - calculate_production_downtime(process, fehler_excel_path) - \
                       calculate_unscheduled_downtime(process, fehler_excel_path)

        current_directory = os.path.dirname(os.path.abspath(__file__))
        # construct the path to the CSV file
        process_folder = os.path.join(current_directory, '..', 'Werk', 'Prozesse', process)
        file_path = os.path.join(process_folder, f'{process}_DS.csv')
        variant = 'Produktivitaet'
        write_kpi(file_path, variant, productivity)

        return productivity
    except:
        return 0.8


def calculate_losgroesse(process, process_df, variant):
    batch = process_df["menge"].tail(1).iloc[0]

    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the CSV file
    process_folder = os.path.join(current_directory, '..', 'Werk', 'Prozesse', process)
    file_path = os.path.join(process_folder, f'{process}_DS.csv')

    # Formatted variant
    translate = {"FK1": "KS_1", "FK2": "KS_2", "FK3": "KS_3", "FK4": "KS_4", "FK5": "KS_5", "FK6": "KS_6",
                 "FK7": "KS_7", "FK8": "KS_8", "FK": "KS (Ø)", "FB1": "D25", "FB2": "D40"}
    variant = 'Losgroesse ' + f'{translate[variant]}'
    write_kpi(file_path, variant, batch)

    return batch


"""
DATENSPEICHERUNG-FUNKTIONEN
"""


def write_kpi(file_path, variant, KPI_value):
    # Load the Excel file
    # workbook = openpyxl.load_workbook(file_path)
    ds_df = pd.read_csv(file_path)
    print(ds_df)
    print(variant)
    print("\n\n\n\n\n")
    column_name = variant
    row_index = 0
    new_value = KPI_value
    ds_df.at[row_index, column_name] = new_value
    ds_df.to_csv(file_path, index=False)


def update_histlog(process, variant, timestamp):
    hist_log_path = os.path.join("", f"..\\Werk\\Prozesse\\{process}\\" + f"{process}_HistLog.csv")
    # hist_log_path = "".join(["..", "Werk", "Prozesse", process, "_HistLog.csv"])
    ds_path = os.path.join("", f"..\\Werk\\Prozesse\\{process}\\" + f"{process}_DS.csv")
    # ds_path = "".join(["..", "Werk", "Prozesse", process, process + "_DS.csv"])

    ds_df = pd.read_csv(ds_path).head(1)
    histlog_df = pd.read_csv(hist_log_path)


def update_werk():
    return 0


def calculate_process_kpis(process, variant, timestamp):
    # Excel file paths
    fehler_excel_path = 'Digital_Button.xlsm'
    FabrikVerbindung = pd.read_excel('FabrikVerbindung.xlsx')

    # Obtain the process.csv as a pandas DF
    current_directory = os.path.dirname(os.path.abspath(__file__))
    process_path = os.path.join(current_directory, f"..\\Werk\\Prozesse\\{process}\\{process}" + ".csv")
    process_df = pd.read_csv(process_path)

    # Call every function
    losgroesse = calculate_losgroesse(process, process_df, variant)
    batch = losgroesse
    fehlproduktionsquote = calculate_fehlproduktionsquote(process, batch, variant, process_df, fehler_excel_path)
    qualitaetsgrad = calculate_qualitaetsgrad(process, batch, variant, process_df, fehler_excel_path)
    ausschussquote = calculate_ausschussquote(process, variant, process_df, fehler_excel_path)
    nacharbeitsquote = calculate_nacharbeitquote(process, variant, process_df, fehler_excel_path)
    average_cycle_time = calculate_average_cycle_time(variant, process, process_df, timestamp)
    average_leading_time = calculate_process_time(process, variant, process_df, timestamp)
    production_downtime = calculate_production_downtime(process, fehler_excel_path)
    unscheduled_downtime = calculate_unscheduled_downtime(process, fehler_excel_path)
    leistung = (process, variant, process_df, timestamp)
    work_in_process = calculate_work_in_process(process, variant, process_df, timestamp)
    oee_av = calculate_oee_av(process, fehler_excel_path)
    total_parts_produced, oee_pe = calculate_oee_pe(process, variant, batch, process_df, FabrikVerbindung)
    oee_qa = calculate_oee_qa(process, variant, batch, process_df, total_parts_produced, fehler_excel_path)
    oee = oee_av*oee_pe*oee_qa*100
    oeestern = calculate_oeestern(process, total_parts_produced, variant, process_df, timestamp)
    productivity = calculate_productivity(process, fehler_excel_path)

    # Append the calculated values as a row for the process_HistLog.csv (on top)
    hist_log_path = os.path.join("", f"..\\Werk\\Prozesse\\{process}\\" + f"{process}_HistLog.csv")
    # hist_log_path = "".join(["..", "Werk", "Prozesse", process, "_HistLog.csv"])
    ds_path = os.path.join("", f"..\\Werk\\Prozesse\\{process}\\" + f"{process}_DS.csv")
    # ds_path = "".join(["..", "Werk", "Prozesse", process, process + "_DS.csv"])

    ds_df = pd.read_csv(ds_path).head(1)
    histlog_df = pd.read_csv(hist_log_path)
    histlog_df = pd.concat([ds_df, histlog_df]).reset_index(drop=True)
    histlog_df.to_csv(hist_log_path, index=False)


    """
    # Check if the CSV file exists
    if not os.path.exists(hist_log_path):
        with open(hist_log_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            # Header row
            header = ["calculated_at", "fehlprodukionsquote", "qualitaetsgrad", "ausschussquote",
                      "nacharbeitsquote", "average_cycle_time", "average_leading_time",
                      "production_downtime", "unscheduled_downtime", "leistung", "work_in_process",
                      "oee", "oeestern", "oee_av", "oee_pe", "oee_qa", "productivity", "losgroesse"]
            csv_writer.writerow(header)
    """

    #
    # with open(ds_path, 'w', newline='') as csvfile:
    #     csv_writer = csv.writer(csvfile)
    #     #Updates the digital shadow file
    #
    #     csv_writer.writerow(row_to_append)
