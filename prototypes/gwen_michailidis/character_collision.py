# for when character collides with buildings
import pygame
from character_movement import *

# buildings' Rects need x, y, width, height to be assigned
library = pygame.Rect()
cafeteria = pygame.Rect()
counselling_office = pygame.Rect()
classroom = pygame.Rect()
it_dept = pygame.Rect()


buildings = {
    "library" : library,
    "cafeteria" : cafeteria,
    "counselling_office" : counselling_office,
    "classroom" : classroom,
    "it_dept" : it_dept
}


for building, building_rect in buildings.items():
    if character.collide