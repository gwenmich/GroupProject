import pygame
from config import *
from character_building_collision import enter_building

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Character movement")
clock = pygame.time.Clock()

dt = 0

# position player in the centre of the screen
player_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# load main character image and get its rectangle
character = pygame.image.load('girl64.png').convert_alpha()
x = character.get_width()
y = character.get_height()



running = True

while running:

    # framerate in seconds - the time difference between two frames
    dt = clock.tick(FPS) / 1000

    # background screen colour - to change with map
    screen.fill((58, 179, 66))

    # position character's rect in the centre of the screen
    character_rect = character.get_rect(center=player_position)

    # adding character image to centre of screen
    screen.blit(character, character_rect)


    # get status of keys on keyboard
    keyboard = pygame.key.get_pressed()

    # movement of character
    if keyboard[pygame.K_UP] and character_rect.y > 0:
        player_position.y -= 250 * dt
    if keyboard[pygame.K_DOWN] and character_rect.y < SCREEN_HEIGHT - y:
        player_position.y += 250 * dt
    if keyboard[pygame.K_LEFT] and character_rect.x > 0:
        player_position.x -= 250 * dt
    if keyboard[pygame.K_RIGHT] and character_rect.x < SCREEN_WIDTH - x:
        player_position.x += 250 * dt


    # triggers building's mini game when character collides with it
    enter_building()


    # exit the game by clicking x or pressing esc key
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False


    # update screen
    pygame.display.flip()



pygame.quit()