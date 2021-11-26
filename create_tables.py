import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="P$kbYYgC?xXX83rF336R9@QPz7",
  database = "playground"
)

def create_table(table_name, table_values, table_values_type,):
  pass

mycursor = mydb.cursor(dictionary=True, buffered=True)

val = "customers"
#mycursor.execute("DROP TABLE "+val)

mycursor.execute(
  "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"
  )

mycursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = DATABASE() AND table_name = 'customers'")
for row in mycursor:
  print(row['COUNT(*)'])
  if row['COUNT(*)'] == 1:
    print("YESSSSSSSSSSS")

mycursor.execute("SHOW TABLES")
for row in mycursor:
  print(row['Tables_in_playground'])

mycursor.execute("SHOW COLUMNS FROM customers")

for row in mycursor:
  print(row)