# Inserting Data

from mysql.connector import connection, Error
from datetime import date, datetime, timedelta

try:
    print("Connecting To Database")
    con = connection.MySQLConnection(user='root', password='root', host='localhost', database='mek')
except Error as err:
    print("Error Connecting Database: {}".format(str(err)))

cur = con.cursor()

add_employee = ("INSERT INTO employees(first_name, last_name, hire_date, gender, birth_date) "
                "VALUES (%s, %s, %s, %s, %s)")

data_employee = ('Jarvis', 'Flare', datetime.now().date() - timedelta(days=15), 'M', date(1987, 2, 12))
print("Inserting Record in Employees Table :", end=" ")
try:
    cur.execute(add_employee, data_employee)
    empid = cur.lastrowid
except Error as err:
    print("Error")
else:
    print("Ok ")

add_salary = ("INSERT INTO salaries "
              "(emp_no, salary, from_date, to_date) "
              "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")
data_salary = {'emp_no': empid, 'salary': 50000, 'from_date': datetime.now().date() + timedelta(days=1),
               'to_date': date(9999, 1, 1)}

print("Inserting Record in Salaries Table :", end=" ")
try:
    cur.execute(add_salary, data_salary)
except Error as err:
    print("Error")
else:
    print("Ok ")

con.commit()
con.close()