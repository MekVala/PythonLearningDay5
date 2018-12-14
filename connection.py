from mysql.connector import connection

try:
    print("Connecting")
    con = connection.MySQLConnection(user='root', password='root',
                                     host='localhost',
                                     database='mek')
    print("Connected")
except Exception as e:
    print("Error: ", str(e))

