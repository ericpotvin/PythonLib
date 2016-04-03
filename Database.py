"""
Database module

Database Class [ Database.py ]

@author      Eric Potvin
@package     PythonLib
@subpackage  Database
@link        https://github.com/ericpotvin/PythonLib
"""
import sqlite3


class Database(object):
    """ Database module class (sqlite3)
    """
    DATABASE_EXT = ".db"

    END_SQL = ";"
    FILE_SQL_EXT = ".sql"
    FILE_SQL_NAME = "insert"

    SQL_FIELD_SEPARATOR = "_"
    SQL_DELIMITER = ", "
    SQL_PRIMARY_KEY = "id"
    SQL_FOREIGN_KEY_PREFIX = "fk_"
    SQL_FOREIGN_KEY_SUFFIX = "_id"

    filename = None
    database = None

    def __init__(self, filename):
        """ Init
            :param filename: The sqlite3 filename
        """
        self.filename = filename
        self.database = sqlite3.connect(filename)

    def create_table(self, table, fields):
        """ Create the table
        """

        sql = "CREATE TABLE IF NOT EXISTS %s (" % table
        glue = ""

        for (_key, _type) in fields.items():
            if _key == Database.SQL_PRIMARY_KEY:
                _type = "INT PRIMARY KEY"
            elif _key[:3] != Database.SQL_FOREIGN_KEY_PREFIX:
                _type += " NOT NULL"

            sql += "%s %s %s" % (glue, _key, _type)
            glue = ", "

        sql += " );"

        try:
            self.database.execute(sql)
        except Exception as e:
            print e

    def insert(self, table, data, fk_id=None):
        """ Add a record
            :param table: The table name
            :param data: The data to insert
            :param fk_id: foreign_key
            :return integer (primary key id)
        """

        sql_insert = "INSERT INTO %s (%s) VALUES (%s)"

        if not fk_id:
            next_id = self._get_next_id(table)
            columns, mapped, values = self._build_params(data, next_id)

            sql = sql_insert % (table, ', '.join(columns), ', '.join(mapped))

            return self._execute_insert(sql, tuple(values))

        for _key in data:
            next_id = self._get_next_id(table)
            columns, mapped, values = self._build_params(data[_key], next_id)

            sql = sql_insert % (table, ', '.join(columns), ', '.join(mapped))

            self._execute_insert(sql, tuple(values))

    def _execute_insert(self, sql, values):

        cursor = self.database.cursor()

        try:
            cursor.execute(sql, values)
            self.database.commit()
        except Exception as e:
            print e

        return cursor.lastrowid

    def close(self):
        self.database.close()

    @staticmethod
    def _build_params(data, next_id):

        columns = []
        mapped = []
        values = []

        # add the ID
        columns.append(Database.SQL_PRIMARY_KEY)
        mapped.append("?")
        values.append(next_id)

        for field in data:
            column = str(field).encode("utf8")
            columns.append(column)

            mapped.append("?")

            text = str(data[field]).encode("utf8")
            values.append(text)

        return columns, mapped, values

    def _get_next_id(self, table):

        _id = 1
        cursor = self.database.cursor()

        query = "SELECT MAX(" + Database.SQL_PRIMARY_KEY + ") + 1 AS next " + \
                " FROM " + table

        try:
            cursor.execute(query)
        except Exception as e:
            print e

        if not cursor:
            return _id

        result = cursor.fetchone()

        if not result[0]:
            return _id

        return result[0]

"""



print "Table created successfully";

conn.close()

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.commit()
print "Records created successfully";
conn.close()


import sqlite3

conn = sqlite3.connect('test.db')
print "Opened database successfully";

cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"

print "Operation done successfully";
conn.close()
"""