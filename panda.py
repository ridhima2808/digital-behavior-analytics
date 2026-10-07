import pandas as pd
df = pd.read_csv('digital_behaviour.csv') #df is a refernce to dataFrame object
print(df)
# sep:
# encoding:
# nrows:
print(df.head())
print(df.tail())
print(df.shape)
print(list(df.columns))
col_name = ['Instagram_Minutes','YouTube_Minutes']
#df[col_name].describe()
df[['Instagram_Minutes','YouTube_Minutes']].describe()
print(df['Instagram_Minutes'].sum())
print(df['Study_Minutes'].mean())
print(df['YouTube_Minutes'].max())
print(round(df['Study_Minutes'].mean(),2))
print(df[df['Instagram_Minutes']>100])
print(df[df['Study_Minutes']>180])
print(df[df['Instagram_Minutes']>df['Study_Minutes']])
danger_days = df[(df['Instagram_Minutes']>100) & (df['Study_Minutes']<100)]
print(danger_days)
print(df.sort_values("Instagram_Minutes", ascending = False).head())
print(df.sort_values("Study_Minutes", ascending = False).head())
print(df['Instagram_Minutes'].max())
df['Total_Screen_Time'] = (df['Instagram_Minutes'] + df['Study_Minutes'] + df['WhatsApp_Minutes'])
df['Screen_Hours'] = (df['Total_Screen_Time'] / 60).round(2)
#print(df['Screen_Hours'])
df['Digital_Balance'] = (df['Study_Minutes'] / df['Total_Screen_Time']).round(2)
print(df['Digital_Balance'])
df['Day_Type'] = 'normal' 
'''df.loc[df['Total_Screen_Time']>300,'Day_Type'] = "Heavy" '''
df['Total_Screen_Time' > 300]['Day_Type'] = "Heavy"
print(df["Day_Type"])

print(df[['Instagram_Minutes','YouTube_Minutes','WhatsApp_Minutes','LinkedIn_Minutes']].sum())
print(df[['Instagram_Minutes','YouTube_Minutes','WhatsApp_Minutes','LinkedIn_Minutes']].max())
