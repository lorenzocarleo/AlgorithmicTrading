import pandas as pd 
from datetime import datetime
from datetime import timedelta

def add_10years(date_string):
   date_obj = datetime.strptime(date_string, '%Y-%m-%d')
   new_date_obj = date_obj.replace(year=date_obj.year + 10)
   return new_date_obj.strftime('%Y-%m-%d')


df = pd.read_csv('/Users/lorenzocarleo/git/AlgorithmicTrading/stockPrice.csv')

df['date'] = df['date'].apply(add_10years)

df.to_csv('/Users/lorenzocarleo/git/AlgorithmicTrading/stockPrice_new.csv', index=False)

