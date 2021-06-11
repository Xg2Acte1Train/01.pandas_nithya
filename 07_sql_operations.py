import pandas as pd

df = pd.read_csv("./girls.csv")
print (df)

print (df.head())
print (df.head(2))

print (df[df['place'] == 'Hyderabad'])

df1 = df.groupby('place')
print (df1.size())

print (df1.groups)
print (df1.get_group('Delhi'))
print (df1.filter(lambda x: len(x) >= 3))

for i, j in df1:
    print (i)
    print (j)
    
df2 = pd.read_csv("./boys.csv")
print (df2)

print (pd.concat([df,df2])) 

print (df.append(df2)) 

print (pd.merge(df,df2,on='place'))

print (pd.merge(df,df2,on='place',how='right')) # left, outer, inner 

print (df2.sort_index(ascending=False))
print (df2.sort_values(by='age'))
