import requests
# we need json to format the data payloads
import json
from bonus_dice_roller import (character_scores_dice_roller, admin_options, player_options, iterate_my_stuff,
                               dictionary_formating)


# this is the client end, used to make the request and return the results to the user.
# The syntax is identical to the one used when we did the python assignment using and existing API

# GET METHOD ########################################################


# CLASSES
# Function to make a GET request to the API for all classes
def get_all_classes_front_end():
    # storing the http endpoint in a variable to pass it to requests.get
    endpoint = "http://127.0.0.1:5000/classes"
    # using .json to format the response, converting it into a python dictionary
    result = requests.get(endpoint).json()
    return result


# Function to make a GET request to the API for class with a given name
# similar to previous function but here we use an f string to pass the argument 'name'
def get_class_by_name_front_end(name: str):
    endpoint = f"http://127.0.0.1:5000/classes/{name}"
    result = requests.get(endpoint).json()
    return result


# ARCHETYPES
# Function to make a GET request to the API for all class archetypes
def get_all_archetypes_front_end():
    endpoint = "http://127.0.0.1:5000/archetypes"
    result = requests.get(endpoint).json()
    return result


# Function to make a GET request to the API to get all Archetypes for the class name given as argument
def get_archetypes_by_class_front_end(name: str):
    endpoint = f"http://127.0.0.1:5000/archetypes/name/{name}"
    result = requests.get(endpoint).json()
    return result


# SPELLS
# Function to make a GET request to the API for all spells
def get_all_spells_front_end():
    endpoint = "http://127.0.0.1:5000/spells"
    result = requests.get(endpoint).json()
    return result


# Function to make a GET request to the APO to get a spell by name
def get_spells_by_name_front_end(name: str):
    endpoint = f"http://127.0.0.1:5000/spells/name/{name}"
    result = requests.get(endpoint).json()
    return result
# POST METHOD ########################################################

# Function to make a POST request to the API to add a new spell to db
def add_new_spell_to_list(spell_name: str, school_of_magic: str, spell_range: str, spell_level: int,
                  casting_time: str, spell_description: str):
    # stored route in variable 'endpoint' for reusability
    endpoint = "http://127.0.0.1:5000/spells/add"
    # created a dictionary to structure de information being passed as argument in key value pairs to make it more
    # clear when its send as a json
    spell_details = {
        "spell_name": spell_name,
        "school_of_magic": school_of_magic,
        "spell_range": spell_range,
        "spell_level": spell_level,
        "casting_time": casting_time,
        "spell_description": spell_description
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


# Function to make a POST request to the API to add a new race to db
# Similar syntax to previous function
def add_new_race_to_list(race_name: str, size: str, speed: str, ability_bonus_2: str, ability_bonus_1: str,
                 darkvision: bool, trained_skill: str):
    endpoint = "http://127.0.0.1:5000/races/add"
    race_details = {
        "race_name": race_name,
        "size": size,
        "speed": speed,
        "ability_bonus_2": ability_bonus_2,
        "ability_bonus_1": ability_bonus_1,
        "darkvision": darkvision,
        "trained_skill": trained_skill
    }

    headers = {
        'Content-Type': 'application/json'  # Minimum header required
    }

    result = requests.post(endpoint, headers=headers, data=json.dumps(race_details))  # Use json instead of data
    return result


# DELETE METHOD ########################################################

# SPELLS
# Function to make a DELETE request to the API to delete an existing spell from db
# in this case it takes and int as argument to and passes to the ID to the server side
def delete_spell_front_end(spell_id: int):
    endpoint = f"http://127.0.0.1:5000/spells/remove/{spell_id}"
    # instead of request.get we use .delete to specify the type of request and the endpoint we are sending it to
    result = requests.delete(endpoint)
    return result