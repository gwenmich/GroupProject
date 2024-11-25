# from flask we import the necessary dependencies to perform requests and handle json
from flask import Flask, jsonify, request
# from the file db_utils we import all the functions we created to be associated with the routes
# to create the functionality
from utilities.database.db_utils import get_high_scores, add_new_score


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


@app.route("/scores/add", methods=["POST"])
def add_high_score():
    data = request.get_json()

    new_user_name = data.get('new_user_name')
    game_final_time = data.get('game_final_time')
    game_score = data.get('game_score')


    return jsonify(add_new_score(new_user_name, game_final_time, game_score))


# again using __main__ to limit the scope of what will run when the script is run directly
if __name__ == "__main__":
    # in this case app.run will start the flask application and also enable debugger as it's set to True
    app.run(debug=True)
