import pandas as pd
df =pd.read_csv('data.csv')
# print(df.head())
# print(df.tail())
# print(df.info())
print(df['diffBreath'].value_counts())
print(df.describe())