# Main program where important Inventory classes and functions are defined
# Also where the program itself runs the inventory cases for events

import os
import pandas as pd
from calculate_inventory_kpis import *

# Reading the dictionary which connects the lanes, target lanes and identifies the inventory/processes
FabrikVerbindung = pd.read_excel("FabrikVerbindung.xlsx", index_col=0)


# Class for box description (unused)
class Boxes:
    def __init__(self, lane_address, ID):
        self.lane = Lane(lane_address)
        self.box_capacity = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane_address,
                                                 "box_capacity"].iloc[0]
        self.variant = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane_address,
                                            "variant"].iloc[0]
        self.ID = ID


# Class for lane description
class Lane:
    # Class for handling all the Lane informations and functions.
    # There 3 important sections: 
    #   First is saving all the lane informations such as variants, lane address, and paths to navigate.
    #   Second is to deal with both put and pick event manipulating the current information.
    #   Third is to basically save all the alterations and calculate the metrics.
    # Other important details of this code are that great part of the information is obtained by the Fabrikverbindung excel.
    #   This occurs because the only information available is the lane address, timestamp and event type.
    #       The others such as IDs (carriers, lanes, etc) are not really reliable or documented in Benny's code
    #       and there are missing RFIDs in a lot of carriers to track every movement.
    #       The system would be reliable as soon as all the sensors worked.
    #       For implementing the IDs from Neoception this would require to enter the information into the class 
    #       In which this info could be obtained after filtering it in datenverarbeitung_main by the kafka.logs
    #       Other option would be getting the sensor data directly from the main controller (but nobody gave us access or really know where it is)
    # Other important functions is read_or_create where it creates the basics dataframes structures
    #   Werk databank is where it would store all the box IDs and timestamps, however I could not come to a good data structure and reliable source of info
    #   so this would require improvements in case of further works in the program
    #   Currently the most inventory that a box is actually tracked is 3 (i.e. Central warehouse,SM Lieferant and Montage)
    #   if sensors for waschen or supermarkets for the production part are implemented, the Werk DB would need alteration such as the starting lanes
    #   for initializing the IDs in the Fabrik.
    #   The ID system itself would be useless if all the RFIDs worked and if the IDs itself were decipherable 
    #       (there is no dictionary for searching info according to one ID)       
    # For future works, this class can be divided between small functions and classes to better organization
    # and comprehension.
    def __init__(self, lane, date, timestamp, event_type):
        # Initializing the class with it's informations
        self.lane_address = lane
        self.event_type = event_type
        self.timestamp = timestamp
        self.date = date
        self.capacity = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "capacity"].iloc[0]
        self.inventar_path = ""
        self.lane_path = ""
        self.boxes_array = []
        self.box_capacity = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "box_capacity"].iloc[0]
        self.variant = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "variant"].iloc[0]
        # For posterity
        self.df = None

        # Finding the specific Inventar and Lane
        self.inventar_name = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "inventar"].iloc[0]
        self.lane_name = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "lane_inventar"].iloc[0]

        # Find folder and return its path
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        werk_folder_path = os.path.join(self.current_dir, "..", "Werk")
        inventar_folder_path = os.path.join(self.current_dir, "..", "Werk", "Inventar")

        self.inventar_path = os.path.join(inventar_folder_path, f"{self.inventar_name}")
        self.lane_path = os.path.join(self.inventar_path, f"{self.lane_name}")

        inventar_csv_name = f'{self.inventar_name}' + '_DS.csv'
        lane_csv_name = f'{self.lane_name}'+'_DS.csv'
        
        self.inventar_csv = os.path.join(self.inventar_path, inventar_csv_name)
        self.lane_csv = os.path.join(self.lane_path, lane_csv_name)
        self.werk_path = os.path.join(werk_folder_path, "Werk_DS.csv")

        self.lane_DB = os.path.join(self.lane_path, f'{self.lane_name}'+'_DB.csv')
        self.hist_csv = os.path.join(self.lane_path, f'{self.lane_name}'+'_HistLog.csv')
        self.werk_DB = os.path.join(werk_folder_path, 'Werk'+'_DB.csv')
        self.inventar_kpi_df_db = os.path.join(self.inventar_path,f'{self.inventar_name}'+'_kpi_DB.csv')


    def read_or_create(self):
        # Function to read or creating a new file for:
        # Lane Databank, Werk Databank, Historical lane csv modell
        # Obs. Werk Databank is really poor handled, right now the data structure is only works for maximum 3 different invetories 
        # and doesn't take account for which inventory it would be.
        # For further works, it would be interesting to rename the timestamps and add a collumn with all the lanes that the box with that specif ID went
        # with the path that the box made in the Fabrik it would need different ways but more robust to calculate metrics
        # With more sensors or more lanes, the Werk DB could also take account for the processes lanes (waschen, fraesen, etc) 
        # and it would need more timestamps collumns or specific only for that
        try:
            df_DB_lane = pd.read_csv(self.lane_DB)
        except:
            # Structure for the Lane Databank
            df_DB_lane = pd.DataFrame(columns=["Besetzt", 'ID', 'Date', 'Timestamp'])
        try:
            df_DB_werk = pd.read_csv(self.werk_DB)
        except:
            # Structure for the Fabrik Databank
            df_DB_werk = pd.DataFrame(columns=['ID', "Besetzt", 'erste Linie', 'letzte Linie',
                                               'date1in', 't1in', 'date1out', 't1out',
                                               'date2in', 't2in', 'date2out', 't2out',
                                               'date3in', 't3in', 'date3out', 't3out'])
        try:
            df_Hist_lane = pd.read_csv(self.hist_csv)
        except:
            df_Hist_lane = pd.DataFrame(columns=["Besetzt", 'ID', 'Date_in', 'Timestamp_in',
                                                 'Date_out', 'Timestamp_out'])
        return df_DB_lane, df_DB_werk, df_Hist_lane
    
    def create_ID(self, db_werk):
        # Create a numerical ID for each box that is initialized in the Fabrik
        # This creation only happens in the starting lanes, but can also be created in other lanes by calling this function
        #   However this would not be taked account in some metrics (needs to be more robust) 
        if db_werk.empty:
            return 1
        else:
            last_id = db_werk['ID'].max()
            return last_id+1

    def get_ID_array(self, df):
        # Unused function
        # first idea was to store the information in a class
        # but the info wouldn't be saved for other runs
        self.df = df
        filtered_df = df[df["Besetzt"] == True]
        self.boxes_array = filtered_df['ID'].tolist()
        return self.boxes_array

    def put_event(self):
        # This function is one of the main functions of the code and could be further divided into smaller parts
        # There are 2 cases for a box being putted in a lane:
        #   First case - Is the starting lane of the fabrik (either the central warehouse or the lanes for production)
        #       This would mean that it needs to create and ID and register the information in the Lane Databank, Historical lane and Werk DB
        #   Second case - Is in the middle of the production line of the Fabrik, in that case some more steps happen
        #       If the box was inserted here, this means that this box came from somewhere, so the first step is to find where it came from,
        #       for that it uses the info in Fabrikverbindung excel to find the original lane and navigate into the folder structure and find the Databanks
        #           This could be further improved by just generating a databank with all the paths infos to optimize the code
        #       after accessing the original lane file, it copies the information (ID) and adds it to the lane DB where it was just inserted
        #       this info also gets to be added into the Werk DB by searching for the ID it just got and adding a new timestamp in 
        #       To end, it removes the the the information from the original lane Databank where it was written as besetzt == False
        #           This is a simulation of a requests system, after a box is picked from a lane, it is not automatically removed from the lane
        #           the besetzt just turns into False and wait until it is putted into the next lane so that it can save the ID and the FIFO modell works        #
        df_DB_lane, df_DB_werk, df_Hist_lane = self.read_or_create()
        # WHICH LANE DOES IT BEGIN 
        # NEEDS TO CHANGE ACCORDINGLY IN HOW THE FABRIK IS WORKING
        # If it's the starting point of the fabrik
        Start_lanes = ['S001.M007.01.01', 'S001.M007.01.02', 'S001.M007.01.03', 'S001.M007.01.04',
                       'S001.M007.02.01', 'S001.M007.02.02', 'S001.M007.02.03', 'S001.M007.02.04',
                       'S001.M003.02.01', 'S001.M003.02.02', 'S001.M003.02.03']
        # , 'S001.M003.02.03'
        if self.lane_address in Start_lanes:
            print('Put event in the starting lanes')
            ID = self.create_ID(df_DB_werk)
            # Adding the ID to the Databank from the lane
            new_line = [{"Besetzt": True, 'ID': ID, 'Date': self.date, 'Timestamp': self.timestamp}]
            df_DB_lane = pd.concat([df_DB_lane, pd.DataFrame(new_line)], ignore_index=True)
            # Adding the ID to the Hist log
            new_line_hist = [{"Besetzt": True, 'ID': ID, 'Date_in': self.date, 'Timestamp_in': self.timestamp,
                              'Date_out': None, 'Timestamp_out': None}]
            df_Hist_lane = pd.concat([df_Hist_lane, pd.DataFrame(new_line_hist)], ignore_index=True)
            # Adding the ID to the Databank from the Fabrik
            if ID in df_DB_werk['ID'].values:
                linha_id = df_DB_werk[df_DB_werk['ID'] == ID]
                empty_column = linha_id.columns[2:][linha_id.iloc[:, 2:].isna().all(axis=0)][:2]
                if not empty_column.empty:
                    df_DB_werk.loc[df_DB_werk['ID'] == ID, empty_column[0]] = self.date  # First slot with None as value
                    df_DB_werk.loc[df_DB_werk['ID'] == ID, empty_column[1]] = self.timestamp  # Second slot with None as value
                df_DB_werk.loc[df_DB_werk['ID'] == ID, df_DB_werk.columns[1]] = True  # Besetz
                df_DB_werk.loc[df_DB_werk['ID'] == ID, df_DB_werk.columns[3]] = self.lane_address  # letzte lane
            else:  # In case itś the very first ID on Fabrik Databank
                nova_linha = {'ID': ID, "Besetzt": True, 'erste Linie': self.lane_address,
                              'letzte Linie': self.lane_address, 'date1in': self.date, 't1in': self.timestamp}
                new_row = pd.DataFrame([nova_linha])  # Create a DataFrame from nova_linha
                df_DB_werk = pd.concat([df_DB_werk, new_row], ignore_index=True)
                # Fill the rest of the columns of tin and tout with None
                colunas_restantes = df_DB_werk.columns[6:]  # Exclui 'ID', 't1in' e 't1out'
                df_DB_werk.loc[df_DB_werk['ID'] == ID, colunas_restantes] = None
        # If it's not a lane which starts the production line
        # The information should only be copied from the lane before
        else:
            print('Put event in mid of production line')
            # Searching for the box ID in the original lane accordding to it's path (in DatenVerbindung)
            try:
                for target_list in FabrikVerbindung["target_lane_address"]:
                    if self.lane_address in f'{target_list}':
                        lane_original = FabrikVerbindung.loc[FabrikVerbindung["target_lane_address"] == target_list,
                                                             "lane_address"].iloc[0]
                inventar_original_name = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane_original,
                                                              "inventar"].iloc[0]
                lane_original_name = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane_original,
                                                          "lane_inventar"].iloc[0]
                lane_csv_name = f'{lane_original_name}'+'_DB.csv'
                lane_original_path = os.path.join(self.current_dir, "..", "Werk", "Inventar",
                                                  f'{inventar_original_name}', f'{lane_original_name}',
                                                  lane_csv_name)
                df_original = pd.read_csv(lane_original_path)
                false_besetz_line = df_original[df_original["Besetzt"] == False]
                ID = false_besetz_line["ID"].iloc[0]
                # Adding the ID to the Databank from the lane
                new_line = [{"Besetzt": True, 'ID': ID, 'Date': self.date, 'Timestamp': self.timestamp}]
                df_DB_lane = pd.concat([df_DB_lane, pd.DataFrame(new_line)], ignore_index=True)
                # Adding the ID to the Hist log
                new_line_hist = [{"Besetzt": True, 'ID': ID, 'Date_in': self.date, 'Timestamp_in': self.timestamp, 'Date_out': None, 'Timestamp_out': None}]
                df_Hist_lane = pd.concat([df_Hist_lane, pd.DataFrame(new_line_hist)], ignore_index=True)
                # Adding the ID to the Databank from the Fabrik
                if ID in df_DB_werk['ID'].values:
                    linha_id = df_DB_werk[df_DB_werk['ID'] == ID]
                    empty_column = linha_id.columns[2:][linha_id.iloc[:, 2:].isna().all(axis=0)][:2]
                    if not empty_column.empty:
                        df_DB_werk.loc[df_DB_werk['ID'] == ID, empty_column[0]] = self.date  # First slot with None as value
                        df_DB_werk.loc[df_DB_werk['ID'] == ID, empty_column[1]] = self.timestamp  # Second slot with None as value
                    df_DB_werk.loc[df_DB_werk['ID'] == ID, df_DB_werk.columns[1]] = True  # Besetz
                    df_DB_werk.loc[df_DB_werk['ID'] == ID, df_DB_werk.columns[3]] = self.lane_address  # letzte lane
            except:
                print('Error, the ID should already exist, this might break the databank')
                ID = self.create_ID(df_DB_werk)
                # Adding the ID to the Databank from the lane
                new_line = [{"Besetzt": True, 'ID': ID, 'Date': self.date, 'Timestamp': self.timestamp}]
                df_DB_lane = pd.concat([df_DB_lane, pd.DataFrame(new_line)], ignore_index=True)
                # Adding the ID to the Hist log
                new_line_hist = [{"Besetzt": True, 'ID': ID, 'Date_in': self.date, 'Timestamp_in': self.timestamp, 'Date_out': None, 'Timestamp_out': None}]
                df_Hist_lane = pd.concat([df_Hist_lane, pd.DataFrame(new_line_hist)], ignore_index=True)
                # Adding the ID to the Databank from the Fabrik
                if ID in df_DB_werk['ID'].values:
                    linha_id = df_DB_werk[df_DB_werk['ID'] == ID]
                    empty_column = linha_id.columns[2:][linha_id.iloc[:, 2:].isna().all(axis=0)][:2]
                    if not empty_column.empty:
                        df_DB_werk.loc[
                            df_DB_werk['ID'] == ID, empty_column[0]] = self.date  # First slot with None as value
                        df_DB_werk.loc[
                            df_DB_werk['ID'] == ID, empty_column[1]] = self.timestamp  # Second slot with None as value
                    df_DB_werk.loc[df_DB_werk['ID'] == ID, df_DB_werk.columns[1]] = True  # Besetz
                    df_DB_werk.loc[df_DB_werk['ID'] == ID, df_DB_werk.columns[3]] = self.lane_address  # letzte lane
            # Removing the data where the besetz is false after copying the info to the next lane
            df_original = df_original[df_original['ID'] != ID]
            df_original.to_csv(lane_original_path, index=False)
        # Box = Boxes(self.lane_address,ID)
        # Saving Databanks
        print(self.lane_DB)
        print(self.werk_DB)
        df_DB_lane.to_csv(self.lane_DB, index=False)
        df_DB_werk.to_csv(self.werk_DB, index=False)
        df_Hist_lane.to_csv(self.hist_csv, index=False)

    def pick_event(self):
        # This is the other main function from this script and could also be further divided into small functions
        # What happens here is much simpler when compared to the put event
        # Basically the script only turns the Besetzt from True to False in the Lane Databank and in the Historical info in the lane
        # It also saves the timestamp out in the Historical lane and in Werk DB
        # In case it's one of the ending lanes, the ID with besetz false gets removed from the lane databank
        # as it won't have a next lane where is putted in.
        df_DB_lane, df_DB_werk, df_Hist_lane = self.read_or_create()
        # Adding the pick event at the lane DB
        print(f"\n\nDEBUGGING: PRINTING DF_DB_LANE for {self.lane_name}")
        print(df_DB_lane)
        print("\n")
        primeiro_registro = df_DB_lane[df_DB_lane["Besetzt"] == True].iloc[0]
        ID = primeiro_registro['ID']
        index_of_primeiro_registro = primeiro_registro.name
        df_DB_lane.at[index_of_primeiro_registro, 'Besetzt'] = False
        # df_DB_lane.at[index_of_primeiro_registro, 'Date'] 
        # Adding the pick event on Historical Log
        primeiro_registro_hist = df_Hist_lane[df_Hist_lane["Besetzt"] == True].iloc[0]
        ID = primeiro_registro_hist['ID']
        index_of_primeiro_registro_hist = primeiro_registro_hist.name
        df_Hist_lane.at[index_of_primeiro_registro_hist, 'Besetzt'] = False
        df_Hist_lane.at[index_of_primeiro_registro_hist, 'Date_out'] = self.date
        df_Hist_lane.at[index_of_primeiro_registro_hist, 'Timestamp_out'] = self.timestamp
        # Changing things for werk
        if ID in df_DB_werk['ID'].values:
            linha_id = df_DB_werk[df_DB_werk['ID'] == ID]
            empty_column = linha_id.columns[2:][linha_id.iloc[:, 2:].isna().all(axis=0)][:2]
            if not empty_column.empty:  # Adding date and time out and changing the Besetz to false
                df_DB_werk.loc[df_DB_werk['ID'] == ID, empty_column[0]] = self.date  # First slot with None as value
                df_DB_werk.loc[df_DB_werk['ID'] == ID, empty_column[1]] = self.timestamp  # Second slot with None as value
            df_DB_werk.loc[df_DB_werk['ID'] == ID, df_DB_werk.columns[1]] = False  # Besetz
        Ending_lanes = ['S001.M006.01.01', 'S001.M006.01.02', 'S001.M006.01.03', 'S001.M006.01.04',
                        'S001.M006.01.05', 'S001.M006.02.01', 'S001.M006.02.02', 'S001.M006.02.03',
                        'S001.M006.02.04', 'S001.M006.02.05']
        # FK 1 - 8 could be added
        if self.lane_address in Ending_lanes:
            # IF IT'S THE LAST LANE FROM THE PRODUCTION LINE, REMOVE THE ID FROM THE LANE
            df_DB_lane = df_DB_lane[df_DB_lane['ID'] != ID]
        df_DB_lane.to_csv(self.lane_DB, index=False)
        df_DB_werk.to_csv(self.werk_DB, index=False)
        df_Hist_lane.to_csv(self.hist_csv, index=False)

    def save_dashboard_format(self):
        # This is the last main fucntion of the code where the Kennzahlen (metrics) are calculated 
        # and both model and metrics are saved in the dashboard format
        # There are 3 important files for dashboard: Lane, Inventar and Werk
        # In lane there are 2 different data structures, first the metrics for the lane and after the lane modell with some info
        #   Important to notice that kapazitaet, bestandsmenge and losgrosse in the modell is for each box and not for the lane
        # In Inventar file is basically the metrics for all the lanes (some are just a sum and other are averaged), after that the modell for each lane
        # In Werk file it is only some metrics from all the lanes

        # Read csv files from Werk, Inventar and Lane
        df_W = pd.read_csv(self.werk_path, encoding="cp1252")
        df_I = pd.read_csv(self.inventar_csv, encoding="cp1252")
        df_L = pd.read_csv(self.lane_csv, encoding="cp1252")
        df_DB_lane, df_DB_werk, df_Hist_lane = self.read_or_create()

        # Updating the csv from the lane first
        #
        # Find the position in which to separate the Dataframes
        separator_idx = df_L[df_L['Bestandsmenge'] == f'{self.lane_name}'].index[0]

        # Dividing the Data frame in 2
        df_kpi = df_L.iloc[:separator_idx]
        df_DS = df_L.iloc[separator_idx + 1:]  # Jump 2 lines after separator

        # Redefining indexes
        df_DS = df_DS.reset_index(drop=True)
        df_DS.columns = df_L.iloc[separator_idx]

        # Redefining values
        # Really dumb way, but easiest
        df_DS['Besetzt'] = 0
        df_DS['Time In'] = '-'
        df_DS['Waiting Time'] = '-'
        df_DS['Bestandsmenge'] = '-'
        df_DS['Kapazitaet'] = '-'
        df_DS['Losgroesse'] = '-'
        df_DS['Lead Time'] = '-'

        condicao = df_DB_lane['Besetzt'] == True
        linhas_a_atualizar = condicao.index[condicao].tolist()  
        # for every besetzt True, substitute the info for the box
        for truelinha in linhas_a_atualizar:
            linha = linhas_a_atualizar.index(truelinha)
            print("\nentrou aqui")
            df_DS.loc[linha, 'Besetzt'] = 1
            df_DS.loc[linha, 'Time In'] = df_DB_lane.loc[linha, 'Timestamp']
            # Parse the input date string
            input_date = datetime.strptime(df_DB_lane.loc[linha, 'Date'], "%d/%b/%Y")
            # Format the date into the "DD.MM.YYYY" format
            output_date_string = input_date.strftime("%d.%m.%Y")
            df_DS.loc[linha, 'Waiting Time'] = output_date_string
            # df_DS.loc[linha, 'Bestandmenge'] = len(linhas_a_atualizar) 
            df_DS.loc[linha, 'Bestandsmenge'] = self.box_capacity
            # df_DS.loc[linha, 'Kapazitaet'] = self.capacity
            df_DS.loc[linha, 'Kapazitaet'] = self.box_capacity
            df_DS.loc[linha, 'Losgroesse'] = self.box_capacity
            # Lead time for each box not needed, but gonna keep it here for purpose of not ruining the csv format
            # df_DS.loc[linha, 'Lead Time'] =
             
        # Updating the csv from the KPIs
        # 
        # Using functions from calculate_inventory_kpis
        bestandsmenge = calculate_Bestandsmenge(df_DB_lane, self.box_capacity)
        kapazitaet = calculate_Kapazitaet(self.capacity, self.box_capacity)
        lagernutzungsgrad = calculate_Lagernutzungsgrad(bestandsmenge, kapazitaet)
        bestandsgenauigkeit = calculate_Bestandsgenauigkeit()
        durchschnittliche_wartezeit = calculate_Durchschnittliche_Wartezeit(df_Hist_lane)
        lagerumschlagsrate = calculate_Lagerumschlagsrate(df_Hist_lane, self.capacity)
        reichweite = calculate_Reichweite(lagerumschlagsrate, lagernutzungsgrad)
        wiederbeschaffungszeit = calculate_Wiederbeschaffungszeit(df_DB_werk, self.lane_path, self.lane_address)
        df_kpi['Bestandsmenge'] = [bestandsmenge]
        df_kpi['Kapazitaet'] = [kapazitaet]
        df_kpi['Lagernutzungsgrad'] = [lagernutzungsgrad]
        df_kpi['Bestandsgenauigkeit'] = [bestandsgenauigkeit]
        df_kpi['Durchschnittliche Wartezeit'] = [durchschnittliche_wartezeit]
        df_kpi['Lagerumschlagsrate'] = [lagerumschlagsrate]
        df_kpi['Reichweite'] = [reichweite]
        df_kpi['Wiederbeschaffungszeit'] = [wiederbeschaffungszeit]

        # Saving the csv from the lane
        #
        # Uniting both KPIs and DS csv into one
        path_kpi = os.path.join(self.lane_path, f"kpi_{self.lane_name}.csv")
        path_DS = os.path.join(self.lane_path, f"DS_{self.lane_name}.csv")
        df_kpi.to_csv(path_kpi, index=False)
        df_DS.to_csv(path_DS, index=False)

        # Caminho para o arquivo de saída onde os dois arquivos serão mesclados
        arquivo_saida_lane = self.lane_csv

        # Saving file into the dashboard format
        # Really dumb way of working as it contrariates the structure format of a Data Frame
        try:
            print("Saving Lane.csv with digital shadow")
            # Abrir o primeiro arquivo CSV e ler seu conteúdo
            with open(path_kpi, "r") as file1:
                conteudo1 = file1.read()

            print(conteudo1)

            # Abrir o segundo arquivo CSV e ler seu conteúdo
            with open(path_DS, "r") as file2:
                conteudo2 = file2.read()

            print(conteudo2)

            # Combinar o conteúdo dos dois arquivos
            conteudo_combinado = conteudo1 + conteudo2

            print(conteudo_combinado)

            # Escrever o conteúdo combinado em um novo arquivo CSV
            with open(arquivo_saida_lane, "w") as output_file:
                output_file.write(conteudo_combinado)
        except:
            print('Could not unite the files')

        # Updating the csv from the Inventar
        #
        #  Updating the Inventar lane DS
        #  Encontre o índice onde a primeira coluna começa com a lane name
        ld1_index = df_I[df_I['Bestandsmenge'] == f'{self.lane_name}'].index[0]
        df_I.iloc[ld1_index+1:ld1_index+len(df_DS)+1] = df_DS.values

        # Change the first row of each lane to show Bestandsmenge/Kapazität (dumb request from the dashboard team)
        df_I.iloc[ld1_index+1]["Lagerumschlagsrate"] = kapazitaet
        df_I.iloc[ld1_index+1]["Durchschnittliche Wartezeit"] = bestandsmenge

        # Updating the Inventar KPIs
        if not os.path.exists(self.inventar_kpi_df_db):
            df_inventar_kpi_db = pd.DataFrame(columns=['Lane', 'Bestandsmenge', 'Kapazitaet', 'Lagernutzungsgrad',
                                                       'Bestandsgenauigkeit', 'Durchschnittliche Wartezeit',
                                                       'Lagerumschlagsrate', 'Reichweite', 'Wiederbeschaffungszeit'])
        else:
            df_inventar_kpi_db = pd.read_csv(self.inventar_kpi_df_db)
        
        data_inventar = {
            'Lane': [self.lane_name],
            'Bestandsmenge': [bestandsmenge],
            'Kapazitaet': [kapazitaet],
            'Lagernutzungsgrad': [lagernutzungsgrad],
            'Bestandsgenauigkeit': [bestandsgenauigkeit],
            'Durchschnittliche Wartezeit': [durchschnittliche_wartezeit],
            'Lagerumschlagsrate': [lagerumschlagsrate],
            'Reichweite': [reichweite],
            'Wiederbeschaffungszeit': [wiederbeschaffungszeit]
        }
        df_lane_kpi_db = pd.DataFrame(data_inventar)

        df_inventar_kpi_db.loc[df_inventar_kpi_db['Lane'] == self.lane_name] = df_lane_kpi_db.values

        df_inventar_kpi_db.to_csv(self.inventar_kpi_df_db, index=False)

        somas = df_inventar_kpi_db.drop(columns=['Lane']).sum()
        medias = df_inventar_kpi_db.drop(columns=['Lane']).mean()
        print("Somas:")
        print(somas)
        print("Medias:")
        print(medias)
        df_I.loc[0, 'Bestandsmenge'] = somas['Bestandsmenge']
        df_I.loc[0, 'Kapazitaet'] = somas['Kapazitaet']
        df_I.loc[0, 'Lagernutzungsgrad'] = round(medias['Lagernutzungsgrad'])
        # df_I.loc[0, 'Bestandsgenauigkeit'] = medias['Bestandsgenauigkeit']
        df_I.loc[0, 'Bestandsgenauigkeit'] = 100 #%
        # Should be calculating but for any reason it gives different values 
        # The function gives only 100%
        df_I.loc[0, 'Durchschnittliche Wartezeit'] = medias['Durchschnittliche Wartezeit']
        df_I.loc[0, 'Lagerumschlagsrate'] = somas['Lagerumschlagsrate']
        df_I.loc[0, 'Reichweite'] = somas['Reichweite']
        df_I.loc[0, 'Wiederbeschaffungszeit'] = somas['Wiederbeschaffungszeit']

        # Substitua os três primeiros valores das linhas "Lager_Fertigung" e "SM_Fertigung"
        #df_W.loc[df_W['Werk'] == f'{self.inventar_name}', ['Schichtlaenge', 'Pausen', 'SF Besprechung']] = \
        #    [medias['Lagernutzungsgrad'], medias['Bestandsgenauigkeit'], medias['Durchschnittliche Wartezeit']]
        df_W.loc[df_W['Werk'] == f'{self.inventar_name}', ['Schichtlaenge', 'Pausen', 'SF Besprechung']] = \
            [medias['Lagernutzungsgrad'], 100, medias['Durchschnittliche Wartezeit']]

        # Saving files back
        df_W.to_csv(self.werk_path, index=False, encoding="cp1252")
        df_I.to_csv(self.inventar_csv, index=False, encoding="cp1252")
        # df_L.to_csv(self.lane_csv, index=False,encoding = "cp1252")












# # Class for the Digital shadow of the Inventar
# class InventarDataDistribution:
#     def __init__(self,lane_address, date, timestamp,event_type):

# if __name__ == "__main__":
#     date, lane, timestamp, event_type = read_kafka_lane_time_event(csv_file_path)
#     InventarDataDistribution(Lane(lane), date, timestamp, event_type)
   
