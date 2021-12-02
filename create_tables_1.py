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
      print("The table "+table_name+" is/was created")

def show_tables(mycursor):
  call = "SHOW TABLES"
  mycursor.execute(call)
  for row in mycursor:
    print(row['Tables_in_playground'])

def was_ist_drinnen(mycursor):
  column_list = []
  full_list = []
  call = "SHOW COLUMNS FROM customers"
  mycursor.execute(call)
  for row in mycursor:
    column_list.append(row['Field'])
  
  for i in column_list:
    print(i)

  call = "SELECT * FROM customers"
  mycursor.execute(call)
  for row in mycursor:
    print(row)
  




  
  
  

def fill_table():
  pass


values = ["id","name", "address"]
types = ["INT(11) NOT NULL AUTO_INCREMENT","VARCHAR(255)", "VARCHAR(255)"]
name = "customers"


mycursor = mydb.cursor(dictionary=True, buffered=True)

#mycursor.execute("DROP TABLE customers")
#create_table(name, values, types, mycursor)
#show_tables(mycursor)
was_ist_drinnen(mycursor)

