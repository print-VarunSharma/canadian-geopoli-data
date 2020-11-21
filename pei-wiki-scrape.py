import pandas as pd
import requests
from bs4 import BeautifulSoup

info = requests.get('https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population').text
bs = BeautifulSoup(info, 'html.parser')
table=bs.find_all('table',class_='wikitable')[1]
df=pd.read_html(str(table))[0]
#Get the first 20 records
df1=df.iloc[:20]

Rank=df1['2019rank'].values.tolist()
City=df1['City'].values.tolist()
#Get the location in list
locationlist=df1['Location'].values.tolist()
Latitude=[]
Longitude=[]
for val in locationlist:
    val1=val.split("/")[-1]
    Latitude.append(val1.split()[0])
    Longitude.append(val1.split()[-1])

df2=pd.DataFrame({"Rank":Rank,"City":City,"Latitude":Latitude,"Longitude":Longitude})
print(df2)