import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nips",
  password="peach1395",
  database="mydatabase"
)
mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted") 