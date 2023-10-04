import os
import pandas as pd
import numpy as np
from InventarDataDistribution import *
import time
import datetime


def calculate_Bestandsmenge(df_DB_lane, box_capacity):
    condicao = df_DB_lane['Besetzt'] == True
    linhas_a_atualizar = condicao.index[condicao].tolist()  # Encontre os índices das linhas com Besetzt True
    Bestandsmenge = len(linhas_a_atualizar) * box_capacity
    return Bestandsmenge 

def calculate_Kapazitaet(lane_capacity, box_capacity):
    kapazitaet = lane_capacity * box_capacity
    return kapazitaet

def calculate_Lagernutzungsgrad():
    return "AAAAAAAAA"

def calculate_Bestandsgenauigkeit():
    return "AAAAAAAAA"

def calculate_Durchschnittliche_Wartezeit():
    return "AAAAAAAAA"

def calculate_Lagerumschlagsrate():
    return "AAAAAAAAA"

def calculate_Reichweite():
    return "AAAAAAAAA"

def calculate_Wiederbeschaffungszeit():
    return "AAAAAAAAA"
#################################################################
# MAIN FUNCTION                                                 #
#################################################################


def calculate_inventory_kpis():
    # This will be the main function at the end that only calls each individual calculation
    # and then adds the result to the _DS.csv files.
    return 0
