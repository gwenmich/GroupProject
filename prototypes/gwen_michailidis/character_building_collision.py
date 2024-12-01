# for when character collides with buildings
from character_movement import *
from mini_games import mini_game

# buildings' sizes and coordinates on map
library = pygame.Rect(230, 540, 35, 40)
cafeteria = pygame.Rect(850, 525, 40, 40)
counselling_office = pygame.Rect(510, 327, 35, 40)
classroom = pygame.Rect(760, 183, 50, 40)
it_dept = pygame.Rect(230, 150, 35, 40)



def enter_building():
    """
    if the character collides with a building and hasn't won that challenge will call the building's mini-game
    """
    games_won = {
        "library": "Not won",
        "cafeteria": "Not won",
        "counselling_office": "Not won",
        "classroom": "Not won",
        "it_dept": "Not won"
    }

    for building, building_rect in games_won.items():
        if character_rect.colliderect(building_rect):
            if building == "counselling_office" or games_won[building] == "Not won":
                mini_game(building)
            else:
                print("Sorry, you've already won this game, time to visit another building!")





