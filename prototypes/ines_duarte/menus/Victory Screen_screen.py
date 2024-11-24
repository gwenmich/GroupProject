import pygame
import sys
from world.game_screen_classes import Screen
from world.map_config import *

# storing colors in variables
DUSTY_PINK = (231, 84, 128)
SKY_BLUE = (135, 206, 235)
DUSTY_YELLOW = (250, 228, 100)
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
        self.font_small = pygame.font.Font(FONT_PATH, 15)
        # blinking interval in milliseconds
        self.blink_interval = 600

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


        # yes_no = self.font_small.render("Type y(Yes) or n(No)", True, DUSTY_YELLOW)
        # self.screen.blit(yes_no, (SCREEN_WIDTH // 2 - yes_no.get_width() // 2, 570))

        medal = self.load_image('prototypes/ines_duarte/menus/menu_assets/medal.png', (100, 100))
        if (current_time // self.blink_interval) % 2 == 0:
            self.screen.blit(medal, (150, 190))
            self.screen.blit(medal, (300, 190))
            self.screen.blit(medal, (450, 190))
            self.screen.blit(medal, (600, 190))
            self.screen.blit(medal, (750, 190))
        # these are always visible
        score = self.font_medium.render("with Distinction", True, DUSTY_PINK)
        self.screen.blit(score, (SCREEN_WIDTH // 2 - score.get_width() // 2, 350))

        # if stars == 3:
        #     if (current_time // self.blink_interval) % 2 == 0:
        #         self.screen.blit(medal, (300, 190))
        #         self.screen.blit(medal, (450, 190))
        #         self.screen.blit(medal, (600, 190))



    # this checks for pygame events such as key presses and or QUIT
    def menu_handler(self):
        for event in pygame.event.get():
            # if user presses QUIT it closes pygame and sys to close all operations
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # if the key press is either N or ESQ it also quits
                if event.key == pygame.K_n or event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                # if key press is Y replay game loop
                if event.key == pygame.K_y:
                    main_game_loop()
                    return



# UNCOMMENT TO TEST
def main_game_loop():
    # Initialize Pygame
    pygame.init()

    # Call game over class and store it in a variable in order to create an instance of the screen object
    victory_screen = VictoryScreen()

    # instantiating Clock to control framerate
    clock = pygame.time.Clock()

    while True:
        # pass the menu interaction function
        victory_screen.menu_handler()

        # Draw the Game Over screen
        victory_screen.draw()

        # Update the screen
        pygame.display.flip()

        # set the frame rate at 60 FPS
        clock.tick(60)

if __name__ == "__main__":
    main_game_loop()
