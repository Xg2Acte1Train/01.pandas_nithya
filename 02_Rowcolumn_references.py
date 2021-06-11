import pandas as pd

l1 = [90,83,67,83,45]
l2 = [[90,83,67,83,45],[68,89,75,56,73],[58,88,60,90,100]]

df = pd.DataFrame(l2)

print (df) 
print (df[2])
print (df[:2])
print (df[-2:])

df = pd.DataFrame(l2,columns=['Tamil','English','Maths','Science','Social'],index=['Ramesh','Suresh','Kamesh'],dtype='int32')

print (df)
print (df['Maths'])
print (df[:'Suresh'])
print (df['Suresh':])

s = pd.Series(l1,index=['Tamil','English','Maths','Science','Social'])
print (s[['Tamil','Social']])
