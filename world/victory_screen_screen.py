import pygame
import sys

from werkzeug.sansio.http import is_resource_modified

from world.game_screen_classes import Screen
from world.map_config import *

# storing colors in variables
DUSTY_PINK = (231, 84, 128)
SKY_BLUE = (135, 206, 235)
DUSTY_YELLOW = (250, 228, 100)
DARKER_BLUE = (108, 165, 188)
BLACK = (0, 0, 0)
# variable storing
FONT_PATH = "world/PressStart2P-Regular.ttf"

# Child Class inheriting from Screen Class
class VictoryScreen(Screen):
    def __init__(self):
        # initializing the parent class variables
        super().__init__()
        # variables for different sized fonts, calling the font path variable
        self.font_large = pygame.font.Font(FONT_PATH, 60)
        self.font_medium = pygame.font.Font(FONT_PATH, 40)
        self.font_small_2 = pygame.font.Font(FONT_PATH, 30)
        self.font_small = pygame.font.Font(FONT_PATH, 15)
        self.font_tiny = pygame.font.Font(FONT_PATH, 15)
        # blinking interval in milliseconds
        self.star_blink = 300
        self.button_blink = 300
        self.stars = 5
        self.user_text = ''
        self.enter_pressed = False

        # function to load and resize images, size is NONE by default unless it needs resizing
    # takes path and size as arguments
    def load_image(self, path, size=None):
        image = pygame.image.load(path)
        # if size is given, rescale image
        if size:
            return pygame.transform.scale(image, size)
        else:
            # is not just assumes NONE and returns image
            return image

    # function to draw the Game Over Screen
    def draw(self, game_state=None):
        global stars
        # first fills background
        self.screen.fill(SKY_BLUE)
        # pass pygame.time.get_ticks() to count how long since pygame initialized to set the blinking
        current_time = pygame.time.get_ticks()

        # this if statement determines whether the text is displayed, by checking the remainder of the current time
        # divided using floor division to round down by the blinking interval in milliseconds. It's either one, or zero,
        #and only when it is zero does it blit the text.
        victory_text = self.font_large.render("YOU GRADUATED!", True, DUSTY_YELLOW)
        # centering the text exactly in middle
        self.screen.blit(victory_text, (SCREEN_WIDTH // 2 - victory_text.get_width() // 2, 80))
        medal = self.load_image('prototypes/ines_duarte/menus/menu_assets/medal.png', (100, 100))

        # if statements to show the number of stars matching player score.
        if self.stars == 5:
            if (current_time // self.star_blink) % 2 == 0:
                medal = self.load_image('prototypes/ines_duarte/menus/menu_assets/medal.png', (100, 100))
                self.screen.blit(medal, (150, 190))
                self.screen.blit(medal, (300, 190))
                self.screen.blit(medal, (450, 190))
                self.screen.blit(medal, (600, 190))
                self.screen.blit(medal, (750, 190))
            elif (current_time // self.star_blink) % 2 == 1:
                medal = self.load_image('prototypes/ines_duarte/menus/menu_assets/medal.png', (95, 95))
                self.screen.blit(medal, (150, 190))
                self.screen.blit(medal, (300, 190))
                self.screen.blit(medal, (450, 190))
                self.screen.blit(medal, (600, 190))
                self.screen.blit(medal, (750, 190))
            # these are always visible
            score = self.font_medium.render("with Distinction", True, DUSTY_PINK)
            self.screen.blit(score, (SCREEN_WIDTH // 2 - score.get_width() // 2, 310))
        elif self.stars == 4:
            if (current_time // self.star_blink) % 2 == 0:
                self.screen.blit(medal, (210, 190))
                self.screen.blit(medal, (360, 190))
                self.screen.blit(medal, (510, 190))
                self.screen.blit(medal, (660, 190))
            elif (current_time // self.star_blink) % 2 == 1:
                medal = self.load_image('prototypes/ines_duarte/menus/menu_assets/medal.png', (95, 95))
                self.screen.blit(medal, (210, 190))
                self.screen.blit(medal, (360, 190))
                self.screen.blit(medal, (510, 190))
                self.screen.blit(medal, (660, 190))
            score = self.font_medium.render("with Merit!", True, DUSTY_PINK)
            self.screen.blit(score, (SCREEN_WIDTH // 2 - score.get_width() // 2, 310))
        elif self.stars == 3:
            if (current_time // self.star_blink) % 2 == 0:
                self.screen.blit(medal, (300, 190))
                self.screen.blit(medal, (450, 190))
                self.screen.blit(medal, (600, 190))
            elif (current_time // self.star_blink) % 2 == 1:
                medal = self.load_image('prototypes/ines_duarte/menus/menu_assets/medal.png', (95, 95))
                self.screen.blit(medal, (300, 190))
                self.screen.blit(medal, (450, 190))
                self.screen.blit(medal, (600, 190))
            score = self.font_medium.render("Well done!", True, DUSTY_PINK)
            self.screen.blit(score, (SCREEN_WIDTH // 2 - score.get_width() // 2, 310))

    def save_button(self):
        current_time = pygame.time.get_ticks()
            # code for the save button
        if self.enter_pressed == False:
            if (current_time // self.button_blink) % 2 == 0:
                save_button = self.load_image('prototypes/ines_duarte/menus/menu_assets/button_pink.png', (630, 100))
                self.screen.blit(save_button, (SCREEN_WIDTH // 2 - save_button.get_width() // 2, 500))
            elif (current_time // self.button_blink) % 2 == 1:
                save_button = self.load_image('prototypes/ines_duarte/menus/menu_assets/button_pink.png', (625, 95))
                self.screen.blit(save_button, (SCREEN_WIDTH // 2 - save_button.get_width() // 2, 500))
            save_score = self.font_small.render("What name shall we put in the diploma?", True, DUSTY_YELLOW)
            self.screen.blit(save_score, (SCREEN_WIDTH // 2 - save_score.get_width() // 2, 480))
            # user name to save score
            user_name = self.font_small_2.render(self.user_text, True, DARKER_BLUE)
            self.screen.blit(user_name, (SCREEN_WIDTH // 2 - user_name.get_width() // 2, 527))
        else:
            diploma = self.load_image('prototypes/ines_duarte/menus/menu_assets/certificate_1.png', (420, 350))
            self.screen.blit(diploma, (SCREEN_WIDTH // 2 - diploma.get_width() // 2, 350))
            well_done = self.font_small_2.render(self.user_text, True, BLACK)
            self.screen.blit(well_done, (SCREEN_WIDTH // 2 - well_done.get_width() // 2, 410))




    # this checks for pygame events such as key presses and or QUIT
    def menu_handler(self):
        for event in pygame.event.get():
            # if user presses QUIT it closes pygame and sys to close all operations
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # if the key press is either N or ESQ it also quits
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    # Check for backspace
                elif event.key == pygame.K_RETURN:
                    if len(self.user_text) > 0:
                        self.enter_pressed = True
                elif event.key == pygame.K_BACKSPACE:
                    self.user_text = self.user_text[:-1]
                    # Usi Unicode
                else:
                    if len(self.user_text) < 11:
                        self.user_text += event.unicode


# UNCOMMENT TO TEST
def main_game_loop():
    # Initialize Pygame
    pygame.init()

    # Call game over class and store it in a variable in order to create an instance of the screen object
    victory_screen = VictoryScreen()


    # instantiating Clock to control framerate
    clock = pygame.time.Clock()

    while True:
        # stars variable to change medals. This should probably be coded with the timer to update depending on final time
        victory_screen.stars = 3
        # pass the menu interaction function


        # Draw the Game Over screen
        victory_screen.draw()
        victory_screen.save_button()

        victory_screen.menu_handler()


        # Update the screen
        pygame.display.flip()

        # set the frame rate at 60 FPS
        clock.tick(60)

if __name__ == "__main__":
    main_game_loop()
