
mycursor = mydb.cursor(dictionary=True, buffered=True)

val = "customers"
mycursor.execute("DROP TABLE "+val)