import os
import pandas as pd
import csv

import datetime

# Make one function for each KPI and then a "main" function at the end that
# just calls all of them in order and updates the KPIs table

fehler_excel_path= 'Reject_Button.xlm'
FabrikVerbindung = pd.read_excel('FabrikVerbindung.xlsx')


def calculate_average_cycle_time(process, variant, process_df, timestamp):
    # Filter events that happened in the last 24 hours (86400 seconds)
    filtered_process_df = process_df[(process_df["timestamp"] >= timestamp - 86400)
                                     and (process_df["timestamp"] <= timestamp) and process_df["variant"] == variant ]

    # Calculate average cycle time
    return filtered_process_df["duration"].mean()


def calculate_average_leading_time(process, variant, process_df, timestamp):
    process_sequence = ["Saegen/Drehen", "Fraesen", "Waschen", "Messen",
                        "Transport/Lieferung", "Transport/Montage", "Montage"]
    # We will probably have to change this to a conditional, some pieces go through Saegen, others through Drehen

    leading_time = 0
    for name in process_sequence:
        leading_time += calculate_average_cycle_time(process, variant, process_df, timestamp)
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


def calculate_nacharbeitquote(process, batch, variant, process_df, fehler_excel_path):  # Prozentzahl


    today = datetime.date.today()

    # Filter the DataFrame for the desired variant and today's date
    filtered_df = process_df[(process_df['variant'] == variant) & (process_df['date'].dt.date == today)]

    # Count the number of rows in the filtered DataFrame
    variants_today = filtered_df.shape[0]

    total_parts = variants_today * batch

    fehler_excel = pd.read_excel(fehler_excel_path, sheet_name='LogData(Dashboard)')

    for row in fehler_excel.iter_rows():
        for cell in row:
            if cell.value ==process:
                process_cell= cell
                nacharbeitsteil_cell = fehler_excel.cell(row=process_cell.row + 2, column=process_cell.column+1)
                na_teile= nacharbeitsteil_cell.value

                return na_teile*100/total_parts


def calculate_ausschussquote(process, batch, variant, process_df,  fehler_excel_path):  # Prozentzahl



    today = datetime.date.today()

    # Filter the DataFrame for the desired variant and today's date
    filtered_df = process_df[(process_df['variant'] == variant) & (process_df['date'].dt.date == today)]

    # Count the number of rows in the filtered DataFrame
    variants_today = filtered_df.shape[0]

    total_parts =variants_today*batch

    fehler_excel = pd.read_excel(fehler_excel_path, sheet_name='LogData(Dashboard)')

    for row in fehler_excel.iter_rows():
        for cell in row:
            if cell.value ==process:
                process_cell= cell
                ausschissteil_cell = fehler_excel.cell(row=process_cell.row + 2, column=process_cell.column)
                as_teile=  ausschissteil_cell.value

                return as_teile*100/total_parts


def calculate_fehlproduktionsquote(process, variant, FabrikVerbindung, process_df,  fehler_excel):  # Prozentzahl
    return calculate_ausschussquote(process, variant, FabrikVerbindung, process_df,  fehler_excel) + \
           calculate_nacharbeitquote(process)

def calculate_fehlproduktionsquote(process, batch, variant, process_df,  fehler_excel_path):  # Prozentzahl
    return calculate_ausschussquote(process, batch, variant, process_df,  fehler_excel_path) + calculate_nacharbeitquote(process, batch, variant, process_df,  fehler_excel_path)



def calculate_qualitaetsgrad(process):  # Prozentzahl
    return 1 - calculate_fehlproduktionsquote(process)


def calculate_yield(process, variant, process_df):
    today = datetime.date.today()

    # Filter the DataFrame for the desired variant and today's date
    filtered_df = process_df[(process_df['variant'] == variant) & (process_df['date'].dt.date == today)]

    # Count the number of rows in the filtered DataFrame
    variants_today = filtered_df.shape[0]

    filtered_row = FabrikVerbindung[(FabrikVerbindung['process_name'] == process) & (FabrikVerbindung['variant'] == variant)]

    ideal_cycle_time = filtered_row['ideal_cycle_time'].values[0]

    operating_time= 8*3600

    max_parts = operating_time/ideal_cycle_time

    return 100*variants_today/max_parts


def calculate_work_in_process(process, variant, process_df, timestamp):
    # Events in the last 24 hours with exit code 1, that is, those that are still running
    filtered_process_df = process_df[(process_df["timestamp"] >= timestamp - 86400)
                                     and (process_df["timestamp"] <= timestamp)
                                     and (process_df["exit_code"] == 1)]

    filtered_df = FabrikVerbindung[(FabrikVerbindung['variant'] == variant) & (FabrikVerbindung['process_name'] == process)]

    # Get the 'box_capacity' value
    batch = filtered_df['box_capacity'].values[0]
    # Return number of pieces
    return filtered_process_df["quantity"].sum()*batch


