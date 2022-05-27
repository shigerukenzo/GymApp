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
            c = self.conn.cursor()
            c.execute(table)
        except Error as e:
            print(e)

    def create_connection(self):
        """ create a database connection to a SQLite database """
        try:
            conn = sqlite3.connect(self._path)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if self._conn:
                self._conn.close()

    def close(self):
        self._conn.close()