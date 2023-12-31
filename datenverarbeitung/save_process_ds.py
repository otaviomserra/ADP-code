import pandas as pd
import os


# Generate DS files
string = "Fehlproduktionsquote,Qualitaetsgrad,Ausschussquote,Nacharbeitsquote,Cycle Time KS_1,Cycle Time KS_2,Cycle Time KS_3,Cycle Time KS_4,Cycle Time KS_5,Cycle Time KS_6,Cycle Time KS_7,Cycle Time KS_8,Cycle Time KS (avg),Cycle Time D25,Cycle Time D40,Cycle Time D(avg),Produktionsdurchlaufzeit,Prozesszeit KS_1,Prozesszeit KS_2,Prozesszeit KS_3,Prozesszeit KS_4,Prozesszeit KS_5,Prozesszeit KS_6,Prozesszeit KS_7,Prozesszeit KS_8,Prozesszeit KS (avg),Prozesszeit D25,Prozesszeit D40,Prozesszeit D(avg),Production Downtime,Leistung/Ausbringung/Yield,Ausfallzeit,Work in Process,OEE,OEE*,OEE - Availability/Verfuegbarkeit,OEE - Performance/Leistung,OEE - Quality,Produktivitaet,Losgroesse KS_1,Losgroesse KS_2,Losgroesse KS_3,Losgroesse KS_4,Losgroesse KS_5,Losgroesse KS_6,Losgroesse KS_7,Losgroesse KS_8,Losgroesse KS (avg),Losgroesse D25,Losgroesse D40,Losgroesse D (avg),Anzahl Typ"
list = string.split(",")
print(list)
for process in ["Saegen", "Drehen", "Fraesen", "Waschen", "Messen", "Montage"]:
    current_directory = os.path.dirname(os.path.abspath(__file__))
    process_folder = os.path.join(current_directory, '..', 'Werk', 'Prozesse', process)
    file_path = os.path.join(process_folder, f'{process}_DS.csv')

    dictionary = {}
    for column in list:
        dictionary[column] = [0]

    print(dictionary)
    ds_df = pd.DataFrame(dictionary)

    print(ds_df)
    ds_df.to_csv(file_path, index=False)

# Generate histlog files
string = "Date,Time,Variant,Menge,OEE Gesamt,OEE Verfuegbarkeit,OEE Leistung,OEE Qualitaet"
list = string.split(",")
print(list)
for process in ["Saegen", "Drehen", "Fraesen", "Waschen", "Messen", "Montage"]:
    current_directory = os.path.dirname(os.path.abspath(__file__))
    process_folder = os.path.join(current_directory, '..', 'Werk', 'Prozesse', process)
    file_path = os.path.join(process_folder, f'{process}_HistLog.csv')

    dictionary = {}
    for column in list:
        dictionary[column] = []

    print(dictionary)
    ds_df = pd.DataFrame(dictionary)

    print(ds_df)
    ds_df.to_csv(file_path, index=False)
