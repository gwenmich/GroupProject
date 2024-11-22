import pygame
from prototypes.ines_duarte.map.map_config import *

# Initializing
pygame.init()

# Game window settings
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# setting the title on game window
pygame.display.set_caption("Thesis Quest")
# setting icon on game window
game_icon = pygame.image.load('map/map_assets/school_2.png')
pygame.display.set_icon(game_icon)


# loading building, grass and wall images and scaling them
# size in map_config file
building_image_1 = pygame.image.load('map/map_assets/police-station.png')
building_image_1 = pygame.transform.scale(building_image_1, (BUILDING_SIZE, BUILDING_SIZE))

building_image_2 = pygame.image.load('map/map_assets/royal-palace.png')
building_image_2 = pygame.transform.scale(building_image_2, (BUILDING_SIZE, BUILDING_SIZE))

building_image_3 = pygame.image.load('map/map_assets/school.png')
building_image_3 = pygame.transform.scale(building_image_3, (BUILDING_SIZE, BUILDING_SIZE))

building_image_4 = pygame.image.load('map/map_assets/apartment.png')
building_image_4 = pygame.transform.scale(building_image_4, (BUILDING_SIZE, BUILDING_SIZE))

building_image_5 = pygame.image.load('map/map_assets/museum.png')
building_image_5 = pygame.transform.scale(building_image_5, (BUILDING_SIZE, BUILDING_SIZE))

grass_image = pygame.image.load('map/map_assets/grass.png')
grass_image = pygame.transform.scale(grass_image, (GRASS_SIZE, GRASS_SIZE))

tree_image_1 = pygame.image.load('map/map_assets/sakura.png')
tree_image_1 = pygame.transform.scale(tree_image_1, (TREE_SIZE, TREE_SIZE))

tree_image_2 = pygame.image.load('map/map_assets/tree.png')
tree_image_2 = pygame.transform.scale(tree_image_2, (TREE_SIZE, TREE_SIZE))

bench_image = pygame.image.load('map/map_assets/bench.png')
bench_image = pygame.transform.scale(bench_image, (BENCH_SIZE, BENCH_SIZE))

wall_image = pygame.image.load('map/map_assets/wall_1.png')
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


# IT dept hitboxes
it_dept_A_1 = pygame.Rect(185, 80, 120, 95)
it_dept_A_2 = pygame.Rect(185, 170, 40, 40)
it_dept_A_3 = pygame.Rect(270, 170, 35, 40)
# library hitboxes
library_B_1 = pygame.Rect(190, 525, 110, 40)
library_B_2 = pygame.Rect(180, 560, 40, 50)
library_B_3 = pygame.Rect(270, 560, 40, 50)
# councelling office hir=tboxes
counselling_office_1 = pygame.Rect(465, 300, 120, 50)
counselling_office_2 = pygame.Rect(465, 330, 38, 50)
counselling_office_3 = pygame.Rect(550, 330, 38, 50)
counselling_office_4 = pygame.Rect(520, 265, 25, 30)
# classroom
classroom_1 = pygame.Rect(725, 140, 120, 60)
classroom_2 = pygame.Rect(725, 210, 30, 20)
classroom_3 = pygame.Rect(815, 210, 30, 20)
classroom_4 = pygame.Rect(773, 103, 25, 40)
# cafeteria hitboxes
cafeteria_1 = pygame.Rect(797, 462, 97, 90)
cafeteria_2 = pygame.Rect(797, 540, 60, 50)


hitboxes = {
    "it_dept_1": it_dept_A_1,
    "it_dept_2": it_dept_A_2,
    "it_dept_3": it_dept_A_3,
    "library_1": library_B_1,
    "library_2": library_B_2,
    "library_3": library_B_3,
    "counselling_office_1": counselling_office_1,
    "counselling_office_2": counselling_office_2,
    "counselling_office_3": counselling_office_3,
    "counselling_office_4": counselling_office_4,
    "classroom_1": classroom_1,
    "classroom_2": classroom_2,
    "classroom_3": classroom_3,
    "classroom_4": classroom_4,
    "cafeteria_1": cafeteria_1,
    "cafeteria_2": cafeteria_2
}