def calculate_oee_av(process): #Make a DF with the ideal cycle time per variant in each process

    
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

    return availability

def calculate_oee_pe(process, variant, batch, process_df, FabrikVerbindung):  # Make a DF with the ideal cycle time per variant in each process

    operating_time = 28800  # 8h per day

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

    return total_parts_produced, performance

def calculate_oee_qa(process, variant, batch, process_df,total_parts_produced):  # Make a DF with the ideal cycle time per variant in each process

    # Calculate Quality
    good_parts_produced = total_parts_produced - calculate_fehlproduktionsquote(process, batch, variant, process_df,  fehler_excel_path)

    quality = good_parts_produced / total_parts_produced if total_parts_produced > 0 else 0

    return quality

def calculate_oeestern(total_parts, variant, process_df, timestamp):

    working_time = 8*3600

    return total_parts*calculate_average_cycle_time(variant, process_df, timestamp)/working_time

def calculate_productivity(process):
    # Percentage of uptime I think
    return 1 - calculate_production_downtime(process) - calculate_unscheduled_downtime(process)


def calculate_losgroesse(process, variant):

    filtered_df = FabrikVerbindung[(FabrikVerbindung['variant'] == variant) & (FabrikVerbindung['process_name'] == process)]

    # Get the 'box_capacity' value
    batch = filtered_df['box_capacity'].values[0]
    return batch

# MAIN FUNCTION
def calculate_process_kpis(process, variant, timestamp):
    # Obtain the process.csv as a pandas DF
    current_directory = os.path.dirname(os.path.abspath(__file__))
    process_path = current_directory.join(["..", "..", "Werk", "Prozesse", process, process + ".csv"])
    process_df = pd.read_csv(process_path)

    # Call every function
    fehlproduktionsquote = calculate_fehlproduktionsquote(process)
    qualitaetsgrad = calculate_qualitaetsgrad(process)
    losgroesse = calculate_losgroesse(process, process_df)
    batch = losgroesse
    ausschussquote = calculate_ausschussquote(process, batch, variant, process_df, fehler_excel_path)
    nacharbeitsquote = calculate_nacharbeitquote(process, batch,  variant, process_df, fehler_excel_path)
    average_cycle_time = calculate_average_cycle_time(process, variant, process_df, timestamp)
    average_leading_time = calculate_average_leading_time( process, process_df, timestamp)
    production_downtime = calculate_production_downtime(process, fehler_excel_path)
    unscheduled_downtime = calculate_unscheduled_downtime(process, fehler_excel_path)
    leistung = (process, variant, process_df, timestamp)
    work_in_process = calculate_work_in_process(process, variant, process_df, timestamp)
    oee_av= calculate_oee_av(process)
    total_parts_produced, oee_pe = calculate_oee_pe(process, variant, batch, process_df, FabrikVerbindung)
    oee_qa = calculate_oee_qa(process, variant, batch, process_df,total_parts_produced)
    oee = oee_av*oee_pe*oee_qa*100
    oeestern = calculate_oeestern(total_parts_produced, variant, process_df, timestamp)
    productivity = calculate_productivity(process)


    # Append the calculated values as a row for the process_DS.csv
    hist_log_path = "".join(["..", "Werk", "Prozesse", process,"_HistLog.csv" ])
    ds_path= "".join(["..", "Werk", "Prozesse", process, process + "_DS.csv"])

    row_to_append = [timestamp, fehlproduktionsquote, qualitaetsgrad, ausschussquote,
                     nacharbeitsquote, average_cycle_time, average_leading_time,
                     production_downtime, unscheduled_downtime, leistung, work_in_process,
                     oee, oeestern, oee_av, oee_pe, oee_qa,+ productivity, losgroesse]


    # Check if the CSV file exists
    if not os.path.exists( hist_log_path):
        with open( hist_log_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            # Header row
            header = ["calculated_at", "fehlprodukionsquote", "qualitaetsgrad", "ausschussquote",
                      "nacharbeitsquote", "average_cycle_time", "average_leading_time",
                      "production_downtime", "unscheduled_downtime", "leistung", "work_in_process",
                      "oee","oeestern", "oee_av", "oee_pe", "oee_qa", "productivity", "losgroesse"]
            csv_writer.writerow(header)


    with open(hist_log_path, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Append this instance of calculated KPIs with the timestamp of when they were calculated

        csv_writer.writerow(row_to_append)

    with open(ds_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        #Updates the digital shadow file

        csv_writer.writerow(row_to_append)