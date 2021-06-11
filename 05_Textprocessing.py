import pandas as pd

df = pd.DataFrame({'Languages': pd.Series(['Tamil','English']), 'Subjects': pd.Series(['Maths','Science','Social'])})
print (df)
print (df['Languages'].str.upper()) # lower(), swapcase(), islower(), isupper(), isnumeric()
print (df['Languages'].str.split('i'))
print (df['Languages'].str.contains('i'))
print (df['Languages'].str.len())
print (df['Subjects'].str.startswith('S')) # endswith()
print (df['Subjects'].str.count('e'))
print (df['Subjects'].str.find('e'))
print (df['Subjects'].str.findall('e')) 
print (df['Languages'].str.replace('i','e'))
print (df['Languages'].str.cat(sep=','))

s = pd.Series(['Ramu','Somu','Jothi','Rathi','Jothi'])
print (s.str.get_dummies())
print (s.str.repeat(4))
