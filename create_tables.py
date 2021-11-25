import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="P$kbYYgC?xXX83rF336R9@QPz7",
  database = "playground"
)

def create_table():
  pass

mycursor = mydb.cursor(dictionary=True, buffered=True)

val = "customers"
mycursor.execute("DROP TABLE "+val)

mycursor.execute(
  "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"
  )

mycursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = DATABASE() AND table_name = 'customers'")
for row in mycursor:
  print(row['COUNT(*)'])
  if row['COUNT(*)'] == 1:
    print("YESSSSSSSSSSS")