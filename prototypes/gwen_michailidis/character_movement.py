import pygame
from config import *
from bars_classes import StressBar, GamesBar
from timer import Timer
from character_class import Character
# from character_building_collision import enter_building

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

dt = 0




# instantiate stress and games bars
stress_bar = StressBar(900, 20, 70, 16, 100)
games_bar = GamesBar(510, 20, 70, 16, 4)

# set timer for 30 minutes -> 1800 seconds
timer = Timer(1800)
# creating timer where a userevent is posted to event queue every 1 second (1000 milliseconds)
pygame.time.set_timer(pygame.USEREVENT, 1000)


# instantiate player
player = Character(screen, "girl_sprite.png", 2,"#ff00d6", 64, 64)




running = True

while running:

    # framerate in seconds - the time difference between two frames
    dt = clock.tick(FPS) / 1000

    # background screen colour - to change with map
    screen.fill((58, 179, 66))

    # animates character and ability to move it
    player.animate(screen)
    player.move(250, dt)


    # add stress and games bar to screen
    stress_bar.draw(screen)
    stress_bar.draw_text(screen)
    games_bar.draw(screen)
    games_bar.draw_text(screen)



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