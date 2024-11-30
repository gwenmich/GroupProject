import pygame
import random
import sys
import os

# Initialize Pygame and set up the basics
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cafeteria Food Fight!")  # Game title

# Pastel color palette
PASTEL_PINK = (255, 182, 193)
PASTEL_BLUE = (173, 216, 230)
PASTEL_PURPLE = (216, 191, 216)
PASTEL_YELLOW = (255, 255, 153)
PASTEL_GREEN = (152, 251, 152)
DARK_BLUE = (25, 25, 112)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Load fonts
try:
    PIXEL_FONT = pygame.font.Font("PressStart2P-Regular.ttf", 12)
    PIXEL_LARGE_FONT = pygame.font.Font("PressStart2P-Regular.ttf", 16)
except FileNotFoundError:
    PIXEL_FONT = pygame.font.SysFont('Arial', 12)
    PIXEL_LARGE_FONT = pygame.font.SysFont('Arial', 16)

# Load images with better error handling
FULL_HEART = None
EMPTY_HEART = None
CABBAGE_IMG = None
RED_APPLE_IMG = None
GREEN_APPLE_IMG = None

try:
    FULL_HEART = pygame.image.load("full_heart.png").convert_alpha()
    EMPTY_HEART = pygame.image.load("empty_heart.png").convert_alpha()
    CABBAGE_IMG = pygame.image.load("cabbage.png").convert_alpha()
    RED_APPLE_IMG = pygame.image.load("red_apple.png").convert_alpha()
    GREEN_APPLE_IMG = pygame.image.load("green_apple.png").convert_alpha()
except FileNotFoundError as e:
    print(f"Error loading image: {e}")

if FULL_HEART:
    FULL_HEART = pygame.transform.scale(FULL_HEART, (30, 30))
if EMPTY_HEART:
    EMPTY_HEART = pygame.transform.scale(EMPTY_HEART, (30, 30))
if CABBAGE_IMG:
    CABBAGE_IMG = pygame.transform.scale(CABBAGE_IMG, (50, 50))
if RED_APPLE_IMG:
    RED_APPLE_IMG = pygame.transform.scale(RED_APPLE_IMG, (50, 50))
if GREEN_APPLE_IMG:
    GREEN_APPLE_IMG = pygame.transform.scale(GREEN_APPLE_IMG, (50, 50))

# Load background music
try:
    pygame.mixer.music.load("battle.mp3")
    pygame.mixer.music.play(-1)
except FileNotFoundError:
    print("Error: Failed to load 'battle.mp3'. Ensure the file exists in the correct path.")

# Game variables
PLAYER_LIVES = 3
ENEMY_LIVES = 3
player_lives = PLAYER_LIVES
enemy_lives = ENEMY_LIVES
coffee_used = False

PLAYER_FOOD = {
    "Broccoli": {"damage": (5, 15), "message": "Broccoli lands in student's hair!"},
    "Carrot": {"damage": (8, 12), "message": "Carrot pokes student's eye!"},
    "Soup": {"damage": (10, 20), "message": "Soup splashes - student loses balance!"},
}

ENEMY_FOOD = {
    "Broccoli": {"damage": (5, 15), "message": "Broccoli sticks to your shirt!"},
    "Carrot": {"damage": (8, 12), "message": "Carrot thrown accurately!"},
    "Soup": {"damage": (10, 20), "message": "Hot soup scalds slightly!"},
}

game_over = False
turn_ended = False
message = ["You enter the cafeteria and see a student yelling at a worker!",
           "Salad? I need sugar if I'm going to study!"]
bottom_message = "The student chooses what to throw!"
instructions_displayed = True

# Define the running state at the module level
running = True


def draw_text(surface, text, x, y, font, color=PASTEL_BLUE, line_height=20):
    if isinstance(text, list):
        for i, line in enumerate(text):
            text_surface = font.render(line, True, color)
            surface.blit(text_surface, (x, y + i * line_height))
    else:
        text_surface = font.render(text, True, color)
        surface.blit(text_surface, (x, y))


def draw_hearts(x, y, lives, max_lives):
    for i in range(max_lives):
        heart_img = FULL_HEART if i < lives else EMPTY_HEART
        screen.blit(heart_img, (x + i * 40, y))


