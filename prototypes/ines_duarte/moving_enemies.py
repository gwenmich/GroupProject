import pygame
from world.map_config import *
from utilities.bars_classes import StressBar, GamesBar
from utilities.timer import Timer
from prototypes.gwen_michailidis.spritesheet import SpriteSheet

# from character_building_collision import enter_building

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

dt = 0

# position player in the centre of the screen
player_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
character_rect = pygame.Rect(player_position.x, player_position.y, 64, 64)



# initialise stress and games bars
stress_bar = StressBar(900, 20, 70, 16, 100)
games_bar = GamesBar(510, 20, 70, 16, 4)

# set timer for 30 minutes -> 1800 seconds
timer = Timer(1800)
# creating timer where a userevent is posted to event queue every 1 second (1000 milliseconds)
pygame.time.set_timer(pygame.USEREVENT, 1000)

# lines 33 - 46 will be going into a function or class
# load spritesheet
character_sprite_image = pygame.image.load('prototypes/gwen_michailidis/girl_sprite.png').convert_alpha()
character_sprite = SpriteSheet(character_sprite_image)
bg_colour = "#ff00d6"

#
animation_list = []
animation_steps = 2
last_animation_update = pygame.time.get_ticks()
animation_cooldown = 300
frame = 0

for x in range(animation_steps):
    animation_list.append(character_sprite.get_image(x, 64, 64, bg_colour))




# same as your hero - load
enemy = pygame.image.load('prototypes/ines_duarte/girl64_cropped.png').convert_alpha()
enemy_position = pygame.Vector2(250, 410)
# movement speed
enemy_speed = 100
enemy_direction = 1

# enemy_rect = enemy.get_rect(center=enemy_position)


running = True

while running:

    # framerate in seconds - the time difference between two frames
    dt = clock.tick(FPS) / 1000

    # background screen colour - to change with map
    screen.fill((58, 179, 66))
    # **************************************************************************
    enemy_rect = enemy.get_rect(center=enemy_position)
    # lines 59 - 73 will be going in a function or class
    # sync player position with rect
    character_rect.topleft = player_position

    # update animation frame
    current_animation_time = pygame.time.get_ticks()
    if current_animation_time - last_animation_update >= animation_cooldown:
        frame += 1
        last_animation_update = current_animation_time
        if frame >= len(animation_list):
            frame = 0

    screen.blit(enemy, enemy_rect)

    # this would make the enemy move horizontaly
    # it adds to the x postion the speed * direction (which is either 1 or -1)
    # 1 is moving right
    # -1 is left
    # * times dt(delta time) to keep movement smooth
    enemy_position.x += enemy_speed * enemy_direction * dt
    # then you set the boundaries
    if enemy_rect.colliderect(character_rect) == False:
        if enemy_position.x <= 200 or enemy_position.x >= 350:
            # if it hits a boundry the directio is multiplied by -1, which either makes 1 or -1
            enemy_direction *= -1
    # and it increments or reduces x moving the enemy around
    # just blit it as your hero

    # draw animated sprite on screen
    screen.blit(animation_list[frame], character_rect.topleft)



    # add stress and games bar to screen
    # stress_bar.draw(screen)
    # stress_bar.draw_text(screen)
    # games_bar.draw(screen)
    # games_bar.draw_text(screen)


    # get status of keys on keyboard
    keyboard = pygame.key.get_pressed()

    # movement of character
    if character_rect.colliderect(enemy_rect) == False:
        if keyboard[pygame.K_UP] and character_rect.y > 0:
            player_position.y -= 250 * dt
        if keyboard[pygame.K_DOWN] and character_rect.y < SCREEN_HEIGHT - 64:
            player_position.y += 250 * dt
        if keyboard[pygame.K_LEFT] and character_rect.x > 0:
            player_position.x -= 250 * dt
        if keyboard[pygame.K_RIGHT] and character_rect.x < SCREEN_WIDTH - 64:
            player_position.x += 250 * dt


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


    # timer.countdown(screen)


    # update screen
    pygame.display.flip()



pygame.quit()