from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="root",
        password="P$kbYYgC?xXX83rF336R9@QPz7"
    ) as connection:
        create_db_query = "CREATE DATABASE online_movie_rating"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
except Error as e:
    print(e)