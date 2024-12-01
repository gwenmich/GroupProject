from character_class import Character
from main_config import FPS
from world.game_screen_classes import Screen, MapScreen
import pygame

class Game:
    def __init__(self):
        # self.manager = manager
        self.screen = MapScreen()
        self.player = Character(self.screen.screen, "assets/sprites/girl_sprite.png", 2, "#ff00d6", 64, 64)
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.game_state = "Main Menu"
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

                # if self.game_state == "Main Menu":
                #     self.menu.handle_input(event)
                # elif self.game_state == GameState.GAME:
                #     self.game.handle_input(event)

            if self.game_state == "Main Menu":
                self.menu.display()
            elif self.game_state == "Map":
                self.game.loop()

            self.clock.tick(FPS)

    # def handle_input(self, event):
    #     pass




    def loop(self):

        self.dt = self.clock.tick(FPS)/1000


        # self.manager.screen.fill((0, 200, 110))
        # need function to draw map

        self.player.animate(self.screen)
        self.player.move(250, self.dt)

        pygame.display.flip()





if __name__ == "__main__":

    game = Game()

    game.loop()