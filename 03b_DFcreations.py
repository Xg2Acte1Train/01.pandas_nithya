import pandas as pd
import numpy as np

df = pd.read_csv("./girls.csv")
print (df)

df = pd.read_csv("./girls.csv",index_col=['id'])
print (df)

df = pd.read_csv("./girls.csv",names=['a', 'b', 'c','d','e','f','g'])
print (df)

df=pd.read_csv("./girls.csv",header=4)
print (df)

df=pd.read_csv("./girls.csv",skiprows=5,dtype={'40': np.float64})
print (df)

df.to_csv('aaa.csv')
