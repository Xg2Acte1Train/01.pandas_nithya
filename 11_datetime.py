import pandas as pd

df = pd.DataFrame({'Name':['Mahesh','Elango','Kadiresan','Sundar','Kumar'],'Joining_date':['2020.01.14', '2020, 12, 23', 'Nov 19, 2020', '2020, 04, 06','2020.06.30']})
print (df)

df['Joining_date'] = pd.to_datetime(df['Joining_date'])
print (df)

df['confirmation_date'] = df['Joining_date']+pd.Timedelta(days=180)
print (df)

print (pd.Timedelta(days=180))
print (pd.Timedelta('3 days 5 hours 45 minutes 50 seconds'))
print (pd.Timedelta(5,unit='h'))
l1 = [pd.Timedelta(days=i) for i in range(3)]
print (pd.Series(l1))

df['Allocation_date'] = pd.date_range('01/01/2021', periods=5)
print (df)

print (pd.date_range("11:00", "13:30", freq="30min"))
print (pd.date_range('27-Sep-2017', '17-Oct-2017',freq='3D'))

df['Allocation_date'] = pd.bdate_range('01/01/2021', '01/07/2021')
print (df)

print (pd.bdate_range('27-Sep-2017', '17-Oct-2017'))

print (pd.date_range('27-Sep-2017', '17-Dec-2017',freq='M'))
print (pd.period_range('27-Sep-2017', '17-Dec-2017',freq='M'))

df['Today_date'] = pd.datetime.now()
print (df)  

df['Experience'] = df['Today_date'] - df['Joining_date'] 
print (df['Experience'])

print (pd.datetime.now())
print (pd.datetime.now().strftime("%Y-%m-%d"))
print (pd.Timestamp('2021-03-10'))
print (pd.Timestamp(1372898493,unit='s'))
