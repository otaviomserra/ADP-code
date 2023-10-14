import os
import pandas as pd
import numpy as np
from InventarDataDistribution import *
import time
import datetime
from datetime import datetime, timedelta


def calculate_Bestandsmenge(df_DB_lane, box_capacity):
    # Amount of parts currently on the lane
    condicao = df_DB_lane['Besetzt'] == True
    linhas_a_atualizar = condicao.index[condicao].tolist()  # Find indexes with besetzt equals to True
    Bestandsmenge = len(linhas_a_atualizar) * box_capacity 
    return Bestandsmenge # number of parts


def calculate_Kapazitaet(lane_capacity, box_capacity):
    # Total amount of parts that fit into the lane
    kapazitaet = lane_capacity * box_capacity
    return kapazitaet  # number of parts


def calculate_Lagernutzungsgrad(bestandsmenge, kapazitaet):
    # Percentage of how full is the lane 
    lagernutzungsgrad = bestandsmenge/kapazitaet * 100
    return lagernutzungsgrad  # %


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
    return 1 * 100  # %

def calculate_Durchschnittliche_Wartezeit(df_Hist_lane):
    # Average time for the same box enter and exit the lane
    # Calculate from Historic log by averaging how long it took for a box to enter and exit the lane
    # Can be optimized by changing the exit time format (right now in days because Dashboard wanted, but it's a dumb format)
    # There are also other time formats more adequate to visualization
    try:
        filtered_df = df_Hist_lane[df_Hist_lane['Besetzt'] == False].copy()
        filtered_df['Timestamp_in'] = pd.to_datetime(filtered_df['Date_in'] + ' ' + filtered_df['Timestamp_in'])
        filtered_df['Timestamp_out'] = pd.to_datetime(filtered_df['Date_out'] + ' ' + filtered_df['Timestamp_out'])
        filtered_df['Diferenca_tempo'] = filtered_df['Timestamp_out'] - filtered_df['Timestamp_in']
        # Calcule a diferença de tempo onde 'Besetzt' for False
        diferencas_tempo = filtered_df['Diferenca_tempo']
        # Calcule a média das diferenças de tempo
        media_diferencas_tempo = diferencas_tempo.mean()
        # Calcule os dias, horas, minutos e segundos da média
        dias = media_diferencas_tempo.days
        segundos_total = media_diferencas_tempo.seconds
        segundos_total_2 = media_diferencas_tempo.seconds
        horas, segundos_total = divmod(segundos_total, 3600)
        horas_total = dias * 24 + segundos_total_2 // 3600
        minutos, segundos = divmod(segundos_total, 60)

        # Formate a média no formato "DD hh:mm:ss" se houver dias, ou no formato "hh:mm:ss" se não houver dias
        media_dd_hh_mm_ss = f"{dias} {horas:02}:{minutos:02}:{segundos:02}" if dias > 0 else f"{horas:02}:{minutos:02}:{segundos:02}"

        # Formate a média no formato "hh:mm:ss"
        media_hh_mm_ss = f"{horas_total:02}:{minutos:02}:{segundos:02}"
        media_diferencas_tempo_2 = diferencas_tempo.mean().total_seconds() / (60 * 60 * 24)
    except:
        media_diferencas_tempo_2 = 0
    
    return media_diferencas_tempo_2 # days


