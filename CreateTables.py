

def get_create_tables_query():
    member_table = """ CREATE TABLE IF NOT EXISTS member (
                                MemberID integer PRIMARY KEY,
                                firstName text NOT NULL,
                                lastName text NOT NULL,
                                startDate text NOT NULL,
                                email text NOT NULL,
                                password text NOT NULL
                            ); """

    memberExcercise_table = """CREATE TABLE IF NOT EXISTS memberExercise (
                                    FOREIGN KEY (ExerciseID),
                                    FOREIGN KEY (SetID),
                                    FOREIGN KEY (MemberID),
                                    PRIMARY KEY (ExerciseID, SetID, MemberID)
                                );"""
    set_table = """ CREATE TABLE IF NOT EXISTS set (
                                set integer PRIMARY KEY,
                                reps integer NOT NULL,
                                success integer NOT NULL
                            ); """