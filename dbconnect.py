import mysql.connector
from mysql.connector import Error

connection = None
cursor = None


def conn():
    global connection
    connection = mysql.connector.connect(host='localhost',
                                         database='pos',
                                         user='root',
                                         password='')

    return connection


def destroyConn():
    connect = conn()
    connect.close()


def getcon():
    connector = conn()

    if obj() is True:
        global cursor
        connector
        return connector
    else:
        print('error')


def obj():
    try:
        connection = conn()

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

            return True

    except Error as e:
        print("Error while connecting to MySQL", e)
        return False


# finally:
# if connection.is_connected():
# cursor.close()
# connection.close()
# print("MySQL connection is closed")
# cst = getcon()
