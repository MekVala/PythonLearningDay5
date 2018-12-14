# Testing Connection

from mysql.connector import connection,Error

try:
    print("Connecting To Database")
    con = connection.MySQLConnection(user='root', password='root', host='localhost', database='mek')
    print("Connected !")
    con.close()
except Error as err:
    print("Error Connecting Database: {}".format(str(err)))
