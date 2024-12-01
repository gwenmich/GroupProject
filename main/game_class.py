from character_class import Character
from main_config import FPS, game_state
from world.game_over_screen import GameOverScreen
from world.game_screen_classes import MapScreen
import pygame
from menu_class import Menu
import sys
from world.high_scores_screen import HighScoreScreen
from utilities.timer import Timer
from utilities.bars_classes import StressBar, GamesBar


class Game:
    def __init__(self):
        # self.manager = manager
        self.map_screen = MapScreen()
        self.menu = Menu()
        self.player = Character(self.map_screen.screen, "assets/sprites/girl_sprite.png", 2, "#ff00d6", 64, 64)
        self.clock = pygame.time.Clock()
        self.dt = 0
        # self.game = Game(self)
        # instantiating Bar Class and giving coordinates
        self.stress_bar = StressBar(900, 23, 70, 16, 100)
        self.games_bar = GamesBar(510, 23, 70, 16, 4)
        # instantiating Timer and passing timer duration
        self.timer = Timer(1800)
        # creating a pygame for to set how often timer updates, every second
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.high_scores = HighScoreScreen()
        self.game_over = GameOverScreen()




    def loop(self):
        while True:
            global game_state
            self.dt = self.clock.tick(FPS)/1000

            print(f"Before checking: Current game_state = {game_state}")


            if game_state == "Main Menu":
                print(f"In Main Menu state.")
                self.menu.display(self.map_screen.screen)
                self.menu.handle_input()
                # So this is where if checks if the game_state is diferent than the menu specifc variable and if so updates
                if game_state != self.menu.next_game_state:
                    print(f"Game state updated to: {self.menu.next_game_state}")
                    game_state = self.menu.next_game_state
                    # the set the menu variable back to default
                    self.menu.next_game_state = "Main Menu"
            elif game_state == "High Scores":
                print(f"In High Scores state.")
                self.high_scores.draw()
                self.high_scores.handler()
                if game_state != self.high_scores.menu:
                    print(f"Game state updated to: {self.high_scores.menu}")
                    game_state = self.high_scores.menu
                    self.high_scores.menu = "High Scores"
            elif game_state == "Map":
                print(f"In Map state.")
                self.map_screen.draw()
                self.map_screen.handler()
                self.player.animate(self.map_screen.screen)
                self.player.move(250, self.dt)
                # drawing the bars and timers and the matching texts
                self.stress_bar.draw(self.map_screen.screen)
                self.stress_bar.draw_text(self.map_screen.screen)
                self.games_bar.draw(self.map_screen.screen)
                self.games_bar.draw_text(self.map_screen.screen)

                self.timer.countdown(self.map_screen.screen)
            elif game_state == "Victory":
                print(f"In Game over state state.")
                self.game_over.draw()
                self.game_over.handler()

            elif game_state == "Game Over":
                print(f"In Game over state state.")
                self.game_over.draw()
                self.game_over.handler()




            # pygame.mixer.music.load('assets/main_menu/mapmusic.mp3')
            # pygame.mixer.music.play(-1)
            pygame.display.flip()

            print(f"After checking: Current game_state = {game_state}")


            # def handle_input(self, event):
        #     pass


if __name__ == "__main__":
    game = Game()
    game.loop()