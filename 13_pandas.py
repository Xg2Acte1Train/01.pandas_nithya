import pandas as pd
from datetime import datetime,timedelta
import numpy as np

df = pd.read_csv('./13_input_data.csv')
df1 = pd.DataFrame()
df1['code'] = df['category'].astype(str)+'_'+df['rating'].astype(str)
df1['rating'] = df['rating']
df1['year'] = pd.DatetimeIndex(df['telecasted_date']).year
df1['telecasted_quarter'] = df1['year'].astype(str)+' Quarter '+pd.DatetimeIndex(df['telecasted_date']).quarter.astype(str)
df1['score'] = df['score']
df2 = df1.groupby(['code','rating','year','telecasted_quarter'])['rating'].count().reset_index(name="total_programs")
df2['greater_than_5'] = df2['total_programs'].apply(lambda x: 'YES' if x >= 5 else 'No')
df3 = df1.groupby(['code','rating','year','telecasted_quarter'])['score'].mean().reset_index(name="all")
df2['all'] = df3['all']

df4 = df1.groupby(['code','rating','year','telecasted_quarter'])['score']
l1 = []
for i,j in df4:
	y = float(j[0:5].mean())
	l1.append(y)
df2['first_5'] = pd.Series(l1)
print (df2)

l2 = []
for i,j,k in zip(df2['all'],df2['first_5'],df2['greater_than_5']):
	if k=='YES':
		l2.append(j)
	else:
		l2.append(i)
df2['avg_score'] = pd.Series(l2)
df2 = df2[['code','telecasted_quarter','avg_score']]

print (df2)
