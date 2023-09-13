import os
import pandas as pd

FabrikVerbindung = pd.read_excel("FabrikVerbindung.xlsx", index_col=0)

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
        
        self.inventar_folder = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "inventar"].iloc[0]
        self.lane_folder = FabrikVerbindung.loc[FabrikVerbindung["lane_address"] == lane, "lane_inventar"].iloc[0]

    def put_event(self):
        print()
        #Add a box into the model with it's info
    
    def pick_event(self):
        print()
        #Remove the first box from the order and rearrange the order