import pygame
import random
import sys
import os


class FoodFight:
    def __init__(self):
        # Initialize Pygame and set up the basics
        pygame.init()

        # Screen settings
        self.WIDTH, self.HEIGHT = 1000, 700
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.victory_status = "Not won"
        self.player_location = "cafeteria"

        # Pastel color palette
        self.PASTEL_PINK = (255, 182, 193)
        self.PASTEL_BLUE = (120, 150, 200)
        self.PASTEL_PURPLE = (216, 191, 216)
        self.PASTEL_YELLOW = (255, 255, 153)
        self.PASTEL_GREEN = (120, 201, 120)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)

        # Load fonts
        try:
            self.PIXEL_FONT = pygame.font.Font("assets/fight_quiz/PressStart2P-Regular.ttf", 14)
            self.PIXEL_LARGE_FONT = pygame.font.Font("assets/fight_quiz/PressStart2P-Regular.ttf", 40)
        except FileNotFoundError:
            self.PIXEL_FONT = pygame.font.SysFont('Arial', 12)
            self.PIXEL_LARGE_FONT = pygame.font.SysFont('Arial', 16)

        # Load images with better error handling
        self.FULL_HEART = None
        self.EMPTY_HEART = None
        self.CABBAGE_IMG = None
        self.RED_APPLE_IMG = None
        self.GREEN_APPLE_IMG = None

        try:
            self.FULL_HEART = pygame.image.load("assets/fight_quiz/full_heart.png").convert_alpha()
            self.EMPTY_HEART = pygame.image.load("assets/fight_quiz/empty_heart.png").convert_alpha()
            self.CABBAGE_IMG = pygame.image.load("assets/fight_quiz/cabbage.png").convert_alpha()
            self.RED_APPLE_IMG = pygame.image.load("assets/fight_quiz/red_apple.png").convert_alpha()
            self.GREEN_APPLE_IMG = pygame.image.load("assets/fight_quiz/green_apple.png").convert_alpha()
        except FileNotFoundError as e:
            print(f"Error loading image: {e}")

        if self.FULL_HEART:
            self.FULL_HEART = pygame.transform.scale(self.FULL_HEART, (50, 50))
        if self.EMPTY_HEART:
            self.EMPTY_HEART = pygame.transform.scale(self.EMPTY_HEART, (50, 50))
        if self.CABBAGE_IMG:
            self.CABBAGE_IMG = pygame.transform.scale(self.CABBAGE_IMG, (50, 50))
        if self.RED_APPLE_IMG:
            self.RED_APPLE_IMG = pygame.transform.scale(self.RED_APPLE_IMG, (50, 50))
        if self.GREEN_APPLE_IMG:
            self.GREEN_APPLE_IMG = pygame.transform.scale(self.GREEN_APPLE_IMG, (50, 50))


        # Game variables
        self.PLAYER_LIVES = 3
        self.ENEMY_LIVES = 3
        self.player_lives = self.PLAYER_LIVES
        self.enemy_lives = self.ENEMY_LIVES
        self.coffee_used = False


        self.PLAYER_FOOD = {
            "Broccoli": {"damage": (5, 15), "message": "Broccoli lands in student's hair!"},
            "Carrot": {"damage": (8, 12), "message": "Carrot pokes student's eye!"},
            "Soup": {"damage": (10, 20), "message": "Soup splashes - student loses balance!"},
        }

        self.ENEMY_FOOD = {
            "Broccoli": {"damage": (5, 15), "message": "Broccoli sticks to your shirt!"},
            "Carrot": {"damage": (8, 12), "message": "Carrot thrown accurately!"},
            "Soup": {"damage": (10, 20), "message": "Hot soup scalds slightly!"},
        }

        self.game_over = False
        self.turn_ended = False
        self.message = ["You enter the cafeteria and see a student yelling at a worker!",
                        "Salad? I need sugar if I'm going to study!"]
        self.bottom_message = "The student chooses what to throw!"
        self.instructions_displayed = True

        self.running = True


    def draw_text(self, surface, text, x, y, font, color=(120, 150, 200), line_height=30):
        if isinstance(text, list):
            for i, line in enumerate(text):
                text_surface = font.render(line, True, color)
                surface.blit(text_surface, (x, y + i * line_height))
        else:
            text_surface = font.render(text, True, color)
            surface.blit(text_surface, (x, y))


    def draw_hearts(self, x, y, lives, max_lives):
        for i in range(max_lives):
            heart_img = self.FULL_HEART if i < lives else self.EMPTY_HEART
            self.screen.blit(heart_img, (x + i * 40, y))

    def player_turn(self, food_type):

        self.turn_ended = True
        if food_type == "Coffee" and not self.coffee_used:
            self.coffee_used = True
            self.bottom_message = "Coffee drunk! Reflexes enhanced! Turn Over."
        elif food_type == "Food Tray":
            self.bottom_message = "Blocked with food tray! Turn Over."
        elif food_type in self.PLAYER_FOOD:
            damage = random.randint(*self.PLAYER_FOOD[food_type]["damage"])
            self.enemy_lives -= 1
            self.bottom_message = f"{self.PLAYER_FOOD[food_type]['message']} Damage dealt: {damage}. Turn Over."

        if self.enemy_lives <= 0:
            self.game_over = True

    def enemy_turn(self):
        food_choice = random.choice(list(self.ENEMY_FOOD.keys()))
        action = random.choice(["Attack", "Block", "Dodge"])  # Randomized actions for the student

        self.turn_ended = False
        if action == "Attack":
            damage = random.randint(*self.ENEMY_FOOD[food_choice]["damage"])
            self.player_lives -= 1
            self.bottom_message = f"{self.ENEMY_FOOD[food_choice]['message']} You took {damage} damage!"
        elif action == "Block":
            self.bottom_message = "Student blocks with lunch tray!"
        else:
            self.bottom_message = "Student dodges your attack!"

        if self.player_lives <= 0:
            self.game_over = True

    def draw_game(self):
        # Set the background to pastel pink for a cute aesthetic
        self.screen.fill(self.PASTEL_PINK)
        if self.CABBAGE_IMG:
            self.screen.blit(self.CABBAGE_IMG, (20, 20))
        if self.RED_APPLE_IMG:
            self.screen.blit(self.RED_APPLE_IMG, (self.WIDTH - 70, 20))
        if self.GREEN_APPLE_IMG:
            self.screen.blit(self.GREEN_APPLE_IMG, (20, self.HEIGHT - 70))

        self.draw_hearts(70, 20, self.player_lives, self.PLAYER_LIVES)
        self.draw_hearts(800, 20, self.enemy_lives, self.ENEMY_LIVES)

        if self.instructions_displayed:
            self.draw_text(self.screen, self.message, 50, 150, self.PIXEL_FONT, self.PASTEL_BLUE)
            self.draw_text(self.screen, "Press any key to start!", 50, 240, self.PIXEL_FONT, self.PASTEL_YELLOW)
        else:
            self.draw_text(self.screen, "Your Actions:", 50, 100, self.PIXEL_FONT, self.PASTEL_BLUE)
            actions = list(self.PLAYER_FOOD.keys()) + ["Coffee", "Food Tray"]
            for i, action in enumerate(actions):
                if action in self.PLAYER_FOOD:
                    damage_text = f"(Dmg: {self.PLAYER_FOOD[action]['damage'][0]}-{self.PLAYER_FOOD[action]['damage'][1]})"
                else:
                    damage_text = ""
                self.draw_text(self.screen, f"{i + 1}. {action} {damage_text}", 50, 140 + i * 30, self.PIXEL_FONT,
                               self.PASTEL_YELLOW)

            self.draw_text(self.screen, self.bottom_message, 50, 500, self.PIXEL_FONT, self.WHITE)

        if self.game_over:
            self.screen.fill(self.PASTEL_PINK)
            result_text = "You lost the food fight!" if self.player_lives <= 0 else "You won the food fight!"
            self.draw_text(self.screen, result_text, self.WIDTH // 2 - 430, self.HEIGHT // 2 - 50,
                           self.PIXEL_LARGE_FONT, self.RED)
            if self.player_lives >0:
                self.draw_text(self.screen, "Press E to quit!", self.WIDTH // 2 -100,
                               self.HEIGHT // 2 + 50, self.PIXEL_FONT, self.WHITE)
            else:
                self.draw_text(self.screen, "Press R to play again or E to quit!", self.WIDTH // 2 - 240,
                               self.HEIGHT // 2 + 50, self.PIXEL_FONT, self.WHITE)

            if self.player_lives >= 0:
                self.victory_status = "Win"


        pygame.display.flip()

    def reset_game(self):
        self.player_lives = self.PLAYER_LIVES
        self.enemy_lives = self.ENEMY_LIVES
        self.game_over = False
        self.coffee_used = False
        self.turn_ended = False
        self.bottom_message = "Another round begins!"
        self.instructions_displayed = True

    # Load background music
    def load_music(self):
        pygame.mixer.music.load("assets/fight_quiz/battle.mp3")
        pygame.mixer.music.play(-1)


    # Game loop
    def play(self):
        pygame.display.set_caption("Cafeteria Food Fight!") # Game title
        self.load_music()
        self.running = True
        while self.running:
            self.draw_game()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if self.instructions_displayed:
                        self.instructions_displayed = False
                    elif self.game_over:
                        if event.key == pygame.K_r:
                            self.reset_game()
                        elif event.key == pygame.K_e:
                            self.player_location = "Map"
                            self.running = False
                    elif not self.turn_ended:
                        if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5]:
                            action = ["Broccoli", "Carrot", "Soup", "Coffee", "Food Tray"][event.key - pygame.K_1]
                            self.player_turn(action)
                    else:
                        self.enemy_turn()

        return self.victory_status

        # pygame.quit()
        # sys.exit()

if __name__ == "__main__":
    game = FoodFight()
    game.play()
