from mysql.connector import connection,cursor

try:
    print("Connecting To Database")
    con = connection.MySQLConnection(user='root', password='root', host='localhost', database='mek')


except Exception as e:
    print("Error: ",str(e))
