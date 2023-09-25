import os
import numpy as np
import pandas as pd
import csv
import openpyxl
import datetime

# Make one function for each KPI and then a "main" function at the end that
# just calls all of them in order and updates the KPIs table

fehler_excel_path= 'Reject_Button.xlm'
FabrikVerbindung = pd.read_excel('FabrikVerbindung.xlsx')
fehler_excel= openpyxl.load_workbook(fehler_excel_path)

def calculate_average_cycle_time(process, variant, process_df, timestamp):
    # Filter events that happened in the last 24 hours (86400 seconds)
    filtered_process_df = process_df[(process_df["timestamp"] >= timestamp - 86400)
                                     and (process_df["timestamp"] <= timestamp) and process_df["variant"] == variant ]

    # Calculate average cycle time
    return filtered_process_df["duration"].mean()


def calculate_average_leading_time(process, process_df, timestamp):
    process_sequence = ["Saegen/Drehen", "Fraesen", "Waschen", "Messen",
                        "Transport/Lieferung", "Transport/Montage", "Montage"]
    # We will probably have to change this to a conditional, some pieces go through Saegen, others through Drehen

    leading_time = 0
    for name in process_sequence:
        leading_time += calculate_average_cycle_time(process, process_df, timestamp)
        if name == process:
            break

    return leading_time


def calculate_production_downtime(process, fehler_excel_path):

    df = pd.read_excel(fehler_excel_path, sheet_name='LogData(Wartung)')

    # Ensure the 'Start', 'End', 'Date', and 'Process' columns exist in the DataFrame
    if 'Start' in df.columns and 'End' in df.columns and 'Date' in df.columns and 'Process' in df.columns:
        # Convert 'Date' column to datetime format (if not already)
        if not pd.api.types.is_datetime64_ns_dtype(df['Date']):
            df['Date'] = pd.to_datetime(df['Date'])

        # Filter rows where 'Start' and 'End' are on the same date and match the desired process
        same_date_and_process_rows = df[(df['Start'].dt.date == df['End'].dt.date) & (df['Process'] == process)]

        # Calculate the sum of 'End' - 'Start' for these rows
        total_duration = same_date_and_process_rows['End'] - same_date_and_process_rows['Start']
        total_duration = total_duration.sum()

        return total_duration
    else:
        return None
def calculate_unscheduled_downtime(process, fehler_excel_path):

    df = pd.read_excel(fehler_excel_path, sheet_name='LogData(Ausfallzeit)')

    # Ensure the 'Start', 'End', 'Date', and 'Process' columns exist in the DataFrame
    if 'Start' in df.columns and 'End' in df.columns and 'Date' in df.columns and 'Process' in df.columns:
        # Convert 'Date' column to datetime format (if not already)
        if not pd.api.types.is_datetime64_ns_dtype(df['Date']):
            df['Date'] = pd.to_datetime(df['Date'])

        # Filter rows where 'Start' and 'End' are on the same date and match the desired process
        same_date_and_process_rows = df[(df['Start'].dt.date == df['End'].dt.date) & (df['Process'] == process)]

        # Calculate the sum of 'End' - 'Start' for these rows
        total_duration = same_date_and_process_rows['End'] - same_date_and_process_rows['Start']
        total_duration = total_duration.sum()

        return total_duration
    else:
        return None


def calculate_nacharbeitquote(process, variant, process_df, fehler_excel):  # Prozentzahl

    # Filter the Excel DataFrame based on the variant and process
    filtered_df = FabrikVerbindung[
        (FabrikVerbindung['variant'] == variant) & (FabrikVerbindung['process_name'] == process)]

    # Get the 'box_capacity' value
    batch = filtered_df['box_capacity'].values[0]

    today = datetime.date.today()

    # Filter the DataFrame for the desired variant and today's date
    filtered_df = process_df[(process_df['variant'] == variant) & (process_df['date'].dt.date == today)]

    # Count the number of rows in the filtered DataFrame
    variants_today = filtered_df.shape[0]

    total_parts = variants_today * batch

    for row in fehler_excel.iter_rows():
        for cell in row:
            if cell.value ==process:
                process_cell= cell
                nacharbeitsteil_cell = fehler_excel.cell(row=process_cell.row + 2, column=process_cell.column+1)
                na_teile= nacharbeitsteil_cell.value

                return na_teile*100/total_parts


def calculate_ausschussquote(process, variant, FabrikVerbindung, process_df,  fehler_excel):  # Prozentzahl

    # Filter the Excel DataFrame based on the variant and process
    filtered_df = FabrikVerbindung[(FabrikVerbindung['variant'] == variant) & (FabrikVerbindung['process_name'] == process)]


    # Get the 'box_capacity' value
    batch = filtered_df['box_capacity'].values[0]

    today = datetime.date.today()

    # Filter the DataFrame for the desired variant and today's date
    filtered_df = process_df[(process_df['variant'] == variant) & (process_df['date'].dt.date == today)]

    # Count the number of rows in the filtered DataFrame
    variants_today = filtered_df.shape[0]

    total_parts =variants_today*batch

    for row in fehler_excel.iter_rows():
        for cell in row:
            if cell.value ==process:
                process_cell= cell
                ausschissteil_cell = fehler_excel.cell(row=process_cell.row + 2, column=process_cell.column)
                as_teile=  ausschissteil_cell.value

                return as_teile*100/total_parts


def calculate_fehlproduktionsquote(process):  # Prozentzahl
    return calculate_ausschussquote(process) + calculate_nacharbeitquote(process)


