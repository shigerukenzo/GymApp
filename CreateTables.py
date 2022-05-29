

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

    exercise_table = """ CREATE TABLE IF NOT EXISTS Exercise (
                                exerciseID integer PRIMARY KEY,
                                FOREIGN KEY (muscleGroupID),
                                exerciseName text NOT NULL
                            ); """

    exerciseMuscleGroup_table = """ CREATE TABLE IF NOT EXISTS ExerciseMuscleGroup (
                                FOREIGN KEY (ExerciseID),
                                FOREIGN KEY (muscleGroupID)
                            ); """

    muscleGroup_table = """ CREATE TABLE IF NOT EXISTS MuscleGroup (
                                muscleGroupID integer PRIMARY KEY,
                                muscleGroupName text NOT NULL
                            ); """

    muscle_table = """ CREATE TABLE IF NOT EXISTS Muscle (
                                muscleID integer PRIMARY KEY,
                                FOREIGN KEY (muscleGroupID),
                                muscleName text NOT NULL
                            ); """

    return member_table, memberExcercise_table, exercise_table, exerciseMuscleGroup_table, muscleGroup_table, muscle_table, set_table
