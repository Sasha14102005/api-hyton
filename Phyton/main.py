from mysql.connector import connect, Error

def insert(conn):
    print("Вставка данных")
    query="INSERT INTO lists (name) VALUES (\"Продукты\")"  
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()

def delete(conn):
    print("Вставка данных")
    query="DELETE INTO lists (name) VALUES (\"Продукты\")"  
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()



try:
    with connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="root",
        database="todo"
    ) as connection:
        print(connection)
        #insert(connection)
        delete(connection)

except Error as e:
    print(e)

