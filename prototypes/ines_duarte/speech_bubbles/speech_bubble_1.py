import pygame
import sys
from abc import ABC, abstractmethod
from world.map_config import *
from world.game_screen_classes import Screen, MapScreen
from world.victory_screen_screen import *
from prototypes.ines_duarte.random_useful_code import hitbox_visible_square
# from handlers.hitboxes import *

DARK_BLUE = (10, 100, 160)


def center_text(rect, text):
    x_position = rect.x + (rect.width - text.get_width()) // 2
    y_position = rect.y + (rect.height - text.get_height()) // 2
    return x_position, y_position

# class for speech bubbles
class Bubble(ABC):
    # initialize
    def __init__(self, surface, width, height, x_axis, y_axis, text):
        pygame.init()
        FONT_PATH = "world/PressStart2P-Regular.ttf"
        self.font_large = pygame.font.Font(FONT_PATH, 60)
        self.font_medium = pygame.font.Font(FONT_PATH, 40)
        self.font_small_2 = pygame.font.Font(FONT_PATH, 20)
        self.font_small = pygame.font.Font(FONT_PATH, 12)
        self.font_tiny = pygame.font.Font(FONT_PATH, 11)
        self.bubble_height = height
        self.bubble_width = width
        self.bubble_x = x_axis
        self.bubble_y = y_axis
        self.text = text
        self.enter_pressed = False
        self.surface = surface



    @staticmethod
    def load_image(path, size=None):
        image = pygame.image.load(path)
        # if size is given, rescale image
        if size:
            return pygame.transform.scale(image, size)
        else:
            # is not just assumes NONE and returns image
            return image

    # abstract methods to be overwritten by child classes
    @abstractmethod
    def draw(self):
        pass


class MapBubbles(Bubble):
    def __init__(self, surface, x_axis, y_axis, text):
        # initializing the parent class variables
        super().__init__(surface, width=110, height=90, x_axis=x_axis, y_axis=y_axis, text=text)
        self.bubble_blink = 300
        self.enter_pressed = False

        self.building_names = {
                            "Library": (280, 520),
                            "Classroom": (815, 120),
                            "Cafeteria":(480, 190),
                            "IT Department":(280, 120),
                            "Counselling": (480, 190)
                        }


    # bubble_rect = pygame.Rect(player_position.x, player_position.y, 64, 64)
    def draw(self):
        current_time = pygame.time.get_ticks()
        if self.enter_pressed == False:
            if (current_time // self.bubble_blink) % 2 == 0:
                # text instruction to player on how to clear bubble
                clear_bubble = self.font_small_2.render("PRESS ENTER TO CLEAR", True, DARK_BLUE)
                self.surface.screen.blit(clear_bubble, (SCREEN_WIDTH // 2 - clear_bubble.get_width() // 2, 655))

                bubble = Bubble.load_image('prototypes/ines_duarte/speech_bubbles/message_pink.png', (self.bubble_width, self.bubble_height))
                self.surface.screen.blit(bubble, (self.bubble_x, self.bubble_y))
                building_name = self.font_small.render(self.text, True, DARK_BLUE)

                bubble_rect = pygame.Rect(self.bubble_x, self.bubble_y, self.bubble_width, self.bubble_height)
                text_x, text_y = center_text(bubble_rect, building_name)
                self.surface.screen.blit(building_name, (text_x, text_y - 5))

            elif (current_time // self.bubble_blink) % 2 == 1:
                bubble = Bubble.load_image('prototypes/ines_duarte/speech_bubbles/message_pink.png', (self.bubble_width - 3, self.bubble_height - 3))
                self.surface.screen.blit(bubble, (self.bubble_x, self.bubble_y))
                building_name = self.font_tiny.render(self.text, True, DARK_BLUE)
                # centering the text in bubble using the rect
                bubble_rect = pygame.Rect(self.bubble_x, self.bubble_y, self.bubble_width, self.bubble_height)
                text_x, text_y  = center_text(bubble_rect, building_name)
                self.surface.screen.blit(building_name, (text_x, text_y - 5))


    def menu_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.enter_pressed = True



def main_game_loop():
    # Initialize Pygame
    pygame.init()

    # Call game over class and store it in a variable in order to create an instance of the screen object
    map_screen = MapScreen()
    bubble = MapBubbles(map_screen, 280, 520, 'Library')

    # instantiating Clock to control framerate
    clock = pygame.time.Clock()

    while True:
        # stars variable to change medals. This should probably be coded with the timer to update depending on final time
        map_screen.draw()
        bubble.draw()
        bubble.menu_handler()

        # Update the screen
        pygame.display.flip()

        # set the frame rate at 60 FPS
        clock.tick(60)

if __name__ == "__main__":
    main_game_loop()