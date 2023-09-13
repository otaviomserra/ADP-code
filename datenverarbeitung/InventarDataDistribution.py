import os
import pandas as pd

# Reading the dictionary which connects the lanes, target lanes and identifies the inverntar/processes 
FabrikVerbindung = pd.read_excel("FabrikVerbindung.xlsx", index_col=0)

# Class for one specific lane
class Lane_stucture:
    def __init__(self,lane):
        self.lane = lane
        self.capacitaty = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "capacity"].iloc[0]


# Class for the Digistal shadow of the Inventar
class InventarDataDistribution:
    def __init__(self, lane, date, timestamp,event_type):
        self.event_type = event_type
        self.lane = lane
        self.timestamp = timestamp
        self.date = date
        self.inventar_path = ""
        self.lane_path = ""

    def find_folder(self,lane):
        # Find folder and return it's path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        werk_folder_path = os.path.join(current_dir, "..", "Werk")
        inventar_folder_path = os.path.join(current_dir, "..", "Werk", "Inventar")

        # Finding the specific Inventar and Lane
        self.inventar_name = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "inventar"].iloc[0]
        self.lane_name = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "lane_inventar"].iloc[0]

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
        #Remove the first box from the order and rearrange the order
