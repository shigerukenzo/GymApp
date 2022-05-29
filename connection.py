import sqlite3
from sqlite3 import Error


class Database:
    def __init__(self):
        self._path = r"\sqlite\db\pythonsqlite.db"
        self._conn = None

    def create_table(self, table):
        """ create a table from the create_table_sql statement
        :param table: a CREATE TABLE statement
        :return:
        """
        try:
            c = self._conn.cursor()
            c.execute(table)
        except Error as e:
            print(e)

    def print_schema(self):
        cursor = self._conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(cursor.fetchall())

    def create_connection(self):
        """ create a database connection to a SQLite database """
        try:
            self._conn = sqlite3.connect(self._path)
            print(sqlite3.version)
        except Error as e:
            print(e)

    def close(self):
        self._conn.close()