import sqlite3
from sqlite3 import Error


class Database:
    def __init__(self):
        self._path = None
        self._conn = None

    def create_table(self, table):
        """ create a table from the create_table_sql statement
        :param table: a CREATE TABLE statement
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(table)
        except Error as e:
            print(e)