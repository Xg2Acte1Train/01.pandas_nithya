import pandas as pd
import numpy as np

l2 = [[90,83,67,83,45],[68,89,75,56,73],[58,88,60,90,100]]
df = pd.DataFrame(l2,columns=['Tamil','English','Maths','Science','Social'],index=['Ramesh','Suresh','Kamesh'],dtype='int32')

df = df.rolling(window=3).mean()
print (df)
print (df.isnull())
print (df.notnull())
print (df.dropna())    
print (df.fillna(0))       
print (df.fillna(method='bfill')) # pad / fill for forward fill; bfill / backfill from backward
print (df.fillna(method='bfill',limit=1))
print (df.sum())
print (df.replace({72:100}))

