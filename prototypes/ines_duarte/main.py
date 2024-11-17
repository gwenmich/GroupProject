import pygame
import sys
from map_config import *
from map_creation import *

# Initializing pygame!
pygame.init()


def game_lopp():
    # setting running to True for game loop
    running = True
    # game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.fill((0, 200, 110))
        draw_tile_map()

        # remember to update the screen
        pygame.display.flip()


    pygame.quit()
    sys.exit()



game_lopp()