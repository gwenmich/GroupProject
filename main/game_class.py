from character_class import Character
from main_config import FPS
from world.game_over_screen import GameOverScreen
from world.game_screen_classes import MapScreen
import pygame
from menu_class import Menu
import sys
from world.high_scores_screen import HighScoreScreen
from utilities.timer import Timer
from utilities.bars_classes import StressBar, GamesBar
from utilities.intro_bubble import IntroBubble
from quizgame import QuizGame
from typing_game import TypingGame
from wellbeing_room import WellbeingGame
from maze import MazeGame
from fightgame import FoodFight
from world.victory_screen_screen import VictoryScreen
# from win_class import VictoryScreen

class Game:

    def __init__(self):
        self.map_screen = MapScreen()
        self.menu = Menu()
        self.menu.setup_music()
        self.player = Character(self.map_screen.screen, "assets/sprites/girl_sprite.png", 2, "#ff00d6", 64, 64)
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.game_state = "Main Menu"
        # Instantiating stress and games bars and giving coordinates
        self.stress_bar = StressBar(900, 23, 70, 16, 10)
        self.games_bar = GamesBar(510, 23, 70, 16, 4)
        # Instantiating Timer and passing timer duration
        self.timer = Timer(1800)
        # Creating a pygame for to set how often timer updates, every second
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.intro_text = IntroBubble(self.map_screen.screen, 125, 30, '')
        # Instantiating screens
        self.high_scores = HighScoreScreen()
        self.victory_screen = VictoryScreen()
        self.game_over = GameOverScreen()
        # Instantiating all mini-games
        self.library = QuizGame()
        self.classroom = TypingGame(self.map_screen.screen)
        self.wellbeing_room = WellbeingGame()
        self.it_dept = MazeGame()
        self.cafeteria = FoodFight()
        # Initial state of the main game
        self.state = "Playing"
        self.running = True
        # Start game with all mini-games as Not won
        self.games_won = {
        "library": "Not won",
        "cafeteria": "Not won",
        "wellbeing_room": "Not won",
        "classroom": "Not won",
        "it_dept": "Not won"
    }
        # Dictionary of buildings with challenges needed to win the game
        self.buildings = {
            "library" : self.library,
            "cafeteria" : self.cafeteria,
            "classroom" : self.classroom,
            "it_dept" : self.it_dept
        }

    def update_game_status(self, building_name):
        if building_name in self.buildings:
            building = self.buildings[building_name]
            if self.games_won[building_name] != building.victory_status:
                self.games_won[building_name] = building.victory_status

                if building.victory_status == "Won":
                    self.games_bar.wins += 1
                    self.victory_condition()
                elif building.victory_status == "Lost":
                    self.stress_bar.update()


    def victory_condition(self):
        if self.games_bar.wins == self.games_bar.max_wins:
            self.game_state = "Victory"

    def game_over_condition(self):
        if self.timer.timer_duration <= 0 or self.stress_bar.stress == self.stress_bar.max_stress:
            self.game_state = "Game Over"

    def star_score(self):
        if self.timer.timer_duration >= (self.timer.initial_duration * 2 // 3):
            return "5 Stars"
        elif self.timer.timer_duration >= (self.timer.initial_duration // 3):
            return "4 Stars"
        else:
            return "3 Stars"


    def loop(self):
        while self.running:

            self.dt = self.clock.tick(FPS)/1000

            if self.game_state != "Main Menu" and self.game_state != "High Scores" and self.game_state != self.player.character_location:
                print(f"Game state updated to: {self.player.character_location}")
                self.game_state = self.player.character_location
                if self.player.character_location != "Map":
                    self.player.character_location = "Map"

            # Victory status logic
            self.update_game_status("library")
            self.update_game_status("cafeteria")
            self.update_game_status("classroom")
            self.update_game_status("it_dept")

            self.game_over_condition()

            # Main game_state engine
            if self.game_state == "Main Menu":
                print(f"In Main Menu state.")
                self.menu.display(self.map_screen.screen)
                self.menu.handle_input()
                # Checks if the game_state is different than the menu specific variable and if so updates
                if self.game_state != self.menu.next_game_state:
                    print(f"Game state updated to: {self.menu.next_game_state}")
                    self.game_state = self.menu.next_game_state
                    # Sets the menu variable back to default
                    self.menu.next_game_state = "Main Menu"


            elif self.game_state == "High Scores":
                print(f"In High Scores state.")
                self.high_scores.draw()
                self.high_scores.handler()
                if self.game_state != self.high_scores.menu:
                    print(f"Game state updated to: {self.high_scores.menu}")
                    self.game_state = self.high_scores.menu
                    self.high_scores.menu = "High Scores"


            elif self.game_state == "Map":
                # print(f"In Map state.")
                self.map_screen.draw()
                self.player.animate(self.map_screen.screen)
                self.player.move(400, self.dt)
                # Drawing stress bar with its text
                self.stress_bar.draw(self.map_screen.screen)
                self.stress_bar.draw_text(self.map_screen.screen)
                # Drawing challenges bar with its text
                self.games_bar.draw(self.map_screen.screen)
                self.games_bar.draw_text(self.map_screen.screen)
                # Displaying timer with its text
                self.timer.countdown(self.map_screen.screen)
                self.intro_text.draw()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.intro_text.enter_pressed = True
                        if event.key == pygame.K_ESCAPE:
                            self.running = False
                    if event.type == pygame.USEREVENT:
                        self.timer.timer_duration -= 1

            # Checks if the game state if the wellbeing room
            elif self.game_state == "wellbeing_room":
                pygame.mixer.music.stop()
                self.wellbeing_room.handle_music()
                self.wellbeing_room.play()
                if self.wellbeing_room.player_location == "Map":
                    print("Transitioning to Map...")
                    self.player.character_position.y += 10
                    self.player.character_rect.topleft = self.player.character_position
                    print(f"Game state updated to: {self.wellbeing_room.player_location}")
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("assets/main_menu/mapmusic.mp3")
                    self.game_state = "Map"


            # Checks if the game state matches building and is not won
            elif self.game_state in self.buildings and self.games_won[self.game_state] == "Not won":
                building = self.buildings[self.game_state]
                print(f"In {self.game_state} state.")
                building.play()
                if building.player_location == "Map":
                    print("Transitioning to Map...")
                    self.player.character_position.y += 10
                    self.player.character_rect.topleft = self.player.character_position
                    print(f"Game state updated to: {building.player_location}")
                    self.game_state = "Map"

            elif self.game_state == "Victory":
                print("Games won. In victory state.")
                self.victory_screen.stars = self.victory_screen.star_calculator(self.timer.timer_duration, self.timer.initial_duration)
                self.victory_screen.victory_loop(self.timer.get_time_taken(), self.star_score())

            elif self.game_state == "Game Over":
                print(f"In Game over state state.")
                self.game_over.draw()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_n:
                            pygame.quit()
                            sys.exit()
                        if event.key == pygame.K_y:
                            # if you pick yes, it re/initializes the game, and changes state to main menu to start with menu not map
                            self.__init__()
                            self.game_state = "Main Menu"


            pygame.display.flip()



if __name__ == "__main__":
    game = Game()
    game.loop()