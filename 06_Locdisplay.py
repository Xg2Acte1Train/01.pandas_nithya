import pandas as pd

df = pd.read_csv("./girls.csv")
print (df.shape)
print (df.columns)
print (df['fname']) # df.fname , df['fname','age'] 

print (df.loc[ 1:4 , 'fname' ])
print (df.loc[ [1,4] , 'fname' ])
print (df.loc[ : , 'age']>30 )

print (df.ix[1:4, 'fname' ])
print (df.ix[[1,4], 'fname' ])
print (df.ix[ : , 'age']>30 )

print (df.iloc[1:4,1:4])
print (df.iloc[[1,4],[1,4]])
print (df.iloc[[1,4],lambda x : [1,4]])

print (pd.get_option("display.max_rows")) # max_columns

pd.set_option("display.max_rows",5) # reset_option()
pd.set_option("display.max_columns",4) # reset_option()
print (df)

pd.reset_option("display.max_rows")
pd.reset_option("display.max_columns")

print (pd.describe_option("display.max_rows"))

with pd.option_context("display.max_rows",5):
   print (df)
