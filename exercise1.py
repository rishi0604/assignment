import pandas as pd
from datetime import datetime, timedelta

input_file = 'input.csv'
df = pd.read_csv(input_file)


far_future_date = datetime(2100, 1, 1)


transformed_records = []


for index, row in df.iterrows():
    
    effective_date = datetime.strptime(row['Date of Joining'], '%Y-%m-%d')

    
    if index < len(df) - 1:
        end_date = datetime.strptime(df.loc[index + 1, 'Date of Joining'], '%Y-%m-%d') - timedelta(days=1)
    else:
       
        end_date = far_future_date

    
    record = {
        'Employee Code': row['Employee Code'],
        'Manager Employee Code': row['Manager Employee Code'],
        'Effective Date': effective_date.strftime('%Y-%m-%d'),
        'End Date': end_date.strftime('%Y-%m-%d'),
        'Compensation 1': row['Compensation 1'],
        'Compensation 1 date': row['Compensation 1 date'],
        'Compensation 2': row['Compensation 2'],
        'Compensation 2 date': row['Compensation 2 date'],
        'Review 1': row['Review 1'],
        'Review 1 date': row['Review 1 date'],
        'Review 2': row['Review 2'],
        'Review 2 date': row['Review 2 date'],
        'Engagement 1': row['Engagement 1'],
        'Engagement 1 date': row['Engagement 1 date'],
        'Engagement 2': row['Engagement 2'],
        'Engagement 2 date': row['Engagement 2 date']
    }

    
    transformed_records.append(record)


output_df = pd.DataFrame(transformed_records)


output_file = 'historical_employee_data9.csv'
output_df.to_csv(output_file, index=False)

print('Transformation completed. Output saved to {output_file}')

