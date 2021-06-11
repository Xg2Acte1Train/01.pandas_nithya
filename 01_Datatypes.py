import pandas as pd

print (pd.Series())
print (pd.DataFrame())
print (pd.Panel())

l1 = [90,83,67,83,45]
s = pd.Series(l1)
print (s)

df = pd.DataFrame(l1)
print (df)

l2 = [[90,83,67,83,45],[68,89,75,56,73],[58,88,60,90,100]]
df = pd.DataFrame(l2)
print (df) 

d1 = {'Midterm': pd.DataFrame([[90,83,67,83,45],[68,89,75,56,73],[58,88,60,90,100]]), 
'Quarterly': pd.DataFrame([[35,44,65,56,79],[85,55,84,50,99],[65,90,87,69,78]]), 
'Half early': pd.DataFrame([[80,78,90,68,66],[35,89,67,79,90],[67,89,59,90,45]]),
'Annual': pd.DataFrame([[90,94,58,69,84],[95,68,57,89,96],[90,58,67,96,78]])}
p = pd.Panel(d1)
print (p)
print (p['Midterm'])
print (p.major_xs(1))
print (p.minor_xs(1))

print (s.dtype) # This attribute available only for series
print (df.dtypes) 
print (df[1].dtype)
