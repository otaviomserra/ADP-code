import pandas as pd
import numpy as np
import os
import re

# Need to change the log path and name according to the new log to be worked
# Need automation
path='/logs/teste.log'
log_data=open(path,'r')

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

# Creating path for csv files
if not os.path.exists('ADP-code/csv-logs'):
   os.makedirs('ADP-code/csv-logs')

# Saving the csv files
df.to_csv('/csv-logs/df_teste.csv',index=False)
df.to_excel('/csv-logs/df_teste.xlsx')
