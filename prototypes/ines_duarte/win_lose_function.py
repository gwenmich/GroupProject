from prototypes.gwen_michailidis.bars_classes import stress_bar, games_bar
from prototypes.gwen_michailidis.timer import timer


# to implement in main game file
initial_time = 1800
timer = Timer(initial_time)

# this will go in the game loop after countdown and where it will be continuously checked
# it takes the final player time as a variable
def win_lose(initial_time):
    # indicating we are referring to the global game_state
    global game_state
    # check win condition and updates game state to trigger menu
    if games_bar.wins == 4:
        game_state = "Victory"
        if stress_bar.stress == 0 and timer.time_limit <= initial_time / 2:
            print("WOW that's a perfect victory! Five stars!")
        elif timer.time_limit <= initial_time / 2:
            print("That's really impressive! Four stars!")
        else:
            print("Nice one! Three stars!")
    # check for losing condition calling the variables from stress and timer classes
    elif stress_bar.stress == stress_bar.max_stress or timer.time_limit <= 0:
        game_state = "Game Over"
        print("You lost, better luck next time?")



