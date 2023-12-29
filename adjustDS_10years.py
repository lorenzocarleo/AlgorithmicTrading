import pandas as pd 
from datetime import datetime
from datetime import timedelta

def add_10years(date_string):
   date_obj = datetime.strptime(date_string, '%m/%d/%Y')
   new_date_obj = date_obj.replace(year=date_obj.year + 10)
   return new_date_obj.strftime('%m/%d/%Y')


# Read the CSV file with tab as a delimiter
df = pd.read_csv('/Users/lorenzocarleo/git/AlgorithmicTrading/stockPrice.csv', sep='\t')

# Print the column names (for debugging)
#print("Column names:", df.columns.tolist())

#df['Date'] = df['Date'].apply(add_10years)

#df.to_csv('/Users/lorenzocarleo/git/AlgorithmicTrading/stockPrice_new.csv', index=False)

# Print the column names (for debugging)
print("Column names:", df.columns.tolist())

# Make sure to replace 'Date' with the actual column name from your CSV
df['Date'] = df['Date'].apply(add_10years)

# Save to a new CSV file
df.to_csv('updated_dataset.csv', index=False)