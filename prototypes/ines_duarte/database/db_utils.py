# importing the module mysql.connector to connect to the sql database
import mysql.connector
# importing the variables that hold the sensitive data from the config file
from database_config import USER, PASSWORD, HOST, DATABASE


# defining a custom exception to allow better error handling.
# this will be used in the function bellow
class DbConnectionError(Exception):
    pass


# SQL connector that contains the necessary credentials to connect to the sql server and query the database.
# Sensitive data is stored in variables imported from config file
def _connect_to_db():
    cnx = mysql.connector.connect(
        #  passing the credentials to establish connection to database
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=DATABASE
    )
    return cnx



def get_high_scores():
    # using try and except block to handle exceptions. If and error is found in the try block,
    # instead of program breaking down, it moves to run the except block
    try:
        # calling database connecting function and storing it in variable db_connection
        db_connection = _connect_to_db()
        # cursor is a object used to interact with the SQL database, working as a pointer to navigate
        cur = db_connection.cursor()
        # informative text to let you know code got to this point
        print("Connected to DB: %s" % DATABASE)

        query = """SELECT sc.game_score, pl.user_name
                    FROM scores sc
                    JOIN players pl ON sc.player_id = pl.player_id
                    ORDER BY pl.user_name ASC
                    LIMIT 10;"""

        # aptly named, execute is used to...you guessed it, execute the query
        cur.execute(query)
        # fetchall is used to return all the rows
        result = cur.fetchall()
        # creating a list to return the results as well as the corresponding keys keys
        scores_list = []
        # using a for loop to iterate through the query response, using the index to
        # match the values to the correct keys
        for i in result:
            scores_info = {
                "Final Time": i[0],
                "Stars": i[1],
                "Player": i[2]
            }
            # appending the dictionary to the class_list
            scores_list.append(scores_info)



        # returns the query result
        return scores_list

    # except block to return the assigned error message. It helps us locate where the error ocurred.
    # In this case it would indicate it was in reading the data
    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    # The finally block always executes, and its being used to check if the cursor and db_connections exist and
    # if so to close them
    finally:
        if cur:
            cur.close()
        if db_connection:
            db_connection.close()
            # prints statement to indicate it was successful
            print("DB connection is closed")