def calculate_qualitaetsgrad(process):  # Prozentzahl
    return 1 - calculate_fehlproduktionsquote(process)


def calculate_yield(process, process_df, timestamp):
    # Filter events that happened in the last 24 hours (86400 seconds)
    filtered_process_df = process_df[(process_df["timestamp"] >= timestamp - 86400)
                                     and (process_df["timestamp"] <= timestamp)]

    # Add up the total number of produced items (per day)
    return filtered_process_df["quantity"].sum()


def calculate_work_in_process(process, process_df, timestamp):
    # Events in the last 24 hours with exit code 1, that is, those that are still running
    filtered_process_df = process_df[(process_df["timestamp"] >= timestamp - 86400)
                                     and (process_df["timestamp"] <= timestamp)
                                     and (process_df["exit_code"] == 1)]

    # Return number of pieces
    return filtered_process_df["quantity"].sum()


def calculate_oee(process, variant, process_df, FabrikVerbindung): #Make a DF with the ideal cycle time per variant in each process

    
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

    downtime = calculate_unscheduled_downtime(process, fehler_excel_path) +  calculate_production_downtime(process, fehler_excel_path)
    operating_time = 28800 #8h per day
    availability = (operating_time - downtime) / operating_time if operating_time > 0 else 0

    # Calculate Performance



    # Filter the Excel DataFrame based on the variant and process
    filtered_df = FabrikVerbindung[(FabrikVerbindung['variant'] == variant) & (FabrikVerbindung['process_name'] == process)]


    # Get the 'box_capacity' value
    batch = filtered_df['box_capacity'].values[0]

    today = datetime.date.today()

    # Filter the DataFrame for the desired variant and today's date
    filtered_df = process_df[(process_df['variant'] == variant) & (process_df['date'].dt.date == today)]

    # Count the number of rows in the filtered DataFrame
    variants_today = filtered_df.shape[0]

    total_parts_produced =variants_today*batch

    # Filter the DataFrame to get the ideal_cycle_time
    filtered_row = FabrikVerbindung[(FabrikVerbindung['process_name'] == process) & (FabrikVerbindung['variant'] == variant)]

    ideal_cycle_time = filtered_row['ideal_cycle_time'].values[0]

    performance = (ideal_cycle_time * total_parts_produced) / operating_time if operating_time > 0 else 0

    # Calculate Quality
    good_parts_produced = total_parts_produced - calculate_fehlproduktionsquote(process, variant)*total_parts_produced/100

    quality = good_parts_produced / total_parts_produced if total_parts_produced > 0 else 0

    # Calculate OEE
    oee = availability * performance * quality * 100  # Multiply by 100 to get percentage

    return oee




def calculate_productivity(process, process_df, timestamp):
    # Percentage of uptime I think
    return 1 - calculate_production_downtime(process) - calculate_unscheduled_downtime(process)


def calculate_losgroesse(process, variant, process_df, timestamp):

    filtered_df = FabrikVerbindung[(FabrikVerbindung['variant'] == variant) & (FabrikVerbindung['process_name'] == process)]

    # Get the 'box_capacity' value
    batch = filtered_df['box_capacity'].values[0]
    return batch

# MAIN FUNCTION
def calculate_process_kpis(process, timestamp):
    # Obtain the process.csv as a pandas DF
    current_directory = os.path.dirname(os.path.abspath(__file__))
    process_path = current_directory.join(["..", "..", "Werk", "Prozesse", process, process + ".csv"])
    process_df = pd.read_csv(process_path)

    # Call every function
    fehlproduktionsquote = calculate_fehlproduktionsquote(process)
    qualitaetsgrad = calculate_qualitaetsgrad(process)
    ausschussquote = calculate_ausschussquote(process, process_df, fehler_excel)
    nacharbeitsquote = calculate_nacharbeitquote(process, process_df, fehler_excel)
    average_cycle_time = calculate_average_cycle_time(process, process_df, timestamp)
    average_leading_time = calculate_average_leading_time(process, process_df, timestamp)
    production_downtime = calculate_production_downtime(process)
    unscheduled_downtime = calculate_unscheduled_downtime(process)
    leistung = calculate_yield(process, process_df, timestamp)
    work_in_process = calculate_work_in_process(process, process_df, timestamp)
    oee = calculate_oee(process, process_df, timestamp)
    productivity = calculate_productivity(process, process_df, timestamp)
    losgroesse = calculate_losgroesse(process, process_df, timestamp)

    # Append the calculated values as a row for the process_DS.csv
    digital_shadow_path = "".join(["..", "Werk", "Prozesse", process, process + "_DS.csv"])

    # Check if the CSV file exists
    if not os.path.exists(digital_shadow_path):
        with open(digital_shadow_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            # Header row
            header = ["calculated_at", "fehlprodukionsquote", "qualitaetsgrad", "ausschussquote",
                      "nacharbeitsquote", "average_cycle_time", "average_leading_time",
                      "production_downtime", "unscheduled_downtime", "leistung", "work_in_process",
                      "oee", "productivity", "losgroesse"]
            csv_writer.writerow(header)

    with open(digital_shadow_path, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Append this instance of calculated KPIs with the timestamp of when they were calculated
        row_to_append = [timestamp, fehlproduktionsquote, qualitaetsgrad, ausschussquote,
                         nacharbeitsquote, average_cycle_time, average_leading_time,
                         production_downtime, unscheduled_downtime, leistung, work_in_process,
                         oee, productivity, losgroesse]
        csv_writer.writerow(row_to_append)
