import pandas as pd
import members

emailed = {}
not_emailed = {}
    
df1 = pd.read_csv('form2.csv')
df2 = pd.read_csv('form1.csv')

for index, row in df1.iterrows():
    emailed[row['Email']] = row['First_Name']

for index, row in df2.iterrows():
    if row['Email'] not in emailed:
        not_emailed[row['Email']] = row['First_Name']
        members.send_email(row['Email'], row['First_Name'])








