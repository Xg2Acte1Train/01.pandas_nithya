import pandas as pd
import numpy as np

l2 = [[90,83,67,83,45],[68,89,75,56,73],[58,88,60,90,100]]
df = pd.DataFrame(l2,columns=['Tamil','English','Maths','Science','Social'],index=['Ramesh','Suresh','Kamesh'],dtype='int32')

print (df)
print (df.pct_change())
print (df['Tamil'].cov(df['English']))
print (df.cov())
print (df.corr())
print (df.rank())
print (df.rolling(window=3).mean())
print (df.rolling(window=3,min_periods=2).mean())
print (df.rolling(window=3,min_periods=2).aggregate([np.sum,np.mean]))
print (df.rolling(window=2).sum())
print (df.expanding(min_periods=2).sum())
print (df.ewm(com=0.5).mean())
