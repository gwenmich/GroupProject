import pygame
from map_config import *

# Initializing
pygame.init()

# Game window settings
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# setting the title on game window
pygame.display.set_caption("Thesis Quest")
# setting icon on game window
game_icon = pygame.image.load('map_assets/school_2.png')
pygame.display.set_icon(game_icon)


# loading building, grass and wall images and scaling them
# size in map_config file
building_image_1 = pygame.image.load('map_assets/police-station.png')
building_image_1 = pygame.transform.scale(building_image_1, (BUILDING_SIZE, BUILDING_SIZE))

building_image_2 = pygame.image.load('map_assets/royal-palace.png')
building_image_2 = pygame.transform.scale(building_image_2, (BUILDING_SIZE, BUILDING_SIZE))

building_image_3 = pygame.image.load('map_assets/school.png')
building_image_3 = pygame.transform.scale(building_image_3, (BUILDING_SIZE, BUILDING_SIZE))

building_image_4 = pygame.image.load('map_assets/apartment.png')
building_image_4 = pygame.transform.scale(building_image_4, (BUILDING_SIZE, BUILDING_SIZE))

building_image_5 = pygame.image.load('map_assets/museum.png')
building_image_5 = pygame.transform.scale(building_image_5, (BUILDING_SIZE, BUILDING_SIZE))

grass_image = pygame.image.load('map_assets/grass.png')
grass_image = pygame.transform.scale(grass_image, (GRASS_SIZE, GRASS_SIZE))

tree_image_1 = pygame.image.load('map_assets/sakura.png')
tree_image_1 = pygame.transform.scale(tree_image_1, (TREE_SIZE, TREE_SIZE))

tree_image_2 = pygame.image.load('map_assets/tree.png')
tree_image_2 = pygame.transform.scale(tree_image_2, (TREE_SIZE, TREE_SIZE))

bench_image = pygame.image.load('map_assets/bench.png')
bench_image = pygame.transform.scale(bench_image, (BENCH_SIZE, BENCH_SIZE))

wall_image = pygame.image.load('map_assets/wall_1.png')
wall_image = pygame.transform.scale(wall_image, (WALL_SIZE, WALL_SIZE))


# tile map dict to shorten map drawing logic
tile_images = {
    'W': wall_image,
    'A': building_image_1,
    'B': building_image_3,
    'C': building_image_2,
    'D': building_image_4,
    'E': building_image_5,
    'G': grass_image,
    'T': tree_image_2,
    'S': tree_image_1,
    'F': bench_image,
}


# drawing tile map
def draw_tile_map():
    for y, row in enumerate(TILE_MAP):
        for x, tile in enumerate(row):
            if tile in tile_images:
                screen.blit(tile_images[tile], (x * TILE_SIZE, y * TILE_SIZE))


hitboxes = [
    pygame.Rect(205, 85, 85, 85),  # Building A
    pygame.Rect(205, 525, 85, 50),  # Building E
    pygame.Rect(485, 296, 85, 60),  # Building B
    pygame.Rect(540, 270, 1, 1) , # Minibox for flag on Building B
    pygame.Rect(745, 140, 80, 45),  # Building C
    pygame.Rect(785, 110, 1, 1),  # Minibox for Top of Building C
    pygame.Rect(810, 465, 70, 85),  # Building D
]

