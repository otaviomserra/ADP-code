import pandas as pd
from calculate_process_kpis import *

current_directory = os.path.dirname(os.path.abspath(__file__))
for process in ["Fraesen", "Messen", "Montage"]:
    process_path = os.path.join(current_directory, f"..\\Werk\\Prozesse\\{process}\\{process}" + ".csv")
    process_df = pd.read_csv(process_path)

    number_of_rows = process_df.shape[0]
    for i in range(number_of_rows):
        date = process_df.at[i, "date"]
        timestamp = process_df.at[i, "put_time"]
        variant = process_df.at[i, "variant"]

        calculate_process_kpis(process, variant, date, timestamp)
        print(f"Calculated KPIs for {process}\n")