def calculate_Lagerumschlagsrate(df_Hist_lane,lane_capacity):
    # How often a inventory replaces it's inventory
    # Calculate from Historic log
    # The definition itself from the group is somewhat wrong, but the Dashboard wanted
    # as the time needed to a complete inventory to be changes
    # This code gets how long it took for a box to enter and exit and make groups according to the capacity of the lane
    # By doing that it sums how long it took for the group to enter and exit the lane 
    # and average the time between the groups
    # so it does not take account for the time in between a new product entering
    # in other words the time from the exit of one until it's substituted 
    # It can be opitimized by taken this missing time and by reordering the groups
    # to get better average (dropping outliers groups or boxes)
    # If alterations are made here, need to change Reichweite
    try:
        # Crie uma cópia do DataFrame original para não fazer alterações nele
        df_copy = df_Hist_lane.copy()

        # Filtrar os registros em que 'Besetzt' é False
        df_copy = df_copy[df_copy['Besetzt'] == False]
        
        # Ordenar os registros por 'Date_in' e 'Timestamp_in'
        df_copy['DateTime_in'] = pd.to_datetime(df_copy['Date_in'] + ' ' + df_copy['Timestamp_in'])
        df_copy.sort_values(by=['DateTime_in'], inplace=True)

        # Calcular a diferença de tempo entre entrada e saída para cada par de entrada e saída
        df_copy['DateTime_out'] = pd.to_datetime(df_copy['Date_out'] + ' ' + df_copy['Timestamp_out'])
        df_copy['Tempo_de_Troca'] = (df_copy['DateTime_out'] - df_copy['DateTime_in']).dt.total_seconds()

        # Definir a capacidade máxima da estante
        capacidade = lane_capacity  # Substitua pelo valor correto
        # Calcular o tempo médio de troca para conjuntos completos dentro do último ano
        um_ano_antes = datetime.now() - timedelta(days=365)

        df_last_year = df_copy[df_copy['DateTime_in'] >= um_ano_antes]
        df_last_year = df_last_year.reset_index(drop=True)

        # Identificar quando um conjunto completo de peças foi trocado
        df_last_year['Conjunto'] = df_last_year.groupby(df_last_year.index // capacidade)['DateTime_in'].cumcount()

        # Calcular o número de conjuntos completos
        conjuntos_completos = df_last_year.shape[0] // capacidade
        # Inicializar uma lista para armazenar as somas dos tempos de troca por conjunto
        somas_por_conjunto = []
        # Verificar se há dados suficientes para calcular o tempo médio
        try:
            if conjuntos_completos >= 2:
                # Identificar quando um conjunto completo de peças foi trocado
                df_last_year['Conjunto'] = df_last_year.index // capacidade

                # Calcular a soma dos tempos de troca por conjunto
                soma_por_conjunto = df_last_year.groupby('Conjunto')['Tempo_de_Troca'].sum()

                # Adicionar as somas dos tempos de troca por conjunto à lista
                somas_por_conjunto.extend(soma_por_conjunto)

                # Calcular a média das somas dos tempos de troca por conjunto
                tempo_medio  = sum(somas_por_conjunto) / len(somas_por_conjunto)

                # print("Tempo médio de troca para o estoque completo (último ano):", tempo_medio)
                # print('Há mais de dois conjuntos')
            else:
                # Caso não haja dados suficientes, estime o tempo com base na última troca
                ultima_troca = df_last_year['Tempo_de_Troca'].tail(1).values[0]
                tempo_medio = ultima_troca * capacidade
                # print("Estimativa de tempo de troca com base na última peça:", tempo_medio)
                # print("Não houve dados o suficiente")
        except:
            tempo_medio = 0
            # print("Tempo médio de troca para o estoque completo (último ano):", tempo_medio)

        # Converter de segundos para dias
        tempo_medio = tempo_medio/(60 * 60 * 24)
    except:
        tempo_medio = 0

    return tempo_medio  # days


def calculate_Reichweite(Lagerumschlagsrate, Lagernutzungsgrad):
    # How long the current inventory is expected to last
    # Calculate from how fill is the lane right now and multiplying by the average time
    # that the lane needed to cast all it's content
    Reichweite = (Lagernutzungsgrad/100)*Lagerumschlagsrate
    return Reichweite  # days


def calculate_Wiederbeschaffungszeit(df_db_werk, lane_path, lane):
    # Necessary time to replenish the lane stock based on the previous proccesess
    # Calculate from werk databank

    # Filtre o DataFrame para as entradas onde 'Besetzt' é True e a 'letzte Linie' é igual à posição desejada
    position = lane
    df_DB_werk = df_db_werk.copy()
    filtered_df = df_DB_werk[(df_DB_werk['Besetzt'] == True) & (df_DB_werk['letzte Linie'] == position)]

    # Inicializar um dicionário para armazenar os ID e as somas das diferenças de tempo
    id_somas_diff_tempo = {}

    # Iterar sobre as linhas filtradas
    for index, row in filtered_df.iterrows():
        id = row['ID']
        soma_diff_tempo = 0

        for i in range(1, 4):  # Supondo que você tem no máximo 3 pares de entrada/saída (1 a 3)
            date_in = row[f'date{i}in']
            t_in = row[f't{i}in']
            date_out = row[f'date{i}out']
            t_out = row[f't{i}out']

            if pd.notna(date_in) and pd.notna(date_out):
                # Calcular a diferença de tempo e somar à soma_diff_tempo
                diff_tempo = pd.to_datetime(date_out + ' ' + t_out) - pd.to_datetime(date_in + ' ' + t_in)
                soma_diff_tempo += diff_tempo.total_seconds()

        # Verificar se o ID já existe no dicionário
        if id in id_somas_diff_tempo:
            id_somas_diff_tempo[id] += soma_diff_tempo
        else:
            id_somas_diff_tempo[id] = soma_diff_tempo

    # Criar um DataFrame a partir do dicionário
    resultado_df = pd.DataFrame(list(id_somas_diff_tempo.items()), columns=['ID', 'Wiederbeschaffungszeit'])

    wieder_csv_path = os.path.join(lane_path, f'{lane}'+'_wiederbeschaffungszeit.csv')

    # Verificar se o arquivo CSV já existe
    try:
        arquivo_csv = pd.read_csv(wieder_csv_path)

        # Atualizar IDs duplicados no arquivo CSV com os novos valores
        for index, row in resultado_df.iterrows():
            id = row['ID']
            if id in arquivo_csv['ID'].values:
                arquivo_csv.loc[arquivo_csv['ID'] == id, 'Wiederbeschaffungszeit'] += row['Wiederbeschaffungszeit']
            else:
                arquivo_csv = pd.concat([arquivo_csv, row], ignore_index=True)

    except FileNotFoundError:
        # Se o arquivo CSV não existe, criar um novo
        arquivo_csv = resultado_df

    # Salvar o arquivo CSV
    arquivo_csv.to_csv(wieder_csv_path, index=False)

    # Calcular a média das diferenças de tempo
    media_diff_tempo = arquivo_csv['Wiederbeschaffungszeit'].mean()

    media_diff_tempo = media_diff_tempo / (60 * 60 * 24)
    return media_diff_tempo
#################################################################
# MAIN FUNCTION                                                 #
#################################################################


def calculate_inventory_kpis():
    # This will be the main function at the end that only calls each individual calculation
    # and then adds the result to the _DS.csv files.
    return 0
