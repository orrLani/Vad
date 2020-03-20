import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

cred=ServiceAccountCredentials.from_json_keyfile_name('onedrive.json',scope)

gc = gspread.authorize(cred)

wks = gc.open('Courses').sheet1
mydata=wks.get_all_values()
myHead=mydata.pop(0)
df=pd.DataFrame(data=mydata,columns=myHead)
print(df)
print(type(df))
print(5)