import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="P$kbYYgC?xXX83rF336R9@QPz7",
  database = "playground"
)

def create_table(table_name, table_values, table_values_type, mycursor):
  call = "CREATE TABLE"
  call += " " + table_name + " ("
  for i in range(len(table_values)):
      call += table_values[i] + " " + table_values_type[i]
      if len(table_values)-1 != i:
        call += ","
      else:
        call += ")"
  mycursor.execute(call)
  mycursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = DATABASE() AND table_name = '" + table_name + "'")
  for row in mycursor:
    if row['COUNT(*)'] == 1:
      print("Table is/was created")

def show_tables(mycursor):
  call = "SHOW TABLES"
  
  
  
  

def fill_table():
  pass


values = ["name", "address"]
types = ["VARCHAR(255)", "VARCHAR(255)"]
name = "customers"


mycursor = mydb.cursor(dictionary=True, buffered=True)

mycursor.execute("DROP TABLE customers")
create_table(name, values, types, mycursor)
show_tables(mycursor)

