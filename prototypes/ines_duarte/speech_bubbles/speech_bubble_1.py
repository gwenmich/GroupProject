import pygame
import sys
from abc import ABC, abstractmethod
from world.map_config import *
from world.game_screen_classes import Screen, MapScreen
from world.victory_screen_screen import *

DARK_BLUE = (10, 100, 160)

# class for speech bubbles
class Bubble(ABC):
    # initialize
    def __init__(self, surface):
        pygame.init()
        FONT_PATH = "world/PressStart2P-Regular.ttf"
        self.font_large = pygame.font.Font(FONT_PATH, 60)
        self.font_medium = pygame.font.Font(FONT_PATH, 40)
        self.font_small_2 = pygame.font.Font(FONT_PATH, 30)
        self.font_small = pygame.font.Font(FONT_PATH, 15)
        self.font_tiny = pygame.font.Font(FONT_PATH, 12)
        self.bubble_height = 80
        self.bubble_width = 100
        self.bubble_x = 470
        self.bubble_y = 230
        self.enter_pressed = False
        self.surface = surface


    # abstract methods to be overwritten by child classes
    @abstractmethod
    def load_image(self, path, size=None):
        pass

    # abstract methods to be overwritten by child classes
    @abstractmethod
    def draw(self):
        pass


class MapBubbles(Bubble):
    def __init__(self, surface):
        # initializing the parent class variables
        super().__init__(surface)

    def load_image(self, path, size=None):
        image = pygame.image.load(path)
        # if size is given, rescale image
        if size:
            return pygame.transform.scale(image, size)
        else:
            # is not just assumes NONE and returns image
            return image

    # bubble_rect = pygame.Rect(player_position.x, player_position.y, 64, 64)
    def draw(self):
        counselling_office_1 = pygame.Rect(465, 300, 130, 130)
        bubble = self.load_image('prototypes/ines_duarte/speech_bubbles/message_pink.png', (self.bubble_width, self.bubble_height))
        self.surface.screen.blit(bubble, (self.bubble_x, self.bubble_y))
        bubble_rect = pygame.Rect(self.bubble_x, self.bubble_y, self.bubble_width, self.bubble_height)

        building_name = self.font_tiny.render("Library", True, DARK_BLUE)
        # centering the text in bubble using the rect
        text_x = bubble_rect.x + (bubble_rect.width - building_name.get_width()) // 2
        text_y = bubble_rect.y + (bubble_rect.height - building_name.get_height()) // 2
        self.surface.screen.blit(building_name, (text_x, text_y - 5))







def main_game_loop():
    # Initialize Pygame
    pygame.init()

    # Call game over class and store it in a variable in order to create an instance of the screen object
    map_screen = MapScreen()
    bubble = MapBubbles(map_screen)

    # instantiating Clock to control framerate
    clock = pygame.time.Clock()

    while True:
        # stars variable to change medals. This should probably be coded with the timer to update depending on final time
        map_screen.draw()
        bubble.draw()

        # Update the screen
        pygame.display.flip()

        # set the frame rate at 60 FPS
        clock.tick(60)

if __name__ == "__main__":
    main_game_loop()