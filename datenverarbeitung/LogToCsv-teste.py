import os
import pandas as pd
import numpy as np
import re

class LogToCSVConverter:
    def __init__(self, log_filename, csv_filename):
        self.log_filename = log_filename
        self.csv_filename = csv_filename

    def convert(self):
        # Creating path for csv files
        # if not os.path.exists('datenverarbeitung/csv-logs'):
        #     os.makedirs('datenverarbeitung/csv-logs')
        # log_path = os.path.join('logs', self.log_filename)
        # csv_path = os.path.join('datenverarbeitung/csv-logs', self.csv_filename)
        
        ### TESTANDO, VOLTAR PRO ANTERIOR AQUI TAMBÉM
        if not os.path.exists('csv-logs'):
            os.makedirs('csv-logs')
        log_path = os.path.join(self.log_filename)
        csv_path = os.path.join('csv-logs', self.csv_filename)

        log_data=open(log_path,'r')

        # Working with the log structure itself

        # Correcting first the problem with lines in the log
        # When there is an error message, the message is printed in differents lines in the log
        # Removing the different lines in the code which does not start with the time stamp
        corrected_lines = []
        for line in log_data:
            if line.startswith("["):
                corrected_lines.append(line)
            else:
                corrected_lines[-1] += line

        # Separating the data between date, time stamp, type, module and message
        # Removing the quotes from each column
        # Minor modifications into the Message
        data = []
        for line in corrected_lines:
            split = line.split(' ',4)
            split[0] = split[0][1:]
            split[1] = split[1][:-1]
            split[2] = split[2][1:-1]
            split[3] = split[3][1:-1]
            split[4] = split[4].replace('\n','')
            split[4] = split[4][1:-1]
            data.append(split)

        df = pd.DataFrame(data, columns=['Date','Hour','Type','Module','Message'])

        # Saving the csv files
        df.to_csv(csv_path,index=False)
        #df.to_excel('/csv-logs/df_teste.xlsx')

        print(f"Transformação concluída. Arquivo '{self.csv_filename}' gerado.")


## ADD NA MAIN E MUDAR ESSA PORRA AQUI
# Nome dos arquivos de entrada (log) e saída (CSV)
log_filename = 'teste.log'
csv_filename = 'log_transformado.csv'

# Criar uma instância da classe e realizar a conversão
converter = LogToCSVConverter(log_filename, csv_filename)
converter.convert()