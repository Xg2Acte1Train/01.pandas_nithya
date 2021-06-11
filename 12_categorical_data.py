import pandas as pd

d = {'Names' : pd.Series(['Mahesh','Yazhini','Kadiresan','Malathi','Kumar','Sujith']), 
'Gender' : pd.Series(['Male','Trans','Male','Female','Male','Trans'],dtype="category")}
df = pd.DataFrame(d)

print (df['Names'])
print (df['Gender'])
print (df['Gender'].cat.remove_categories(['Trans'])) # add_categories()
print (df['Gender'].cat.categories)

c = pd.Categorical(['AB+', 'B+', 'AB+', 'O+', 'B-', 'AB-','B+'])
df['Blood_group'] = pd.Series(c)
print (df['Blood_group'])

c = pd.Categorical(['AB+', 'B+', 'AB+', 'O+', 'B-', 'AB-','B+'],['O+','B+'])
df['Blood_group'] = pd.Series(c)
print (df['Blood_group'])

print (c.ordered)

df['Mid Year points'] = pd.Series(["50","90","80","50","120","100"])
df['Year End points'] = pd.Series(["80","50","80","90","100","50"])

df['Mid Year points'] = df['Mid Year points'].astype("category", categories=["50","80","90"], ordered=True)
df['Year End points'] = df['Year End points'].astype("category", categories=["50","80","90"], ordered=True)

print (df['Mid Year points']>df['Year End points'])

print (df)