def player_turn(food_type):
    global enemy_lives, coffee_used, bottom_message, turn_ended, game_over

    turn_ended = True
    if food_type == "Coffee" and not coffee_used:
        coffee_used = True
        bottom_message = "Coffee drunk! Reflexes enhanced! Turn Over."
    elif food_type == "Food Tray":
        bottom_message = "Blocked with food tray! Turn Over."
    elif food_type in PLAYER_FOOD:
        damage = random.randint(*PLAYER_FOOD[food_type]["damage"])
        enemy_lives -= 1
        bottom_message = f"{PLAYER_FOOD[food_type]['message']} Damage dealt: {damage}. Turn Over."

    if enemy_lives <= 0:
        game_over = True


def enemy_turn():
    global player_lives, bottom_message, turn_ended, game_over

    food_choice = random.choice(list(ENEMY_FOOD.keys()))
    action = random.choice(["Attack", "Block", "Dodge"])  # Randomized actions for the student

    turn_ended = False
    if action == "Attack":
        damage = random.randint(*ENEMY_FOOD[food_choice]["damage"])
        player_lives -= 1
        bottom_message = f"{ENEMY_FOOD[food_choice]['message']} You took {damage} damage!"
    elif action == "Block":
        bottom_message = "Student blocks with lunch tray!"
    else:
        bottom_message = "Student dodges your attack!"

    if player_lives <= 0:
        game_over = True


def draw_game():
    # Set the background to pastel pink for a cute aesthetic
    screen.fill(PASTEL_PINK)
    if CABBAGE_IMG:
        screen.blit(CABBAGE_IMG, (20, 20))
    if RED_APPLE_IMG:
        screen.blit(RED_APPLE_IMG, (WIDTH - 70, 20))
    if GREEN_APPLE_IMG:
        screen.blit(GREEN_APPLE_IMG, (20, HEIGHT - 70))

    draw_hearts(50, 20, player_lives, PLAYER_LIVES)
    draw_hearts(600, 20, enemy_lives, ENEMY_LIVES)

    if instructions_displayed:
        draw_text(screen, message, 50, 150, PIXEL_FONT, PASTEL_BLUE)
        draw_text(screen, "Press any key to start!", 50, 200, PIXEL_FONT, PASTEL_GREEN)
    else:
        draw_text(screen, "Your Actions:", 50, 100, PIXEL_FONT, PASTEL_BLUE)
        actions = list(PLAYER_FOOD.keys()) + ["Coffee", "Food Tray"]
        for i, action in enumerate(actions):
            if action in PLAYER_FOOD:
                damage_text = f"(Dmg: {PLAYER_FOOD[action]['damage'][0]}-{PLAYER_FOOD[action]['damage'][1]})"
            else:
                damage_text = ""
            draw_text(screen, f"{i + 1}. {action} {damage_text}", 50, 140 + i * 30, PIXEL_FONT, PASTEL_YELLOW)

        draw_text(screen, bottom_message, 50, 500, PIXEL_FONT, WHITE)

    if game_over:
        screen.fill(PASTEL_PINK)
        result_text = "You lost the food fight!" if player_lives <= 0 else "You won the food fight!"
        draw_text(screen, result_text, WIDTH // 2 - 200, HEIGHT // 2 - 50, PIXEL_LARGE_FONT, RED)
        draw_text(screen, "Press R to play again or Q to quit!", WIDTH // 2 - 200, HEIGHT // 2 + 50, PIXEL_FONT, WHITE)

    pygame.display.flip()


def reset_game():
    global player_lives, enemy_lives, game_over, coffee_used, bottom_message, instructions_displayed, turn_ended
    player_lives = PLAYER_LIVES
    enemy_lives = ENEMY_LIVES
    game_over = False
    coffee_used = False
    turn_ended = False
    bottom_message = "Another round begins!"
    instructions_displayed = True


def main():
    global running, player_lives, enemy_lives, game_over, turn_ended, instructions_displayed

    running = True
    while running:
        draw_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if instructions_displayed:
                    instructions_displayed = False
                elif game_over:
                    if event.key == pygame.K_r:
                        reset_game()
                    elif event.key == pygame.K_q:
                        running = False
                elif not turn_ended:
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5]:
                        action = ["Broccoli", "Carrot", "Soup", "Coffee", "Food Tray"][event.key - pygame.K_1]
                        player_turn(action)
                else:
                    enemy_turn()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
