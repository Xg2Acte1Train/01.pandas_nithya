import pandas as pd

d = {'Tamil' : 90, 'English' : 83, 'Maths' : 67, 'Science' : 83, 'Social' : 45}

s = pd.Series(d)
print (s)

l = [{'Tamil' : 90, 'English' : 83, 'Maths' : 67, 'Science' : 83, 'Social' : 45},
      {'Tamil' : 68, 'English' : 89, 'Maths' : 75, 'Science' : 56, 'Social' : 73},
      {'Tamil' : 58, 'English' : 88, 'Maths' : 60, 'Science' : 90, 'Social' : 100}]

df = pd.DataFrame(l)
print (df)

df = df[['Tamil','English','Maths','Science','Social']]
print (df)

d = {'Tamil' : [90,68,58], 'English' : [83,89,88], 'Maths' : [67,75,60], 'Science' : [83,56,90], 'Social' : [45,73,100]}

df = pd.DataFrame(d)
print (df)

d = {'Tamil' : pd.Series([90,68,58]), 'English' : pd.Series([83,89,88]), 'Maths' : pd.Series([67,75,60]), 
     'Science' : pd.Series([83,56,90]), 'Social' : pd.Series([45,73,100])}
df = pd.DataFrame(d)
print (df)

df['Environmental Science']=pd.Series([90,92,98])
print (df)

df = pd.DataFrame(d,columns=['Tamil','English','Social'])
print (df)
