# for when character collides with buildings
from character_movement import *
from mini_games import mini_game

# buildings' Rects need x, y, width, height to be assigned
library = pygame.Rect()
cafeteria = pygame.Rect()
counselling_office = pygame.Rect()
classroom = pygame.Rect()
it_dept = pygame.Rect()



def enter_building():
    """
    if the character collides with a building will call the building's mini-game
    """

    buildings = {
        "library" : library,
        "cafeteria" : cafeteria,
        "counselling_office" : counselling_office,
        "classroom" : classroom,
        "it_dept" : it_dept
    }

    for building, building_rect in buildings.items():
        if character_rect.colliderect(building_rect):
            mini_game(building)



