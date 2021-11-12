from mysql.connector import connect, Error


with connect(
    host="localhost",
    user="root",
    password="P$kbYYgC?xXX83rF336R9@QPz7"
) as connection:
    show_db_query = "SHOW DATABASES"
    with connection.cursor() as cursor:
        cursor.execute(show_db_query)
        for db in cursor:
            print(db)