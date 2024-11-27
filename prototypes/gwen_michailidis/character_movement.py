import pygame
from config import *
from bars_classes import StressBar, GamesBar
from timer import Timer
from spritesheet import SpriteSheet
from character_class import Character
# from character_building_collision import enter_building

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

dt = 0

# position player in the centre of the screen
# player_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
# character_rect = pygame.Rect(player_position.x, player_position.y, 64, 64)




# initialise stress and games bars
stress_bar = StressBar(900, 20, 70, 16, 100)
games_bar = GamesBar(510, 20, 70, 16, 4)

# set timer for 30 minutes -> 1800 seconds
timer = Timer(1800)
# creating timer where a userevent is posted to event queue every 1 second (1000 milliseconds)
pygame.time.set_timer(pygame.USEREVENT, 1000)

# lines 33 - 46 will be going into a function or class
# load spritesheet
# character_sprite_image = pygame.image.load('girl_sprite.png').convert_alpha()
# character_sprite = SpriteSheet(character_sprite_image)
# bg_colour = "#ff00d6"

player = Character(screen)
player_sprite = SpriteSheet("girl_sprite.png", "ff00d6")



#
# animation_list = []
# animation_steps = 2
# last_animation_update = pygame.time.get_ticks()
# animation_cooldown = 300
# frame = 0
#
# for x in range(animation_steps):
#     animation_list.append(character_sprite.get_image(x, 64, 64, bg_colour))


running = True

while running:

    # framerate in seconds - the time difference between two frames
    dt = clock.tick(FPS) / 1000

    # background screen colour - to change with map
    screen.fill((58, 179, 66))

    # lines 59 - 73 will be going in a function or class
    # sync player position with rect
    # character_rect.topleft = player_position
    player_sprite.get_image(0, 64, 64)
    player.move()
    player_sprite.animate(screen)

    # update animation frame
    # current_animation_time = pygame.time.get_ticks()
    # if current_animation_time - last_animation_update >= animation_cooldown:
    #     frame += 1
    #     last_animation_update = current_animation_time
    #     if frame >= len(animation_list):
    #         frame = 0
    #
    #
    # # draw animated sprite on screen
    # screen.blit(animation_list[frame], character_rect.topleft)


    # add stress and games bar to screen
    stress_bar.draw(screen)
    stress_bar.draw_text(screen)
    games_bar.draw(screen)
    games_bar.draw_text(screen)


    # get status of keys on keyboard
    # keyboard = pygame.key.get_pressed()
    #
    # # movement of character
    # if keyboard[pygame.K_UP] and character_rect.y > 0:
    #     player_position.y -= 250 * dt
    # if keyboard[pygame.K_DOWN] and character_rect.y < SCREEN_HEIGHT - 64:
    #     player_position.y += 250 * dt
    # if keyboard[pygame.K_LEFT] and character_rect.x > 0:
    #     player_position.x -= 250 * dt
    # if keyboard[pygame.K_RIGHT] and character_rect.x < SCREEN_WIDTH - 64:
    #     player_position.x += 250 * dt


    # triggers building's mini game when character collides with it
    # enter_building()


    # exit the game by clicking x or pressing esc key
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        # decreases timer by 1 second every second
        if event.type == pygame.USEREVENT:
                timer.timer_duration -= 1


    timer.countdown(screen)


    # update screen
    pygame.display.flip()



pygame.quit()