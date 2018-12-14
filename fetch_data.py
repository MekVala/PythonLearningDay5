# Fetching Data From Employee Table

from mysql.connector import connection,Error
import datetime

try:
    print("Connecting To Database")
    con = connection.MySQLConnection(user='root', password='root', host='localhost', database='mek')
    print("Connected !")
except Error as err:
    print("Error Connecting Database: {}".format(str(err)))
    exit()

cur = con.cursor()
q = "Select first_name,last_name,hire_date from employees WHERE hire_date BETWEEN %s AND %s"

start = datetime.date(1999, 1, 1)
end = datetime.date(9999, 12, 31)

try:
    print("Fetching Data From Employee Table !")
    cur.execute(q,(start,end))
except Error as err:
    print("Error Fetching Record: {}".format(str(err)))
    exit()
else:
    print("Data :")
    for (first_name, last_name, hire_date) in cur:
        print("{}, {} was hired on {:%d %b %Y}".format(last_name, first_name, hire_date))

cur.close()
con.close()
