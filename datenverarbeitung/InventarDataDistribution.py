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
    # Instancia com o objeto lane, as quais contém caixas indentadas 
    # contém funções de manipulação pra que execute o sistema FIFO
    # Não precisa se preocupar com o tamanho máximo, pois no databank de cada lane (que é o operacional)
    # ele vai ser limitado de acordo com os puts
    # datank da lane é completamente diferente do _DS.csv pra ser mostrado pro Brennan
    # Não podem serem os mesmos pois vão precisar de informações diferentes
    # https://chat.openai.com/share/2b5104e9-3d09-436b-9ce2-e18a33491666 concatenar csvs
    # todas as funções vão precisar serem calculadas com a caixa como parametro

    # funcao pra só retirar uma id do DB de uma lane quando receber o put na outra
    # o put na lane 2 copia o ID e as infos da caixa q já saiu mas n foi apagado do DB da lane 1
    # depois disso o ID da box é apagado da lane 1 e assim por conseguinte até a última instancia
    def __init__(self, lane, date, timestamp, event_type):
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
        self.werk_path = os.path.join(werk_folder_path, "Werk_DS.csv ")

        self.lane_DB = os.path.join(self.lane_path, f'{self.lane_name}'+'_DB.csv')
        self.hist_csv = os.path.join(self.lane_path, f'{self.lane_name}'+'_HistLog.csv')
        self.werk_DB = os.path.join(werk_folder_path, 'Werk'+'_DB.csv')
        self.inventar_kpi_df_db = os.path.join(self.inventar_path,f'{self.inventar_name}'+'_kpi_DB.csv')


    def read_or_create(self):
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
            df_Hist_lane = pd.DataFrame(columns=["Besetzt", 'ID', 'Date_in', 'Timestamp_in','Date_out','Timestamp_out'])
        return df_DB_lane, df_DB_werk, df_Hist_lane
    
    def create_ID(self, db_werk):
        # CRIAR UM ID NUMERICO PRA CADA CAIXA
        # OU SEJA, ESTÁ INSTANCIANDO UM OBJETO COM REFERENCIA EM UMA LANE ESPECIFICA
        # SÓ CRIA UM ID CASO SEJAM LANES ESPECIFICAS (INICIO DA LINHA DE PRODUCAO)
        # ESSE ID TEM PARAMETRO DA LANE
        if db_werk.empty:
            return 1
        else:
            last_id = db_werk['ID'].max()
            return last_id+1

    def get_ID_array(self, df):
        self.df = df
        filtered_df = df[df["Besetzt"] == True]
        self.boxes_array = filtered_df['ID'].tolist()
        return self.boxes_array

    def put_event(self):
        df_DB_lane, df_DB_werk, df_Hist_lane = self.read_or_create()
        # WHICH LANE DOES IT BEGIN 
        # NEEDS TO CHANGE ACCORDINGLY IN HOW THE FABRIK IS WORKING
        # If it's the starting point of the fabrik
        Start_lanes = ['S001.M007.01.01', 'S001.M007.01.02', 'S001.M007.01.03', 'S001.M007.01.04',
                       'S001.M007.02.01', 'S001.M007.02.02', 'S001.M007.02.03', 'S001.M007.02.04',
                       'S001.M003.02.01', 'S001.M003.02.02', 'S001.M003.02.03']
        if self.lane_address in Start_lanes:
            print('entrou no start fabrik')
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
            print('entrou no caso de meio da producao')
            # Searching for the box ID in the original lane accordding to it's path (in DatenVerbindung)
            try:
                for target_list in FabrikVerbindung["target_lane_address"]:
                    if self.lane_address in f'{target_list}':
                        lane_original = FabrikVerbindung.loc[FabrikVerbindung["target_lane_address"] == target_list,"lane_address"].iloc[0]
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
                new_line = [{"Besetzt": True, 'ID': ID, 'Date': self.date, 'Timestamp_in': self.timestamp}]
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
        df_Hist_lane.to_csv(self.hist_csv,index = False)

    def pick_event(self):
        df_DB_lane, df_DB_werk, df_Hist_lane = self.read_or_create()
        # Adding the pick event at the lane DB
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
            df_DB_werk.loc[df_DB_werk['ID'] == ID, df_DB_werk.columns[1]] = False  #Besetz
        Ending_lanes = ['S001.M006.01.01', 'S001.M006.01.02', 'S001.M006.01.03', 'S001.M006.01.04',
                        'S001.M006.01.05', 'S001.M006.02.01', 'S001.M006.02.02', 'S001.M006.02.03',
                        'S001.M006.02.04', 'S001.M006.02.05']
        if self.lane_address in Ending_lanes:
            # IF IT'S THE LAST LANE FROM THE PRODUCTION LINE, REMOVE THE ID FROM THE LANE
            df_DB_lane = df_DB_lane[df_DB_lane['ID'] != ID]
        df_DB_lane.to_csv(self.lane_DB, index=False)
        df_DB_werk.to_csv(self.werk_DB, index=False)
        df_Hist_lane.to_csv(self.hist_csv,index = False)

    def save_dashboard_format(self):
        # Read csv files from Werk, Inventar and Lane
        df_W = pd.read_csv(self.werk_path,encoding = "cp1252")
        df_I = pd.read_csv(self.inventar_csv,encoding = "cp1252")
        df_L = pd.read_csv(self.lane_csv,encoding = "cp1252")
        df_DB_lane, df_DB_werk,df_Hist_lane = self.read_or_create()

        # Updating the csv from the lane first
        #
        # Find the position in which to separate the Dataframes
        separator_idx = df_L[df_L['Bestandsmenge'] == f'{self.lane_name}'].index[0]

        # Dividing the Data frame in 2
        df_kpi = df_L.iloc[:separator_idx]
        df_DS = df_L.iloc[separator_idx +1:]  # Jump 2 lines after separator

        # Redefining indexes
        df_DS = df_DS.reset_index(drop=True)
        df_DS.columns = df_L.iloc[separator_idx]

        # Redefining values
        # Really dumb way, but easiest
        df_DS['Besetzt'] = 0
        df_DS['Time In'] = '-'
        df_DS['Waiting Time'] = '-'
        df_DS['Bestandsmenge'] = '-'
        df_DS['Kapazität'] = '-'
        df_DS['Losgröße'] = '-'
        df_DS['Lead Time'] = '-'

        condicao = df_DB_lane['Besetzt'] == True
        linhas_a_atualizar = condicao.index[condicao].tolist()  # Encontre os índices das linhas com Besetzt True
        # Substitua os valores de 'Name' e 'Age' em df1 nas linhas correspondentes
        for linha in linhas_a_atualizar:
            df_DS.loc[linha, 'Besetzt'] = 1
            df_DS.loc[linha, 'Time In'] = df_DB_lane.loc[linha,'Timestamp']
            df_DS.loc[linha, 'Waiting Time'] = df_DB_lane.loc[linha,'Date']
            # df_DS.loc[linha, 'Bestandmenge'] = len(linhas_a_atualizar) 
            df_DS.loc[linha, 'Bestandsmenge'] = self.box_capacity
            # df_DS.loc[linha, 'Kapazität'] = self.capacity
            df_DS.loc[linha, 'Kapazität'] = self.box_capacity
            df_DS.loc[linha, 'Losgröße'] = self.box_capacity
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
        lagerumschlagsrate = calculate_Lagerumschlagsrate(df_Hist_lane,self.capacity)
        reichweite = calculate_Reichweite(lagerumschlagsrate, lagernutzungsgrad)
        wiederbeschaffungszeit = calculate_Wiederbeschaffungszeit(df_DB_werk,self.lane_path, self.lane_name)
        df_kpi['Bestandsmenge'] = [bestandsmenge]
        df_kpi['Kapazität'] = [kapazitaet]
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

        try:
            # Abrir o primeiro arquivo CSV e ler seu conteúdo
            with open(path_kpi, "r") as file1:
                conteudo1 = file1.read()

            # Abrir o segundo arquivo CSV e ler seu conteúdo
            with open(path_DS, "r") as file2:
                conteudo2 = file2.read()

            # Combinar o conteúdo dos dois arquivos
            conteudo_combinado = conteudo1 + "\n" + conteudo2

            # Escrever o conteúdo combinado em um novo arquivo CSV
            with open(arquivo_saida_lane, "w") as output_file:
                output_file.write(conteudo_combinado)
        except:
            print('não consegui juntar os arquivos')

        # Updating the csv from the Inventar
        #
        #  Updating the Inventar lane DS
        #  Encontre o índice onde a primeira coluna começa com a lane name
        ld1_index = df_I[df_I['Bestandsmenge'] == f'{self.lane_name}'].index[0]
        df_I.iloc[ld1_index+1:ld1_index+len(df_DS)+1] = df_DS.values

        # Updating the Inventar KPIs
        if not os.path.exists(self.inventar_kpi_df_db):
            df_inventar_kpi_db = pd.DataFrame(columns=['Lane', 'Bestandsmenge', 'Kapazität', 'Lagernutzungsgrad', 'Bestandsgenauigkeit', 'Durchschnittliche Wartezeit', 'Lagerumschlagsrate', 'Reichweite', 'Wiederbeschaffungszeit'])
        else:
            df_inventar_kpi_db = pd.read_csv(self.inventar_kpi_df_db)
        
        data_inventar = {
            'Lane': [self.lane_name],
            'Bestandsmenge': [bestandsmenge],
            'Kapazität': [kapazitaet],
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
        df_I.loc[0, 'Bestandsmenge'] = somas['Bestandsmenge']
        df_I.loc[0,'Kapazität'] = somas['Kapazität']
        df_I.loc[0,'Lagernutzungsgrad'] = medias['Lagernutzungsgrad']
        df_I.loc[0,'Bestandsgenauigkeit'] = medias['Bestandsgenauigkeit']
        df_I.loc[0,'Durchschnittliche Wartezeit'] = medias['Durchschnittliche Wartezeit']
        df_I.loc[0,'Lagerumschlagsrate'] = somas['Lagerumschlagsrate']
        df_I.loc[0,'Reichweite'] = somas['Reichweite']
        df_I.loc[0,'Wiederbeschaffungszeit'] = somas['Wiederbeschaffungszeit']

        # Substitua os três primeiros valores das linhas "Lager_Fertigung" e "SM_Fertigung"
        df_W.loc[df_W['Werk'] == f'{self.inventar_name}', ['Schichtlänge', 'Pausen', 'SF Besprechung']] = [medias['Lagernutzungsgrad'], medias['Bestandsgenauigkeit'], medias['Durchschnittliche Wartezeit']]


        # Saving files back
        df_W.to_csv(self.werk_path, index=False,encoding = "cp1252")
        df_I.to_csv(self.inventar_csv, index=False,encoding = "cp1252")
        df_L.to_csv(self.lane_csv, index=False,encoding = "cp1252")












# # Class for the Digital shadow of the Inventar
# class InventarDataDistribution:
#     def __init__(self,lane_address, date, timestamp,event_type):

# if __name__ == "__main__":
#     date, lane, timestamp, event_type = read_kafka_lane_time_event(csv_file_path)
#     InventarDataDistribution(Lane(lane), date, timestamp, event_type)
   