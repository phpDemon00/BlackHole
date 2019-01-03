import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "stan",
  passwd = "stan",
)

print(mydb) 