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
from prototypes.ines_duarte.random_useful_code import hitbox_visible_square
from utilities.intro_bubble import IntroBubble
from Quizgame import QuizGame
from typing_game import TypingGame


class Game:
    def __init__(self):
        # self.manager = manager
        self.map_screen = MapScreen()
        self.menu = Menu()
        self.player = Character(self.map_screen.screen, "assets/sprites/girl_sprite.png", 2, "#ff00d6", 64, 64)
        self.clock = pygame.time.Clock()
        self.dt = 0
        # instantiating Bar Class and giving coordinates
        self.stress_bar = StressBar(900, 23, 70, 16, 10)
        self.games_bar = GamesBar(510, 23, 70, 16, 4)
        # instantiating Timer and passing timer duration
        self.timer = Timer(1800)
        # creating a pygame for to set how often timer updates, every second
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.intro_text = IntroBubble(self.map_screen.screen, 125, 30, '')
        self.high_scores = HighScoreScreen()
        self.game_over = GameOverScreen()
        self.library = QuizGame()
        self.classroom = TypingGame(self.map_screen.screen)
        self.games_won = {
        "library": "Not won",
        "cafeteria": "Not won",
        "counselling_office": "Not won",
        "classroom": "Not won",
        "it_dept": "Not won"
    }

    def update_game_status(self, building_name):
        if building_name == "library" and self.games_won["library"] != self.library.victory_status:
            self.games_won["library"] = self.library.victory_status
        # elif building_name == "cafeteria" and self.games_won["cafeteria"] != self.cafeteria.victory_status:
        #     self.games_won["cafeteria"] = self.cafeteria.victory_status
        elif building_name == "classroom" and self.games_won["classroom"] != self.classroom.victory_status:
            self.games_won["classroom"] = self.classroom.victory_status
        # elif building_name == "it_dept" and self.games_won["it_dept"] != self.it_dept.victory_status:
        #     self.games_won["it_dept"] = self.it_dept.victory_status

    def loop(self):
        while True:
            global game_state

            self.dt = self.clock.tick(FPS)/1000

            # print(f"Before checking: Current game_state = {game_state}")
            # check to bring player back to map, excluding menu
            if game_state != "Main Menu" and game_state != self.player.character_location:
                print(f"Game state updated to: {self.player.character_location}")
                game_state = self.player.character_location
                if self.player.character_location != "Map":
                    self.player.character_location = "Map"

            # Victory status logic
            self.update_game_status("library")
            # self.update_game_status("cafeteria")
            self.update_game_status("classroom")
            # self.update_game_status("it_dept")

            # main game_state engine
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
                self.dt = self.clock.tick(FPS) / 1000
                # print(f"In Map state.")
                self.map_screen.draw()
                self.map_screen.handler()
                self.player.animate(self.map_screen.screen)
                self.player.move(400, self.dt)
                # drawing the bars and timers and the matching texts
                # stress bars
                self.stress_bar.draw(self.map_screen.screen)
                self.stress_bar.draw_text(self.map_screen.screen)
                # Challenge wins
                self.games_bar.draw(self.map_screen.screen)
                self.games_bar.draw_text(self.map_screen.screen)
                # timer
                self.timer.countdown(self.map_screen.screen)
                hitbox_visible_square(self.map_screen.screen, 797, 540, 10, 50)
                # self.intro_text.draw()
                # self.intro_text.handler()
                for event in pygame.event.get():
                    if event.type == pygame.USEREVENT:
                       self.timer.timer_duration -= 1

                # check to trigger building state update
            elif game_state == "library" and self.games_won["library"] == "Not won":
                self.stress_bar.update()
                print(f"In library state.")
                self.library.main()
                print(f"After library.main(): game_state = {game_state}, player_location = {self.library.player_location}")
                if game_state != self.library.player_location:
                     self.player.player_position.y += 10
                     self.player.character_rect.topleft = self.player.player_position
                     print(f"Game state updated to: {self.library.player_location}")
                     game_state = self.library.player_location

            elif game_state == "classroom" and self.games_won["classroom"] == "Not won":
                self.stress_bar.update()
                print(f"In classroom state.")
                self.classroom.run()
                if game_state != self.classroom.player_location:
                     self.player.player_position.y += 10
                     self.player.character_rect.topleft = self.player.player_position
                     print(f"Game state updated to: {self.classroom.player_location}")
                     game_state = self.classroom.player_location

            elif game_state == "Victory":
                print(f"In Game victory state.")
                self.game_over.draw()
                self.game_over.handler()

            elif game_state == "Game Over":
                print(f"In Game over state state.")
                self.game_over.draw()
                self.game_over.handler()



            # pygame.mixer.music.load('assets/main_menu/mapmusic.mp3')
            # pygame.mixer.music.play(-1)
            pygame.display.flip()


            # print(f"After checking: Current game_state = {game_state}")



if __name__ == "__main__":
    game = Game()
    game.loop()