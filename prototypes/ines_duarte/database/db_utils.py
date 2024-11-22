# importing the module mysql.connector to connect to the sql database
import mysql.connector
# importing the variables that hold the sensitive data from the config file
from config import USER, PASSWORD, HOST, DATABASE


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



def get_all_classes():
    # using try and except block to handle exceptions. If and error is found in the try block,
    # instead of program breaking down, it moves to run the except block
    try:
        # calling database connecting function and storing it in variable db_connection
        db_connection = _connect_to_db()
        # cursor is a object used to interact with the SQL database, working as a pointer to navigate
        cur = db_connection.cursor()
        # informative text to let you know code got to this point
        print("Connected to DB: %s" % DATABASE)
        # SQL query to get all classes in the database. Using CASE to return TRUE or FALSE in the spellcaster column
        # as it's a BOOLEAN and it would 0 or 1 otherwise. This makes it more user friendly
        # JOINING abilities and and skills table to retrieve the skill and ability names as they show up on
        # classes table only as IDs, and with the join it returns the actual names instead
        query = """SELECT cl.class_id, cl.class_name, ab.ability_name, cl.base_hit_points, cl.hit_dice, sk.skill_name,
                        CASE 
                            WHEN cl.spellcaster = 1 THEN 'true' 
                            ELSE 'false' 
                        END AS is_spellcaster
                    FROM classes cl
                    JOIN abilities ab ON ab.ability_id = cl.key_ability_id
                    JOIN skills sk ON sk.skill_id = cl.trained_skill_id"""
        # aptly named, execute is used to...you guessed it, execute the query
        cur.execute(query)
        # fetchall is used to return all the rows
        result = cur.fetchall()
        # creating a list to return the results as well as the corresponding keys keys
        class_list = []
        # using a for loop to iterate through the query response, using the index to
        # match the values to the correct keys
        for i in result:
            class_info = {
                "class_id": i[0],
                "class_name": i[1],
                "key_ability": i[2],
                "base_hit_points": i[3],
                "hit_dice": i[4],
                "trained_skill": i[5],
                "is_spellcaster": i[6]
            }
            # appending the dictionary to the class_list
            class_list.append(class_info)

        # returns the query result
        return class_list

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

