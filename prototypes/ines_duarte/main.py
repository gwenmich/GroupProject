import sys

from hitboxes import *
from utilities.speech_bubble_map import *
from utilities.intro_bubble import *
from prototypes.ines_duarte.random_useful_code import hitbox_visible_square




# Initializing pygame!
pygame.init()

clock = pygame.time.Clock()

dt = 0

# set player start position
player_position = pygame.Vector2(530, 410)

# load main character image and get its rectangle
character = pygame.image.load('prototypes/ines_duarte/girl64_cropped.png').convert_alpha()
x = character.get_width()
y = character.get_height()



def game_loop():
    global player_position

    # setting running to True for game loop
    running = True
    # game loop
    bubble = MapBubbles(screen, 0, 0, "")

    intro_bubble = IntroBubble(screen, 125, 30, '')

    while running:

        # framerate in seconds - the time difference between two frames
        dt = clock.tick(FPS) / 1000

        # position character's rect in the centre of the screen
        character_rect = character.get_rect(center=player_position)

        screen.fill((0, 200, 110))
        # drawing tile map
        draw_tile_map()

        # drawing character on top and setting position
        screen.blit(character, character_rect)

        # get status of keys on keyboard
        keyboard = pygame.key.get_pressed()

        # we need a new_position variable to check for collision, before we update player position
        new_position = player_position.copy()

        # movement of character
        if keyboard[pygame.K_UP] and character_rect.y > 20:
            new_position.y -= 250 * dt
        if keyboard[pygame.K_DOWN] and character_rect.y < SCREEN_HEIGHT - 77:
            new_position.y += 250 * dt
        if keyboard[pygame.K_LEFT] and character_rect.x > 20:
            new_position.x -= 250 * dt
        if keyboard[pygame.K_RIGHT] and character_rect.x < SCREEN_WIDTH - 52:
            new_position.x += 250 * dt


        # updates player hitbox position
        new_rect = character.get_rect(center=new_position)

        # check collision
        building_collision = check_collision(new_rect, hitboxes)

        # check collision with building bubbles
        bubble.handler(new_rect, buildings_bubble_hitboxes, bubble_position)

        if bubble.visible_bubble == True:
            bubble.draw()

        if building_collision == False:
            player_position = new_position

        intro_bubble.draw()
        intro_bubble.handler()

        # hitbox_visible_square(screen, 205, 260, 600, 260)
        # game quitting logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False



        # remember to update the screen!
        pygame.display.flip()


    pygame.quit()
    sys.exit()


game_loop()