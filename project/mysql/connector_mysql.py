import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='SkripsiKu',
                                         user='root',
                                         password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connection to MYSQL Server version", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print('Connected to database : ', record)

except Error as e:
    print('Error while Connecting to MYSQL', e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print('MYSQL connection is closed')