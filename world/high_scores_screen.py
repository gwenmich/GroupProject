import pygame
import sys
from world.game_screen_classes import Screen
from world.map_config import *
import requests


# storing colors in variables
DUSTY_PINK = (250, 100, 160)
SKY_BLUE = (135, 206, 235)
DUSTY_YELLOW = (250, 228, 30)
DARK_PURPLE = (150, 0, 100)
BLACK = (0, 0, 0)

# variable storing
FONT_PATH = "world/PressStart2P-Regular.ttf"

# Child Class inheriting from Screen Class
class HighScoreScreen(Screen):
    def __init__(self):
        # initializing the parent class variables
        super().__init__()
        # variables for different sized fonts, calling the font path variable
        self.font_large = pygame.font.Font(FONT_PATH, 70)
        self.font_medium = pygame.font.Font(FONT_PATH, 20)
        self.font_small = pygame.font.Font(FONT_PATH, 15)
        # new variable to contain the menu game stated that will be used to update the main game loop
        # always reset back to its own menu
        self.menu = "High Scores"

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


    def get_top10_scores_front_end(self):
        endpoint = "http://127.0.0.1:5000/scores"
        result = requests.get(endpoint).json()
        return result

    # function to draw the Game Over Screen
    def draw(self):
        icon = self.load_image('prototypes/ines_duarte/menus/menu_assets/new_cloud_bg.png', (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.blit(icon, (0,0))

        scores = self.get_top10_scores_front_end()

        # pass pygame.time.get_ticks() to count how long since pygame initialized to set the blinking
        current_time = pygame.time.get_ticks()

        # this if statement determines whether the text is displayed, by checking the remainder of the current time
        # divided using floor division to round down by the blinking interval in milliseconds. It's either one, or zero,
        #and only when it is zero does it blit the text.

        high_score_text = self.font_large.render("HIGH SCORES", True, DARK_PURPLE)
        # centering the text exactly in middle
        self.screen.blit(high_score_text, (SCREEN_WIDTH // 2 - high_score_text.get_width() // 2, 80))

        headers = self.font_medium.render("PLAYERS     TIME      STARS", True, DUSTY_YELLOW)
        self.screen.blit(headers, (SCREEN_WIDTH // 2 - headers.get_width() // 2, 200))

        y_position = 250
        for score in scores:
            score_text = f"{score['Player']}"
            rendered_text = self.font_small.render(score_text, True, DARK_PURPLE)
            self.screen.blit(rendered_text, (300 - rendered_text.get_width() // 2, y_position))
            y_position += 40

        y_position = 250
        for score in scores:
            score_text = f"{score['Stars']}"
            rendered_text = self.font_small.render(score_text, True, DARK_PURPLE)
            self.screen.blit(rendered_text, (720 - rendered_text.get_width() // 2, y_position))
            y_position += 40

        y_position = 250
        for score in scores:
            score_text = f"{score['Final Time']}"
            rendered_text = self.font_small.render(score_text, True, DARK_PURPLE)
            self.screen.blit(rendered_text, (510 - rendered_text.get_width() // 2, y_position))
            y_position += 40

        pygame.display.flip()

            # this checks for pygame events such as key presses and or QUIT
    def handler(self):
        for event in pygame.event.get():
            # if user presses QUIT it closes pygame and sys to close all operations
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # if the key press is ESQ back to menu
                if event.key == pygame.K_ESCAPE:
                    # variable to update game state gets called here to go back to main menu
                    self.menu = "Main Menu"



# UNCOMMENT TO TEST
def main_game_loop():
    # Initialize Pygame
    pygame.init()

    # Call game over class and store it in a variable in order to create an instance of the screen object
    high_score_screen = HighScoreScreen()

    # instantiating Clock to control framerate
    clock = pygame.time.Clock()

    while True:
        # pass the menu interaction function
        high_score_screen.handler()

        # Draw the Game Over screen
        high_score_screen.draw()

        # Update the screen
        pygame.display.flip()

        # set the frame rate at 60 FPS
        clock.tick(60)

if __name__ == "__main__":
    main_game_loop()
