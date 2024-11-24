# from flask we import the necessary dependencies to perform requests and handle json
from flask import Flask, jsonify, request
# from the file db_utils we import all the functions we created to be associated with the routes
# to create the functionality
from db_utils import get_high_scores


# passing __name__ to the variable app is necessary to set up the route paths for the API. This will tell our program
# to actually run flask
app = Flask(__name__)


# GET METHOD ########################################################

# route to fetch all classes using GET Method
@app.route("/scores", methods=["GET"])
def get_top10_scores():
    # print(jsonify("TESTING ENDPOINT"))
    # I'm keeping the testing endpoint in case it becames necessary for testing and debugging,
    # to help verify if the route is working, I'll just keep it commented out
    # jsonify will convert the python data into json format which is essential for the flask app
    # passing the function created in bd_utils to add the functionality to this route by assigning it a query
    return jsonify(get_high_scores())





#
# # POST METHOD ########################################################
# # the post method is used to add new data to your db via the api request
#
# # this a route to add a new race, changed method to POST
# @app.route("/races/add", methods=["POST"])
# def add_race():
#     # the tricky part of this route is that it need to take several arguments to pass them to the db query
#     # get_json extracts the json data from the request made to the endpoint above and stores it in the
#     # variable data as python dictionary
#     data = request.get_json()
#     # from the variable data that contains the details to be passed to the query we pull the individual arguments
#     # associated with a particular keu using .get and store them in variables
#     race_name = data.get('race_name')
#     size = data.get('size')
#     speed = data.get('speed')
#     ability_bonus_2 = data.get('ability_bonus_2')
#     ability_bonus_1 = data.get('ability_bonus_1')
#     darkvision = data.get('darkvision')
#     trained_skill = data.get('trained_skill')
#
#     # Call the function with the arguments retrieved via .get
#     return jsonify(add_new_race(race_name, size, speed, ability_bonus_2, ability_bonus_1, darkvision, trained_skill))
#     # using jsonify to ensure tit formated properly
#
#
# # this route work similarly to add_race, only it allows user to add a spell
# @app.route("/spells/add", methods=["POST"])
# def add_spell():
#     data = request.get_json()
#
#     spell_name = data.get('spell_name')
#     school_of_magic = data.get('school_of_magic')
#     spell_range = data.get('spell_range')
#     spell_level = data.get('spell_level')
#     casting_time = data.get('casting_time')
#     spell_description = data.get('spell_description')
#
#     return jsonify(add_new_spell(spell_name, school_of_magic, spell_range, spell_level,
#                                  casting_time, spell_description))
#
#
# # DELETE METHOD ########################################################
# # this route serves to remove a spell by its ID(to showcase some variety)
# # which is added directly to the route and uses the DELETE Method
# @app.route("/spells/remove/<int:spell_id>", methods=["DELETE"])
# def remove_spell(spell_id):
#     # having only one argument we don't need to convert the json object to a dict and pull individual values.
#     # the value can be passed directly to the db query function
#     return jsonify(delete_spell_by_id(spell_id))
#

# again using __main__ to limit the scope of what will run when the script is run directly
if __name__ == "__main__":
    # in this case app.run will start the flask application and also enable debugger as it's set to True
    app.run(debug=True)
