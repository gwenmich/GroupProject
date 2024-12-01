from character_class import Character
from main_config import *
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
            self.dt = self.clock.tick(FPS)/1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # if self.game_state == "Main Menu":
                #     self.menu.handle_input(event)
                # elif self.game_state == GameState.GAME:
                #     self.game.handle_input(event)

            self.menu.select_option()

            if game_state == "Main Menu":
                self.menu.display(self.map_screen.screen)
                self.menu.handle_input()
            elif game_state == "Map":
                self.map_screen.draw()
                self.player.animate(self.map_screen.screen)
                self.player.move(250, self.dt)

            # pygame.mixer.music.load('assets/main_menu/mapmusic.mp3')
            # pygame.mixer.music.play(-1)
            pygame.display.flip()


        # def handle_input(self, event):
        #     pass


if __name__ == "__main__":
    game = Game()
    game.loop()