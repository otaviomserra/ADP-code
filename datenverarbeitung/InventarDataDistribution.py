import os
import pandas as pd

# Reading the dictionary which connects the lanes, target lanes and identifies the inverntar/processes 
FabrikVerbindung = pd.read_excel("FabrikVerbindung.xlsx", index_col=0)

# Class for box description
class Box:
    def __init__(self,lane_address):
        self.lane = Lane(lane_address)
        self.box_capacity = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "box_capacity"].iloc[0]
        self.variant = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "variant"].iloc[0]

        
    def create_ID(): 
        # CRIAR UM ID NUMERICO PRA CADA CAIXA
        # OU SEJA, ESTÁ INSTANCIANDO UM OBJETO COM REFERENCIA EM UMA LANE ESPECIFICA
        # SÓ CRIA UM ID CASO SEJAM LANES ESPECIFICAS (INICIO DA LINHA DE PRODUCAO)
        # ESSE ID TEM PARAMETRO DA LANE
        pass 
    def remove_ID():
        # DESISTANCIAR O OBJETO DE ID DESSA CAIXA
        # O ID SÓ VAI EXISTIR E FICAR MAIS APARENTE NO DB GERAL PRA GUARDAR INFOS
        pass

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
    def __init__(self,lane):
        self.lane_address = lane
        self.capacitaty = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "capacity"].iloc[0]
        self.inventar_path = ""
        self.lane_path = ""

        # Finding the specific Inventar and Lane
        self.inventar_name = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "inventar"].iloc[0]
        self.lane_name = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "lane_inventar"].iloc[0]

    def find_folder(self,lane):
        # Find folder and return it's path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        werk_folder_path = os.path.join(current_dir, "..", "Werk")
        inventar_folder_path = os.path.join(current_dir, "..", "Werk", "Inventar")


        self.inventar_path = os.path.join(inventar_folder_path,f"{self.inventar_name}")
        self.lane_path = os.path.join(inventar_folder_path,f"{self.lane_name}")
        self.werk_path = os.path.join(werk_folder_path,"Werk_DS.csv")
        
        inventar_csv_name = f'{self.inventar_name}' + '_DS.csv'
        lane_csv_name = f'{self.lane_name}'+'_DS.csv'
        
        self.inventar_csv = os.path.join(self.inventar_path,inventar_csv_name)
        self.lane_csv = os.path.join(self.lane_path, lane_csv_name)
    
    def put_event(self):
        print()
        #Add a box into the model with it's info
    
    def pick_event(self):
        print()
        #Remove the first box from the order and rearrange the ord

# # Class for the Digistal shadow of the Inventar
# class InventarDataDistribution:
#     def __init__(self,lane_address, date, timestamp,event_type):
#         self.event_type = event_type
#         self.timestamp = timestamp
#         self.lane = Lane(lane_address)
#         self.date = date
    


# if __name__ == "__main__":
#     date, lane, timestamp, event_type = read_kafka_lane_time_event(csv_file_path)
#     InventarDataDistribution(Lane(lane), date, timestamp, event_type)
   