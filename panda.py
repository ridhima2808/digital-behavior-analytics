import pandas as pd
df = pd.read_csv('digital_behaviour.csv') #df is a refernce to dataFrame object
print(df)
# sep:
# encoding:
# nrows:
print(df.head())
print(df.tail())
print(df.shape)
print(df.column)
df[['Instagram_Minutes','Youtube_Minutes']].describe()
