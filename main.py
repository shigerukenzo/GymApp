import sqlite3
from sqlite3 import Error


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
    database = r"\sqlite\db\pythonsqlite.db"

    sql_create_member_table = """ CREATE TABLE IF NOT EXISTS member (
                                        MemberID integer PRIMARY KEY,
                                        firstName text NOT NULL,
                                        lastName text NOT NULL,
                                        startDate text NOT NULL
                                    ); """

    sql_create_memberExcercise_table = """CREATE TABLE IF NOT EXISTS memberExercise (
                                    FOREIGN KEY (ExerciseID),
                                    FOREIGN KEY (SetID),
                                    FOREIGN KEY (MemberID),
                                    PRIMARY KEY (ExerciseID, SetID, MemberID)
                                );"""

    sql_create_exercise_table = """ CREATE TABLE IF NOT EXISTS Exercise (
                                        ExerciseID integer PRIMARY KEY,
                                        firstName text NOT NULL,
                                        lastName text NOT NULL,
                                        startDate text NOT NULL
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)

        # create tasks table
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"\sqlite\db\pythonsqlite.db")
