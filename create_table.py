# Creating Sample Table

from mysql.connector import connection, Error, errorcode

try:
    print("Connecting To Database")
    con = connection.MySQLConnection(user='root', password='root', host='localhost', database='mek')

    TABLES = {'employees': (
        "CREATE TABLE `employees` ("
        "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
        "  `birth_date` date NOT NULL,"
        "  `first_name` varchar(14) NOT NULL,"
        "  `last_name` varchar(16) NOT NULL,"
        "  `gender` enum('M','F') NOT NULL,"
        "  `hire_date` date NOT NULL,"
        "  PRIMARY KEY (`emp_no`)"
        ") ENGINE=InnoDB"), 'departments': (
        "CREATE TABLE `departments` ("
        "  `dept_no` char(4) NOT NULL,"
        "  `dept_name` varchar(40) NOT NULL,"
        "  PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)"
        ") ENGINE=InnoDB"), 'salaries': (
        "CREATE TABLE `salaries` ("
        "  `emp_no` int(11) NOT NULL,"
        "  `salary` int(11) NOT NULL,"
        "  `from_date` date NOT NULL,"
        "  `to_date` date NOT NULL,"
        "  PRIMARY KEY (`emp_no`,`from_date`), KEY `emp_no` (`emp_no`),"
        "  CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`emp_no`) "
        "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
        ") ENGINE=InnoDB"), 'dept_emp': (
        "CREATE TABLE `dept_emp` ("
        "  `emp_no` int(11) NOT NULL,"
        "  `dept_no` char(4) NOT NULL,"
        "  `from_date` date NOT NULL,"
        "  `to_date` date NOT NULL,"
        "  PRIMARY KEY (`emp_no`,`dept_no`), KEY `emp_no` (`emp_no`),"
        "  KEY `dept_no` (`dept_no`),"
        "  CONSTRAINT `dept_emp_ibfk_1` FOREIGN KEY (`emp_no`) "
        "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
        "  CONSTRAINT `dept_emp_ibfk_2` FOREIGN KEY (`dept_no`) "
        "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
        ") ENGINE=InnoDB"), 'dept_manager': (
        "  CREATE TABLE `dept_manager` ("
        "  `dept_no` char(4) NOT NULL,"
        "  `emp_no` int(11) NOT NULL,"
        "  `from_date` date NOT NULL,"
        "  `to_date` date NOT NULL,"
        "  PRIMARY KEY (`emp_no`,`dept_no`),"
        "  KEY `emp_no` (`emp_no`),"
        "  KEY `dept_no` (`dept_no`),"
        "  CONSTRAINT `dept_manager_ibfk_1` FOREIGN KEY (`emp_no`) "
        "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
        "  CONSTRAINT `dept_manager_ibfk_2` FOREIGN KEY (`dept_no`) "
        "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
        ") ENGINE=InnoDB"), 'titles': (
        "CREATE TABLE `titles` ("
        "  `emp_no` int(11) NOT NULL,"
        "  `title` varchar(50) NOT NULL,"
        "  `from_date` date NOT NULL,"
        "  `to_date` date DEFAULT NULL,"
        "  PRIMARY KEY (`emp_no`,`title`,`from_date`), KEY `emp_no` (`emp_no`),"
        "  CONSTRAINT `titles_ibfk_1` FOREIGN KEY (`emp_no`)"
        "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
        ") ENGINE=InnoDB")}

    curs = con.cursor()

    for table_name in TABLES:
        t_query = TABLES[table_name]
        try:
            print("Creating Table {}".format(table_name))
            curs.execute(t_query)
        except Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Already exists.")
            else:
                print(err.msg)
        else:
            print("Created !")

except Exception as e:
    print("Error: ", str(e))

con.commit()
con.close()