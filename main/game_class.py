from character_class import Character
from main_config import FPS, game_state
from world.game_screen_classes import MapScreen
import pygame
from menu_class import Menu
import sys

class Game:
    def __init__(self):
        # self.manager = manager
        self.map_screen = MapScreen()
        self.menu = Menu()
        self.player = Character(self.map_screen.screen, "assets/sprites/girl_sprite.png", 2, "#ff00d6", 64, 64)
        self.clock = pygame.time.Clock()
        self.dt = 0
        # self.game = Game(self)



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
            elif game_state == "Map":
                print(f"In Map state.")
                self.map_screen.draw()
                self.player.animate(self.map_screen.screen)
                self.player.move(250, self.dt)
            elif game_state == "Game Over":

            # pygame.mixer.music.load('assets/main_menu/mapmusic.mp3')
            # pygame.mixer.music.play(-1)
            pygame.display.flip()

            print(f"After checking: Current game_state = {game_state}")


            # def handle_input(self, event):
        #     pass


if __name__ == "__main__":
    game = Game()
    game.loop()