import pygame
from main_config import *
from game_class import Game
from menu_class import Menu
import sys

# Game states
class GameState:
    MAIN_MENU = "main_menu"
    GAME = "game"

# Game Manager
class GameManager:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Thesis Quest")
        self.clock = pygame.time.Clock()
        self.game_state = GameState.MAIN_MENU
        self.selected_option = 0
        self.menu = Menu(self)
        self.game = Game(self)
        self.setup_music()

    def setup_music(self):
        pygame.mixer.music.load('assets/main_menu/lofi1.mp3')
        pygame.mixer.music.play(-1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.game_state == GameState.MAIN_MENU:
                    self.menu.handle_input(event)
                elif self.game_state == GameState.GAME:
                    self.game.handle_input(event)

            if self.game_state == GameState.MAIN_MENU:
                self.menu.display()
            elif self.game_state == GameState.GAME:
                self.game.loop()

            self.clock.tick(FPS)

