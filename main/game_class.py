from character_class import Character
from main_config import FPS, game_state
from world.game_over_screen import GameOverScreen
from world.game_screen_classes import MapScreen
import pygame
from menu_class import Menu
import sys
from world.high_scores_screen import HighScoreScreen


class Game:
    def __init__(self):
        # self.manager = manager
        self.map_screen = MapScreen()
        self.menu = Menu()
        self.player = Character(self.map_screen.screen, "assets/sprites/girl_sprite.png", 2, "#ff00d6", 64, 64)
        self.clock = pygame.time.Clock()
        self.dt = 0
        # self.game = Game(self)
        self.high_scores = HighScoreScreen()
        self.game_over = GameOverScreen()



    def loop(self):
        while True:
            global game_state
            self.dt = self.clock.tick(FPS)/1000

            print(f"Before checking: Current game_state = {game_state}")

            if game_state != self.menu.next_game_state:
                print(f"Game state updated to: {self.menu.next_game_state}")
                game_state = self.menu.next_game_state

            if game_state == "Main Menu":
                print(f"In Main Menu state.")
                self.menu.display(self.map_screen.screen)
                self.menu.handle_input()
            elif game_state == "High Scores":
                print(f"In High Scores state.")
                self.high_scores.draw()
                self.high_scores.menu_handler()
            elif game_state == "Map":
                print(f"In Map state.")
                self.map_screen.draw()
                self.map_screen.handler()
                self.player.animate(self.map_screen.screen)
                self.player.move(250, self.dt)
            elif game_state == "Victory":
                print(f"In Game over state state.")
                self.game_over.draw()
                self.game_over.menu_handler()

            elif game_state == "Game Over":
                print(f"In Game over state state.")




            # pygame.mixer.music.load('assets/main_menu/mapmusic.mp3')
            # pygame.mixer.music.play(-1)
            pygame.display.flip()

            print(f"After checking: Current game_state = {game_state}")


            # def handle_input(self, event):
        #     pass


if __name__ == "__main__":
    game = Game()
    game.loop()