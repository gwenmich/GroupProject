import pygame
import sys
from map_config import *
from map_creation import *


# Initializing pygame!
pygame.init()

clock = pygame.time.Clock()

dt = 0

# position player in the centre of the screen
player_position = pygame.Vector2(530, 410)

# load main character image and get its rectangle
character = pygame.image.load('girl64.png').convert_alpha()
x = character.get_width()
y = character.get_height()



def game_lopp():
    # setting running to True for game loop
    running = True

    # game loop
    while running:

        # framerate in seconds - the time difference between two frames
        dt = clock.tick(FPS) / 1000

        # position character's rect in the centre of the screen
        character_rect = character.get_rect(center=player_position)

        screen.fill((0, 200, 110))
        draw_tile_map()
        # adding character image to centre of screen
        screen.blit(character, character_rect)

        # get status of keys on keyboard
        keyboard = pygame.key.get_pressed()

        # movement of character
        if keyboard[pygame.K_UP] and character_rect.y > 10:
            player_position.y -= 250 * dt
        if keyboard[pygame.K_DOWN] and character_rect.y < SCREEN_HEIGHT - 80:
            player_position.y += 250 * dt
        if keyboard[pygame.K_LEFT] and character_rect.x > 0:
            player_position.x -= 250 * dt
        if keyboard[pygame.K_RIGHT] and character_rect.x < SCREEN_WIDTH - x:
            player_position.x += 250 * dt



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False


        # remember to update the screen
        pygame.display.flip()


    pygame.quit()
    sys.exit()



game_lopp()