import pandas as pd
import numpy as np

l2 = [[90,83,67,83,45],[68,89,75,56,73],[58,88,60,90,100]]
df = pd.DataFrame(l2,columns=['Tamil','English','Maths','Science','Social'],index=['Ramesh','Suresh','Kamesh'],dtype='int32')

for i in df:
    print (i)
    
for i in df.itertuples():
    print (i)

for i,j in df.iteritems():
    print (i)
    print (j)

for i,j in df.iterrows():
    print (i)
    print (j)
    
print (df['Tamil'].isin ([68,58]))

print (df.apply(lambda x: x+2))

def hi(a,b):
   return a+b

print (df.pipe(hi,2))

l2 = [[90,83,45],[68,89,73],[58,88,100]]
df2 = pd.DataFrame(l2,columns=['Tamil','English','Social'],index=['Ramesh','Suresh','Jagadesh'],dtype='int32')
print (df2)
print (df2.reindex_like(df))
