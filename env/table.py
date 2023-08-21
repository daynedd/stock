import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Dayne218!!"
)
cursor = mydb.cursor()
cursor.execute('CREATE DATABASE STOCK')