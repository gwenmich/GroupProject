import pygame
import sys
from abc import ABC, abstractmethod
from world.game_over_screen import FONT_PATH
from utilities.speech_bubble_map import Bubble, center_text, DARK_BLUE
from pygame import Rect

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
        self.title_font = pygame.font.Font(FONT_PATH, 36)
        self.title_font_2 = pygame.font.Font(FONT_PATH, 35)
        self.start_font = pygame.font.Font(FONT_PATH, 18)
        self.start_font_2 = pygame.font.Font(FONT_PATH, 17)
        self.rules_font = pygame.font.Font(FONT_PATH, 13)

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
                intro_bubble = IntroBubble.load_image('assets/bubbles/board.png',(self.bubble_width, self.bubble_height))
                intro_text = self.title_font.render("WELCOME TO CAMPUS", True, DUSTY_PINK)
                intro_rect = pygame.Rect(self.bubble_x, self.bubble_y - 50, self.bubble_width, self.bubble_height)
                start = self.start_font.render("Press ENTER to start your quest", True, DUSTY_PINK)
                start_rect = pygame.Rect(self.bubble_x, self.bubble_y, self.bubble_width, self.bubble_height)
            elif (current_time // self.blink_interval) % 2 == 1:
                intro_bubble = IntroBubble.load_image('assets/bubbles/board.png',(self.bubble_width-3, self.bubble_height-3))
                intro_text = self.title_font_2.render("WELCOME TO CAMPUS", True, DUSTY_PINK)
                intro_rect = pygame.Rect(self.bubble_x, self.bubble_y - 50, self.bubble_width, self.bubble_height)
                start = self.start_font_2.render("Press ENTER to start your quest", True, DUSTY_PINK)
                start_rect = pygame.Rect(self.bubble_x, self.bubble_y, self.bubble_width, self.bubble_height)

            # only need to write the blit code once because the if logic changed the variable
            surface_type.blit(intro_bubble, (self.bubble_x, self.bubble_y))
            start_x, start_y = center_text(start_rect, start)
            surface_type.blit(start, (start_x, 510))

            # GAME RULES Text
            text_x, text_y = center_text(intro_rect, intro_text)
            surface_type.blit(intro_text, (text_x, 120))
            # welcome to campus text
            welcome = self.font_small_2.render("Your PhD Thesis is due TODAY!", True, DARK_BLUE)
            surface_type.blit(welcome, (210, 180))

            # rules text to be wrapped around in two blocks
            rules = ("But it's not finished... Navigate the campus map using the ARROW KEYS and WIN all FOUR challenged "
                     "in the LIBRARY, IT DEPARTMENT, CAFETERIA and CLASSROOM to complete your thesis. Be quick, you can't "
                     "miss the deadline!")
            rules_2 = ("You can retry a failed challenge, but mind your STRESS or you'll have a breakdown!When you feel"
                     "overwhelmed go to the COUNSELLING Building for some meditation to lower your stress. But don't "
                       "get too relaxed! No extensions this time! What are you waiting for?")
            rules_rect = Rect(210, 230, 600, 260)
            Bubble.wrap_text(surface_type, rules, DARK_BLUE, rules_rect, self.rules_font, aa=True)
            rules2_rect = Rect(210, 355, 600, 260)
            Bubble.wrap_text(surface_type, rules_2, DARK_BLUE, rules2_rect, self.rules_font, aa=True)


    # handler to clear text when ENTER is pressed
    def handler(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.enter_pressed = True
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

