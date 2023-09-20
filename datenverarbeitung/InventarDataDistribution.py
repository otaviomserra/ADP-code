import os
import pandas as pd

# Reading the dictionary which connects the lanes, target lanes and identifies the inverntar/processes 
FabrikVerbindung = pd.read_excel("FabrikVerbindung.xlsx", index_col=0)

# Class for box description
class Box:
    def __init__(self,lane_address,ID):
        self.lane = Lane(lane_address)
        self.box_capacity = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane_address, "box_capacity"].iloc[0]
        self.variant = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane_address, "variant"].iloc[0]
        self.ID = ID

# Class for lane description
class Lane:
    # Instancia com o objeto lane, as quais contém caixas indentadas 
    # contém funções de manipulação pra que execute o sistema FIFO
    # Não precisa se preocupar com o tamanho máximo, pois no databank de cada lane (que é o operacional) ele vai ser limitado 
    #de acordo com os puts
    # datank da lane é completamente diferente do _DS.csv pra ser mostrado pro Brennan
    # Não podem serem os mesmos pois vão precisar de informações diferentes
    # https://chat.openai.com/share/2b5104e9-3d09-436b-9ce2-e18a33491666 concatenar csvs
    # todas as funções vão precisar serem calculadas com a caixa como parametro

    # funcao pra só retirar uma id do DB de uma lane quando receber o put na outra
    # o put na lane 2 copia o ID e as infos da caixa q já saiu mas n foi apagado do DB da lane 1
    # depois disso o ID da box é apagado da lane 1 e assim por conseguinte até a última instancia
    def __init__(self,lane, date, timestamp,event_type):
        self.lane_address = lane
        self.event_type = event_type
        self.timestamp = timestamp
        self.date = date
        self.capacitaty = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "capacity"].iloc[0]
        self.inventar_path = ""
        self.lane_path = ""
        self.boxes_array = []

        # Finding the specific Inventar and Lane
        self.inventar_name = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "inventar"].iloc[0]
        self.lane_name = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "lane_inventar"].iloc[0]

        # Find folder and return it's path
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        werk_folder_path = os.path.join(self.current_dir, "..", "Werk")
        inventar_folder_path = os.path.join(self.current_dir, "..", "Werk", "Inventar")

        self.inventar_path = os.path.join(inventar_folder_path,f"{self.inventar_name}")
        self.lane_path = os.path.join(inventar_folder_path,f"{self.lane_name}")
        self.werk_path = os.path.join(werk_folder_path,"Werk_DS.csv")
        
        inventar_csv_name = f'{self.inventar_name}' + '_DS.csv'
        lane_csv_name = f'{self.lane_name}'+'_DS.csv'
        
        self.inventar_csv = os.path.join(self.inventar_path,inventar_csv_name)
        self.lane_csv = os.path.join(self.lane_path, lane_csv_name)
        self.lane_DB = os.path.join(self.lane_path, f'{self.lane_name}'+'_DB.csv')
        self.werk_DB = os.path.join(werk_folder_path, f'{self.lane_name}'+'_DB.csv')
    

    def read_or_create(self):
        try:
            df_DB_lane = pd.read_csv(self.lane_DB)
        except:
            # Structure for the Lane Databank
            df_DB_lane = pd.DataFrame(columns=['Besetz', 'ID', 'Date', 'Timestamp'])
        try:
            df_DB_werk = pd.read_csv(self.werk_DB)
        except:
            # Structure for the Fabrik Databank
            df_DB_werk = pd.DataFrame(columns=['ID','Besetz','erste Linie','letzte Linie','date1in','t1in','date1out','t1out','date2in','t2in','date2out','t2out','date3in','t3in','date3out','t3out'])
        return df_DB_lane, df_DB_werk
    
    def create_ID(self,db_werk): 
        # CRIAR UM ID NUMERICO PRA CADA CAIXA
        # OU SEJA, ESTÁ INSTANCIANDO UM OBJETO COM REFERENCIA EM UMA LANE ESPECIFICA
        # SÓ CRIA UM ID CASO SEJAM LANES ESPECIFICAS (INICIO DA LINHA DE PRODUCAO)
        # ESSE ID TEM PARAMETRO DA LANE
        if db_werk.empty:
            return 1
        else:
            last_id = db_werk['ID'].max()
            return last_id+1

    def get_ID_array(self,df):
        self.df = df
        filtered_df = df[df['Besetz'] == True]
        self.boxes_array = filtered_df['ID'].tolist()
        return self.boxes_array

    def put_event(self):
        df_DB_lane, df_DB_werk = self.read_or_create()
        # WHICH LANE DOES IT BEGIN 
        # NEEDS TO CHANGE ACCORDINGLY IN HOW THE FABRIK IS WORKING
        # If it's the starting point of the fabrik
        if self.lane_address == '': 
            ID = self.create_ID(df_DB_werk)
            # Adding the ID to the Databank from the lane
            new_line = [{'Besetz':True, 'ID':ID, 'Date':self.date, 'Timestamp':self.timestamp}]
            df_DB_lane = pd.concat([df_DB_lane,pd.DataFrame(new_line)], ignore_index=True)
            # Adding the ID to the Databank from the Fabrik
            if ID in df_DB_werk['ID'].values:
                empty_column = df_DB_werk.columns[2:][df_DB_werk.loc[df_DB_werk['ID'] == ID, 2:].isnull().all(axis=0)]
                if not empty_column.empty:
                    df_DB_werk.loc[df_DB_werk['ID'] == ID, empty_column[0]] = self.date # First slot with None as value
                    df_DB_werk.loc[df_DB_werk['ID'] == ID, empty_column[1]] = self.timestamp # Second slot with None as value
                df_DB_werk.loc[df_DB_werk['ID'] == ID, df_DB_werk.columns[1]] = True #Besetz
                df_DB_werk.loc[df_DB_werk['ID'] == ID, df_DB_werk.columns[3]] = self.lane_address # latzte lane
            else: # In case itś the very first ID on Fabrik Databank
                nova_linha = {'ID': ID,'Besetz':True,'erste Linie':self.lane_address,'letzte Linie':self.lane_address,'date1in':self.date,'t1in':self.timestamp}
                df_DB_werk = df_DB_werk.append(nova_linha, ignore_index=True)
                
                # Fill the rest of the columns of tin and tout with None
                colunas_restantes = df_DB_werk.columns[6:]  # Exclui 'ID', 't1in' e 't1out'
                df_DB_werk.loc[df_DB_werk['ID'] == ID, colunas_restantes] = None
        # If it's not a lane which starts the production line
        # The information should only be copied from the lane before
        else:
            # Searching for the box ID in the original lane accordding to it's path (in DatenVerbindung)
            lane_original = FabrikVerbindung.loc[FabrikVerbindung["target_lane"] == self.lane_address, "lane_address"].iloc[0]
            inventar_original_name = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane_original, "inventar"].iloc[0]
            lane_original_name = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane_original, "lane_inventar"].iloc[0]
            lane_csv_name = f'{lane_original_name}'+'_DS.csv'
            lane_original_path = os.path.join(self.current_dir, "..", "Werk", "Inventar",f'{inventar_original_name}',f'{lane_original_name}',lane_csv_name)
            df_original = pd.read_csv(lane_original_path)
            false_besetz_line = df_original[df_original["Besetz"] == False]
            ID = false_besetz_line["ID"].iloc[0]
            # Adding the ID to the Databank from the lane
            new_line = [{'Besetz':True, 'ID':ID, 'Date':self.date, 'Timestamp_in':self.timestamp}]
            df_DB_lane = pd.concat([df_DB_lane,pd.DataFrame(new_line)], ignore_index=True)
            # Adding the ID to the Databank from the Fabrik
            if ID in df_DB_werk['ID'].values:
                empty_column = df_DB_werk.columns[2:][df_DB_werk.loc[df_DB_werk['ID'] == ID, 2:].isnull().all(axis=0)]
                if not empty_column.empty:
                    df_DB_werk.loc[df_DB_werk['ID'] == ID, empty_column[0]] = self.date # First slot with None as value
                    df_DB_werk.loc[df_DB_werk['ID'] == ID, empty_column[1]] = self.timestamp # Second slot with None as value
                df_DB_werk.loc[df_DB_werk['ID'] == ID, df_DB_werk.columns[1]] = True #Besetz
                df_DB_werk.loc[df_DB_werk['ID'] == ID, df_DB_werk.columns[3]] = self.lane_address # latzte lane
            else:
                print('Error, the ID should alredy exist, this might break the databank')
                quit
                nova_linha = {'ID': ID,'Besetz':True,'erste Linie':self.lane_address,'letzte Linie':self.lane_address,'date1in':self.date,'t1in':self.timestamp}
                df_DB_werk = df_DB_werk.append(nova_linha, ignore_index=True)
                
                # Fill the rest of the columns of tin and tout with None
                colunas_restantes = df_DB_werk.columns[6:]  # Exclui 'ID', 't1in' e 't1out'
                df_DB_werk.loc[df_DB_werk['ID'] == ID, colunas_restantes] = None
            # Removing the data where the besetz is false after copying the info to the next lane
            df_original = df_original[df_original['ID'] != ID]
        Box = Box(self.lane_address,ID)
        # Saving Databanks
        df_original.to_csv(lane_original_path, index=False)
        df_DB_lane.to_csv(self.lane_DB , index=False)
        df_DB_werk.to_csv(self.werk_DB, index=False)
        
    
    def pick_event(self):
        df_DB_lane, df_DB_werk = self.read_or_create()
        df_DB_lane.at[0, 'Besetz'] = False
        primeiro_registro = df_DB_lane[df_DB_lane['Besetz'] == False].iloc[0]
        ID = primeiro_registro['ID']
        if ID in df_DB_werk['ID'].values:
            empty_column = df_DB_werk.columns[2:][df_DB_werk.loc[df_DB_werk['ID'] == ID, 2:].isnull().all(axis=0)]
            if not empty_column.empty: # Adding date and time out and changing the Besetz to false
                df_DB_werk.loc[df_DB_werk['ID'] == ID, empty_column[0]] = self.date # First slot with None as value
                df_DB_werk.loc[df_DB_werk['ID'] == ID, empty_column[1]] = self.timestamp # Second slot with None as value
            df_DB_werk.loc[df_DB_werk['ID'] == ID, df_DB_werk.columns[1]] = False #Besetz
        if self.lane_address == '': # IF IT'S THE LAST LANE FROM THE PRODUCTION LINE, REMOVE THE ID FROM THE LANE
            df_DB_lane = df_DB_lane[df_DB_lane['ID'] != ID]
        df_DB_lane.to_csv(self.lane_DB , index=False)
        df_DB_werk.to_csv(self.werk_DB , index=False)


        #Remove the first box from the order and rearrange the ord

# # Class for the Digistal shadow of the Inventar
# class InventarDataDistribution:
#     def __init__(self,lane_address, date, timestamp,event_type):

    


# if __name__ == "__main__":
#     date, lane, timestamp, event_type = read_kafka_lane_time_event(csv_file_path)
#     InventarDataDistribution(Lane(lane), date, timestamp, event_type)
   