import os
import pandas as pd
import numpy as np
from InventarDataDistribution import *
import time
import datetime


def calculate_Bestandsmenge(df_DB_lane, box_capacity):
    # Amount of parts currently on the lane
    condicao = df_DB_lane['Besetzt'] == True
    linhas_a_atualizar = condicao.index[condicao].tolist()  # Find indexes with besetzt equals to True
    Bestandsmenge = len(linhas_a_atualizar) * box_capacity 
    return Bestandsmenge # number of parts

def calculate_Kapazitaet(lane_capacity, box_capacity):
    # Total amount of parts that fit into the lane
    kapazitaet = lane_capacity * box_capacity
    return kapazitaet # number of parts

def calculate_Lagernutzungsgrad(bestandsmenge, kapazitaet):
    # Percentage of how full is the lane 
    lagernutzungsgrad = bestandsmenge/kapazitaet * 100
    return lagernutzungsgrad # %

def calculate_Bestandsgenauigkeit():
    # Precision of the model in how many parts or boxes are right when compared to the real inventory
    # There is no way of calculating how many are currently there given the model approach
    # The program basically gets the data from the logs that Neoception generates after receiving the box
    # This would increase the complexity of the code to deal with errors of putting the boxes
    # Benny's program would be able to show which boxes are misplaced, however even those are not fully correct or precise per tests 
    # and there are missing sensors such as RFIDs and Lanes with optical sensors

    # A way to implement this would be either trying to hijack the information of benny's code before it gets sent to Neoception or
    # to create a request list that would avaliate if the box were inserted into the right lane and, if not, show it that's wrong and
    # also create a system that would be able to deal with wrong informations so that those are not considered in metrics
    return 1 * 100 # %

def calculate_Durchschnittliche_Wartezeit(df_Hist_lane):
    # Average time for the same box enter and exit the lane
    # Calculate from Historic log
    filtered_df = df_Hist_lane[df_Hist_lane['Besetzt'] == False].copy()
    filtered_df['Timestamp_in'] = pd.to_datetime(filtered_df['Date_in'] + ' ' + filtered_df['Timestamp_in'])
    filtered_df['Timestamp_out'] = pd.to_datetime(filtered_df['Date_out'] + ' ' + filtered_df['Timestamp_out'])
    filtered_df['Diferenca_tempo'] = filtered_df['Timestamp_out'] - filtered_df['Timestamp_in']
    average = filtered_df['Diferenca_tempo'].mean()

    return average

def calculate_Lagerumschlagsrate(df_Hist_lane):
    # How often a inventory replaces it's inventory
    # Calculate from Historic log
    return "AAAAAAAAA"

def calculate_Reichweite(df_Hist_lane):
    # How long the current inventory is expected to last
    # Calculate from Historic log
    return "AAAAAAAAA"

def calculate_Wiederbeschaffungszeit():
    # Necessary time to replenish the lane stock based on the previous proccesess
    # Calculate from werk databank
    return "AAAAAAAAA"
#################################################################
# MAIN FUNCTION                                                 #
#################################################################


def calculate_inventory_kpis():
    # This will be the main function at the end that only calls each individual calculation
    # and then adds the result to the _DS.csv files.
    return 0
