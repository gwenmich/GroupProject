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



# drawing tile map
def draw_tile_map():
    for y, row in enumerate(TILE_MAP):
        for x, tile in enumerate(row):
            if tile == 'W':
                screen.blit(wall_image, (x * TILE_SIZE, y * TILE_SIZE))
            elif tile == 'A':
                screen.blit(building_image_1, (x * TILE_SIZE, y * TILE_SIZE))
            elif tile == 'B':
                screen.blit(building_image_3, (x * TILE_SIZE, y * TILE_SIZE))
            elif tile == 'C':
                screen.blit(building_image_2, (x * TILE_SIZE, y * TILE_SIZE))
            elif tile == 'D':
                screen.blit(building_image_4, (x * TILE_SIZE, y * TILE_SIZE))
            elif tile == 'E':
                screen.blit(building_image_5, (x * TILE_SIZE, y * TILE_SIZE))
            elif tile == 'G':
                screen.blit(grass_image, (x * TILE_SIZE, y * TILE_SIZE))
            elif tile == 'T':
                screen.blit(tree_image_2, (x * TILE_SIZE, y * TILE_SIZE))
            elif tile == 'S':
                screen.blit(tree_image_1, (x * TILE_SIZE, y * TILE_SIZE))
            elif tile == 'F':
                screen.blit(bench_image, (x * TILE_SIZE, y * TILE_SIZE))


