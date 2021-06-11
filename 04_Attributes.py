import pandas as pd

s = pd.Series([90,83,67,83,45])
df = pd.DataFrame([[90,83,67,83,45],[68,89,75,56,73],[58,88,60,90,100]])
p = pd.Panel({'Midterm': pd.DataFrame([[90,83,67,83,45],[68,89,75,56,73],[58,88,60,90,100]]), 
'Quarterly': pd.DataFrame([[35,44,65,56,79],[85,55,84,50,99],[65,90,87,69,78]])})

print (s.axes)
print (df.axes)
print (p.axes)

df2 = pd.DataFrame()
print (s.empty)
print (df2.empty)
print (p.empty)

print (s.shape)
print (df.shape)
print (p.shape)

print (s.ndim)
print (df.ndim)
print (p.ndim)

print (s.size)
print (df.size)
print (p.size)

print (s)
print (s.values)
print (df.values)
print (p.values)

print (s.head(2)) 
print (df.head(2)) 
print (s.tail(2))
print (df.tail(2))
# panel doesn't have these attributes

print (df.T) 
# Panel & Series doesn't have these attributes

print (s.dtypes) 
print (df.dtypes) 
print (p.dtypes) 

print (df)
print (df.describe())
print (df.sum())
print (df.sum(1))
print (df.mean(1))
print (df.std(1))


