import sqlite3
from sqlite3 import Error
from CreateTables import get_create_tables_query
import connection
from dashboard import Member


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

def login(db):
    username = input("Enter Member ID")
    password = hash(input("Enter password"))

    query = f"SELECT * FROM member WHERE memberID = {username} AND password = {password}"
    if db.member_validation(query):
        member = Member()
        member.main()
    return

def signup():
    return

def main():
    db = connection.Database()
    db.create_connection()
    for table in get_create_tables_query():
        db.create_table(table)

    db.print_schema()
    user_in = None
    while user_in is not None or user_in == 3:
        user_in = int(input("Select Option: (Enter number)\n1. Login\n2. Sign up\n3. Exit"))
        if user_in == 1:
            login(db)
        elif user_in == 2:
            signup()

    db.close()



if __name__ == '__main__':
    main()
