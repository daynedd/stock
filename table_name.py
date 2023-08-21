import mysql.connector
import pandas as pd 
import time as at
start = at.time()
data = pd.read_csv("BILI.csv")


data = data.drop('Adj Close',axis = 1)
open = data['Open']
high= data['High']
low= data['Low']
close_price= data['Close']
date= data['Date']
vol = data["Volume"]

i=1
value=[]
for i in range(len(date)):
    value.append((date[i],open[i],high[i],low[i],close_price[i],int(vol[i])))

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Dayne218!!",
  database='stock'
)
cursor = mydb.cursor()
#cursor.execute('CREATE DATABASE STOCK')
cursor.execute('CREATE TABLE BiliBili (Date DATE PRIMARY KEY,Open_price FLOAT(4),High FLOAT(4), Low FLOAT(4), Close_price FLOAT(4),Volume INT)')
sql = "INSERT INTO BiliBili (Date , Open_price, High , Low, Close_price, Volume) VALUES (%s, %s, %s, %s, %s, %s)"


for i in range(len(value)):
      cursor.execute(sql, value[i])

#cursor.execute('DROP TABLE BiliBili ')

mydb.commit()
end = at.time()
print("The time of execution of above program is :",
     (end-start) , "s")