import mysql.connector

with mysql.connector.connect(
    host="localhost",
    user="root",
    password="P$kbYYgC?xXX83rF336R9@QPz7",
    database = "playground"
) as connection:    

    mycursor = connection.cursor(dictionary=True, buffered=True)

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("Johnnnnnnn", "Highway 2112121")
    mycursor.execute(sql, val)

    connection.commit()

    print(mycursor.rowcount, "record inserted.")
    mycursor.execute("SELECT * FROM customers")

    #myresult = mycursor.fetchall()

    #for x in myresult:
     #   print(x)

    for row in mycursor:
        print(row['name'],row['address'])
    