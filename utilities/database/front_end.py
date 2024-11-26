import requests
# we need json to format the data payloads
import json
from utilities.database.db_utils import get_high_scores


# GET METHOD ########################################################

# Function to make a GET request to the API for top 10 high scores
def get_top10_scores_front_end():
    # storing the http endpoint in a variable to pass it to requests.get
    endpoint = "http://127.0.0.1:5000/scores"
    # using .json to format the response, converting it into a python dictionary
    result = requests.get(endpoint).json()
    return result
#
#
#
# # POST METHOD ########################################################
#
# Function to make a POST request to the API to add a new spell to db
def add_new_score(user_name: str, game_final_time: str, game_score: str):
    # stored route in variable 'endpoint' for reusability
    endpoint = "http://127.0.0.1:5000/scores/add"
    # created a dictionary to structure de information being passed as argument in key value pairs to make it more
    # clear when its send as a json
    spell_details = {
        "user_name": user_name,
        "game_final_time": game_final_time,
        "game_score": game_score
    }

    # we need a header to tell the server how to correctly interpreter the data.
    # In this case we specify contents will be in json format
    headers = {
        'Content-Type': 'application/json'
    }

    # storing the actual POST request in variable result to be returned
    # passing the header and data type as well as json.dumps.
    # json.dumps specifies the dictionary that is being converted to a string as the POST method requires a string
    result = requests.post(endpoint, headers=headers, data=json.dumps(spell_details))
    return result



def iterate_my_stuff(func):
    for i in func:
        print(i)

def run():
    print('Here are you scores')
    print(get_high_scores())


if __name__ == "__main__":
    run()
