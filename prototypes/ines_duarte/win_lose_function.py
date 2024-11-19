import pygame
from prototypes.emma_begum.menu_map.menu import *
from prototypes.gwen_michailidis.bars_classes import stress_bar, games_bar
from prototypes.gwen_michailidis.timer import timer

pygame.init()

# this will go in the game loop after countdown and where it will be continuously checked
# it takes the final player time as a variable
def win_lose(elapsed_time):
    # indicating we are refering to the global game_state
    global game_state
    # check win condution and updates game state to trigger menu
    if games_bar.wins == 4:
        game_state = "Victory"
        if stress_bar.stress == stress_bar.max_stress and elapsed_time < timer.time_limit / 2:
            print("WOW that's a perfect victory! Five stars!")
        elif elapsed_time < timer.time_limit / 2:
            print("That's really impressive! Four stars!")
        else:
            print("Nice one! Three stars!")
    # check for losing condition calling the varibales from stree and timer classes
    elif stress_bar.stress == 100 or elapsed_time > timer.time_limit:
        game_state = "Game Over"
        print("You lost, better luck next time?")
