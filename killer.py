import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Dayne218!!",
  database='stock'
)
cursor = mydb.cursor()
cursor.execute('DROP TABLE BiliBili ')