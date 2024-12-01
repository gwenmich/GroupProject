import pygame
import sys
from world.game_screen_classes import Screen
from world.map_config import *
# from main.game_class import *

# storing colors in variables
DUSTY_PINK = (231, 84, 128)
SKY_BLUE = (135, 206, 235)
DUSTY_YELLOW = (239, 228, 176)
# variable storing
FONT_PATH = "world/PressStart2P-Regular.ttf"

# Child Class inheriting from Screen Class
class GameOverScreen(Screen):
    def __init__(self):
        # initializing the parent class variables
        super().__init__()
        # variables for different sized fonts, calling the font path variable
        self.font_large = pygame.font.Font(FONT_PATH, 90)
        self.font_medium = pygame.font.Font(FONT_PATH, 40)
        self.font_small = pygame.font.Font(FONT_PATH, 15)
        # blinking interval in milliseconds
        self.blink_interval = 450
        # self.play_again = Game()

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
    def draw(self):
        # first fills background
        self.screen.fill(DUSTY_PINK)
        # pass pygame.time.get_ticks() to count how long since pygame initialized to set the blinking
        current_time = pygame.time.get_ticks()

        # this if statement determines whether the text is displayed, by checking the remainder of the current time
        # divided using floor division to round down by the blinking interval in milliseconds. It's either one, or zero,
        #and only when it is zero does it blit the text.
        if (current_time // self.blink_interval) % 2 == 0:
            game_over_text = self.font_large.render("GAME OVER", True, DUSTY_YELLOW)
            # centering the text exactly in middle
            self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2,
                                              SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))

        # these are always visible
        replay = self.font_medium.render("Try again?", True, SKY_BLUE)
        self.screen.blit(replay, (SCREEN_WIDTH // 2 - replay.get_width() // 2, 500))

        yes_no = self.font_small.render("Type y(Yes) or n(No)", True, DUSTY_YELLOW)
        self.screen.blit(yes_no, (SCREEN_WIDTH // 2 - yes_no.get_width() // 2, 570))

        icon = self.load_image('assets/main_map/game_over_pc_icon.png', (200, 200))
        self.screen.blit(icon, (SCREEN_WIDTH // 2 - icon.get_width() // 2, 100))

    # this checks for pygame events such as key presses and or QUIT
    def handler(self):
        for event in pygame.event.get():
            # if user presses QUIT it closes pygame and sys to close all operations
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # if the key press is either N or ESQ it also quits
                if event.key == pygame.K_n or event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                # if key press is Y replay game loop
                elif event.key == pygame.K_y:
                    # self.play_again.loop()
                    return



# UNCOMMENT TO TEST
def main_game_loop():
    # Initialize Pygame
    pygame.init()

    # Call game over class and store it in a variable in order to create an instance of the screen object
    game_over_screen = GameOverScreen()

    # instantiating Clock to control framerate
    clock = pygame.time.Clock()

    while True:
        # pass the menu interaction function
        game_over_screen.handler()

        # Draw the Game Over screen
        game_over_screen.draw()

        # Update the screen
        pygame.display.flip()

        # set the frame rate at 60 FPS
        clock.tick(60)

if __name__ == "__main__":
    main_game_loop()
