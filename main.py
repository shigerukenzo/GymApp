import sqlite3
from sqlite3 import Error
from CreateTables import get_create_tables_query
import connection


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    db = connection.Database()
    db.create_connection()
    for table in get_create_tables_query():
        db.create_table(table)

    db.print_schema()



if __name__ == '__main__':
    main()
