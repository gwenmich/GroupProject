import pygame
import sys
from abc import ABC, abstractmethod
from world.map_config import *
from world.game_screen_classes import Screen, MapScreen
# from world.victory_screen_screen import *
from handlers.hitboxes import *


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
        self.font_small = pygame.font.Font(FONT_PATH, 11)
        self.font_tiny = pygame.font.Font(FONT_PATH, 10)
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
        super().__init__(surface, width=140, height=100, x_axis=x_axis, y_axis=y_axis, text=text)
        self.bubble_blink = 300
        self.visible_bubble = False



    # bubble_rect = pygame.Rect(player_position.x, player_position.y, 64, 64)
    def draw(self):
        current_time = pygame.time.get_ticks()
        # this is to handle nested surfaces.
        if isinstance(self.surface, pygame.Surface):
            surface_type = self.surface
        elif hasattr(self.surface, 'screen'):
            surface_type = self.surface.screen
        else:
            raise ValueError("Invalid surface type passed to MapBubbles")


        if self.enter_pressed == False:
            if (current_time // self.bubble_blink) % 2 == 0:
                bubble = Bubble.load_image('assets/main_map/message_pink.png', (self.bubble_width, self.bubble_height))
                surface_type.blit(bubble, (self.bubble_x, self.bubble_y))
                building_name = self.font_small.render(self.text, True, DARK_BLUE)

                bubble_rect = pygame.Rect(self.bubble_x, self.bubble_y, self.bubble_width, self.bubble_height)
                text_x, text_y = center_text(bubble_rect, building_name)
                surface_type.blit(building_name, (text_x, text_y - 5))

            elif (current_time // self.bubble_blink) % 2 == 1:
                bubble = Bubble.load_image('assets/main_map/message_pink.png', (self.bubble_width - 3, self.bubble_height - 3))
                surface_type.blit(bubble, (self.bubble_x, self.bubble_y))
                building_name = self.font_tiny.render(self.text, True, DARK_BLUE)
                # centering the text in bubble using the rect
                bubble_rect = pygame.Rect(self.bubble_x, self.bubble_y, self.bubble_width, self.bubble_height)
                text_x, text_y  = center_text(bubble_rect, building_name)
                surface_type.blit(building_name, (text_x, text_y - 5))


    # thif function checks for collisions with the coordinates on the hitboxes in building_bubble_list, and draws the
    # bubble at the coordinates and name on bubble_position w
    def handler(self, new_rect, buildings_bubble_hitboxes, bubble_position):
        # this call another function that has the collision checking logic. Buildings_bubble_list has the hibtboxes for the buildings
        bubble_collision = check_collision_items(new_rect, buildings_bubble_hitboxes)
        # if no collision, not visible
        if bubble_collision == False:
            self.visible_bubble = False
        else:
            # else visible is True
            self.visible_bubble = True
            # pass to bubble position the name of the building returned by bubble_colission to get the righ x,y and text
            x, y = bubble_position[bubble_collision]
            self.bubble_x = x
            self.bubble_y = y
            # the building is the name returned by the collision check
            self.text = bubble_collision

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.enter_pressed = True



# def main_game_loop():
#     # Initialize Pygame
#     pygame.init()
#
#     # Call game over class and store it in a variable in order to create an instance of the screen object
#     map_screen = MapScreen()
#     bubble = MapBubbles(map_screen, 0, 0, "")
#     # instantiating Clock to control framerate
#     clock = pygame.time.Clock()
#
#     while True:
#         # stars variable to change medals. This should probably be coded with the timer to update depending on final time
#         map_screen.draw()
#         bubble.draw()
#         bubble.handler()
#
#         # Update the screen
#         pygame.display.flip()
#
#         # set the frame rate at 60 FPS
#         clock.tick(60)
#
if __name__ == "__main__":
#     # to put in game loop
# # instantiate bubble with dummy values, baically zeros and empty string, just pass the correct surface
    bubble = MapBubbles(map_screen, 0, 0, "")

    # pass handler in loop with the character rect as argument and
    bubble.handler(new_rect, buildings_bubble_hitboxes, bubble_position)

    if bubble.visible_bubble == True:
        bubble.draw()