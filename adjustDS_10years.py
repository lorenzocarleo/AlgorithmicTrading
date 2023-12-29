import pandas as pd 
import os
from datetime import datetime
from datetime import timedelta

old_file = '/Users/lorenzocarleo/git/AlgorithmicTrading/stockPrice.csv'
new_file = '/Users/lorenzocarleo/git/AlgorithmicTrading/stockPrice_new.csv'

def add_10years(date_string):
   date_obj = datetime.strptime(date_string, '%m/%d/%Y')
   new_date_obj = date_obj.replace(year=date_obj.year + 10)
   return new_date_obj.strftime('%m/%d/%Y')


# Read the CSV file with tab as a delimiter
df = pd.read_csv(old_file, sep='\t')

# Print the column names (for debugging)
#print("Column names:", df.columns.tolist())

# Make sure to replace 'Date' with the actual column name from your CSV
df['Date'] = df['Date'].apply(add_10years)

# Save to a new CSV file
df.to_csv(new_file, index=False)

# Check if the new file has been created
if os.path.exists(new_file):
    print(f"File '{os.path.basename(new_file)}' created successfully.")
else:
    print(f"Failed to create the file '{os.path.basename(new_file)}'.")

