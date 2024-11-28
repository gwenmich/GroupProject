import pygame
import sys
from abc import ABC, abstractmethod
from world.game_over_screen import FONT_PATH
from world.map_config import *
from world.game_screen_classes import Screen, MapScreen
from utilities.speech_bubble_map import Bubble, center_text, DARK_BLUE


DUSTY_PINK = (231, 84, 128)
SKY_BLUE = (135, 206, 235)
DUSTY_YELLOW = (250, 228, 100)
DARKER_BLUE = (108, 165, 188)
BLACK = (0, 0, 0)

# new class for intro bubble, inheriting from Bubble Class
class IntroBubble(Bubble):
    def __init__(self, surface, x_axis, y_axis, text):
        super().__init__(surface, width=760, height=660, x_axis=x_axis, y_axis=y_axis, text=text)
        self.enter_pressed = False
        self.blink_interval = 300
        self.title_font = pygame.font.Font(FONT_PATH, 50)
        self.welcome_font = pygame.font.Font(FONT_PATH, 25)
        self.rules_font = pygame.font.Font(FONT_PATH, 12)

    def draw(self):
        current_time = pygame.time.get_ticks()

        if isinstance(self.surface, pygame.Surface):
            surface_type = self.surface
        elif hasattr(self.surface, 'screen'):
            surface_type = self.surface.screen
        else:
            raise ValueError("Invalid surface type passed to IntroBubble")

        # creating pulsation effect
        if self.enter_pressed == False:
            if (current_time // self.blink_interval) % 2 == 0:
                intro_bubble = IntroBubble.load_image('prototypes/ines_duarte/menus/menu_assets/board.png',(self.bubble_width, self.bubble_height))
            elif (current_time // self.blink_interval) % 2 == 1:
                intro_bubble = IntroBubble.load_image('prototypes/ines_duarte/menus/menu_assets/board.png',(self.bubble_width-3, self.bubble_height-3))

            # only need to write the blit code once because the if logic changed the variable
            surface_type.blit(intro_bubble, (self.bubble_x, self.bubble_y))

            # GAME RULES Text
            intro_text = self.title_font.render("GAME RULES", True, DUSTY_PINK)
            intro_rect = pygame.Rect(self.bubble_x, self.bubble_y-50, self.bubble_width, self.bubble_height)
            text_x, text_y = center_text(intro_rect, intro_text)
            surface_type.blit(intro_text, (text_x, 140))
            # welcome to campus text
            welcome = self.font_small_2.render("Welcome to Campus", True, DARK_BLUE)
            surface_type.blit(welcome, (330, 220))
            # rules text to be wrapped around
            rules_line_1 = "After weeks of procrastinating and exams drawing"
            rules_line_2 = "near you suddenly realize OH NO! the PhD thesis deadline is today? You have no time to waste!"

            rules_1 = self.rules_font.render(rules_line_1, True, DARK_BLUE)
            surface_type.blit(rules_1, (210, 280))

            rules_2 = self.rules_font.render(rules_line_2, True, DARK_BLUE)
            surface_type.blit(rules_2, (210, 300))




    def handler(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.enter_pressed = True








