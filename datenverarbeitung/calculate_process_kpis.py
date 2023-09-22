import os
import numpy as np
import pandas as pd
import csv
import openpyxl
import datetime

# Make one function for each KPI and then a "main" function at the end that
# just calls all of them in order and updates the KPIs table

fehler_excel_path= 'Reject_Button.xlm'
fehler_excel= openpyxl.load_workbook(fehler_excel_path)['Dashboard']

def calculate_average_cycle_time(process, process_df, timestamp):
    # Filter events that happened in the last 24 hours (86400 seconds)
    filtered_process_df = process_df[(process_df["timestamp"] >= timestamp - 86400)
                                     and (process_df["timestamp"] <= timestamp)]

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


def calculate_production_downtime(process, fehler_excel):

    
        print(process)  # get from Jungmu
        return 0  # temp


def calculate_unscheduled_downtime(process):
    print(process)  # get from Jungmu
    return 0  # temp


def calculate_nacharbeitquote(process, process_df, fehler_excel):  # Prozentzahl

    total_parts = len(process_df)
    today = datetime.date.today()
    count_today = (process_df['date'].dt.date == today).sum()

    for row in fehler_excel.iter_rows():
        for cell in row:
            if cell.value ==process:
                process_cell= cell
                nacharbeitsteil_cell = fehler_excel.cell(row=process_cell.row + 2, column=process_cell.column+1)
                na_teile= nacharbeitsteil_cell.value

                return na_teile*100/total_parts



def calculate_ausschussquote(process, process_df,  fehler_excel):  # Prozentzahl
    
   
    total_parts = len(process_df)
    today = datetime.date.today()
    count_today = (dprocess_df['date'].dt.date == today).sum()

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


def calculate_oee(process, process_df, timestamp, cycle_df): #Make a DF with the ideal cycle time per variant in each process

    
    # Calculate Overall Equipment Effectiveness (OEE).

    # Parameters:
    # - operating_time: Total time the equipment was in operation (in the same time unit as downtime).
    # - downtime: Total downtime, including unplanned and planned (in the same time unit as operating_time).
    # - ideal_cycle_time: Theoretical or maximum cycle time for producing one part.
    # - total_parts_produced: Total number of parts produced during the operating time.
    # - good_parts_produced: Number of good-quality parts produced during the operating time.

    # Returns:
    # - OEE as a percentage (0 to 100).
    

    total_parts_produced = len(process_df)

    # Calculate Availability
    availability = (operating_time - downtime) / operating_time if operating_time > 0 else 0

    # Calculate Performance



    performance = (ideal_cycle_time * total_parts_produced) / operating_time if operating_time > 0 else 0

    # Calculate Quality
    quality = good_parts_produced / total_parts_produced if total_parts_produced > 0 else 0

    # Calculate OEE
    oee = availability * performance * quality * 100  # Multiply by 100 to get percentage

    return oee

    print(process)  # No clue how to do this for now, check formulas later
    return 0  # temp


def calculate_productivity(process, process_df, timestamp):
    # Percentage of uptime I think
    return 1 - calculate_production_downtime(process) - calculate_unscheduled_downtime(process)


def calculate_losgroesse(process, process_df, timestamp):
    # I think it's the number of parts per operation, we have that in Excel
    return process_df["quantity"].iloc[0]


# MAIN FUNCTION
def calculate_process_kpis(process, timestamp):
    # Obtain the process.csv as a pandas DF
    current_directory = os.path.dirname(os.path.abspath(__file__))
    process_path = current_directory.join(["..", "..", "Werk", "Prozesse", process, process + ".csv"])
    process_df = pd.read_csv(process_path)

    # Call every function
    fehlproduktionsquote = calculate_fehlproduktionsquote(process)
    qualitaetsgrad = calculate_qualitaetsgrad(process)
    ausschussquote = calculate_ausschussquote(process, process_df,fehler_excel)
    nacharbeitsquote = calculate_nacharbeitquote(process, process_df,fehler_excel)
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
