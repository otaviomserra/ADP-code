import pandas as pd
import json


logger_path = "D:\Francisco - Dados\Documentos\GitHub\ADP-code\datenverarbeitung\csv-logs\df_teste.xlsx"



df = pd.read_excel(logger_path)
df = df[df.apply(lambda row: any('KAFKA' in str(cell) for cell in row), axis=1)].drop(columns=['Type', 'Module'], errors='ignore')


def extract_json_info(row):
    content = row.split('[content=')[1][:-1]  # Extract the content portion
    content_json = json.loads(content)
    header = content_json['header']
    body = content_json['body']['action']['carrier']

    topic = row.split('[topic=')[1].split(']')[0]  # Extract topic

    trace_id = header['traceId']
    id_value = header['id']
    org_id = header['organisationId']

    carrier_action = body['carrierActionType']
    carrier_id = body['carrierId']
    current_count = body['currentCount']
    lane_address = body['laneAddress']


    return topic, trace_id, id_value, org_id, carrier_action, carrier_id, current_count, lane_address

# Apply the function and create new columns
extracted_data = df['Message'].apply(extract_json_info).apply(pd.Series)
extracted_data.columns = ['Topic', 'traceId', 'id', 'organisationId', 'carrierActionType', 'carrierId', 'currentCount', 'laneAddress']


# Concatenate the extracted data with the original DataFrame
df = pd.concat([df, extracted_data], axis=1)

# Drop the original "message" column
df.drop(columns=['Message'], inplace=True)
df.drop(df.columns[0], axis=1, inplace=True)

# Output path
csv_file_path = "TESTElogs.csv"
# Convert the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)




