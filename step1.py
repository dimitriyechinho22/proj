import pandas as pd
import re

df = pd.read_csv('buildings.txt')

correct_df = pd.DataFrame(columns=df.columns)
error_df = pd.DataFrame(columns=df.columns)

for i, row in df.iterrows():
    if not isinstance(row['id'], int):
        error_df = error_df.append(row)
        continue

    if not re.match(r'^[A-Za-z0-9\s]{0,255}$', row['full_name']):
        error_df = error_df.append(row)
        continue

    if not pd.to_numeric(row[['latitude', 'longitude']], errors='coerce').notnull().all():
        error_df = error_df.append(row)
        continue

    if not row['type of building'] in ['value1', 'value2', 'value3']:
        error_df = error_df.append(row)
        continue

    for col in df.columns:
        if col not in ['id', 'full_name', 'latitude', 'longitude', 'type of building']:
            if col == 'created_at' or col ==   'updated_at':
                if not re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', row[col]):
                    error_df = error_df.append(row)
                    continue
                continue
            if col == 'name':
                if not re.match(r'^[a-zA-Z\s]+$', row[col]):
                    error_df = error_df.append(row)
                    continue
                continue
            if col == 'postal_codes' or col == 'region_id' or col == 'population':
                if not str(row[col]).isdigit():
                    error_df = error_df.append(row)
                    continue
                continue
            if col == 'region_code':
                if not re.match(r'^[A-Z]\d*$', row[col]):
                    error_df = error_df.append(row)
                    continue
                continue



    else:
        correct_df = correct_df.append(row)

print('Correct rows:')
print(correct_df)
print('\nErroneous rows:')
print(error_df)
