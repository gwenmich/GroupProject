import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cafeteria Food Fight!")

# Colors
LILAC = (200, 162, 200)
DARK_BLUE = (25, 25, 112)
GREEN = (0, 255, 0)
PURPLE = (138, 43, 226)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Fonts (Smaller font size)
try:
    PIXEL_FONT = pygame.font.Font("PressStart2P-Regular.ttf", 10)
    PIXEL_LARGE_FONT = pygame.font.Font("PressStart2P-Regular.ttf", 14)
except FileNotFoundError:
    # Fallback font
    PIXEL_FONT = pygame.font.SysFont("arial", 10)
    PIXEL_LARGE_FONT = pygame.font.SysFont("arial", 14)

# Load heart images
try:
    FULL_HEART = pygame.image.load("full_heart.png").convert_alpha()
    EMPTY_HEART = pygame.image.load("empty_heart.png").convert_alpha()
except (pygame.error, FileNotFoundError):
    # Fallback heart images
    FULL_HEART = pygame.Surface((30, 30), pygame.SRCALPHA)
    FULL_HEART.fill((255, 0, 0, 128))
    EMPTY_HEART = pygame.Surface((30, 30), pygame.SRCALPHA)
    EMPTY_HEART.fill((100, 100, 100, 128))

# Load food assets
try:
    CABBAGE_IMG = pygame.image.load("cabbage.png").convert_alpha()
    RED_APPLE_IMG = pygame.image.load("red_apple.png").convert_alpha()
    GREEN_APPLE_IMG = pygame.image.load("green_apple.png").convert_alpha()
except (pygame.error, FileNotFoundError):
    # Fallback food images
    CABBAGE_IMG = pygame.Surface((50, 50), pygame.SRCALPHA)
    CABBAGE_IMG.fill((0, 255, 0, 128))
    RED_APPLE_IMG = pygame.Surface((50, 50), pygame.SRCALPHA)
    RED_APPLE_IMG.fill((255, 0, 0, 128))
    GREEN_APPLE_IMG = pygame.Surface((50, 50), pygame.SRCALPHA)
    GREEN_APPLE_IMG.fill((0, 128, 0, 128))

# Resize food assets for better display
CABBAGE_IMG = pygame.transform.scale(CABBAGE_IMG, (50, 50))
RED_APPLE_IMG = pygame.transform.scale(RED_APPLE_IMG, (50, 50))
GREEN_APPLE_IMG = pygame.transform.scale(GREEN_APPLE_IMG, (50, 50))

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

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Function to draw text with line wrapping
def draw_text(surface, text, x, y, font, color=DARK_BLUE, line_height=20):
    if isinstance(text, list):
        for i, line in enumerate(text):
            text_surface = font.render(line, True, color)
            surface.blit(text_surface, (x, y + i * line_height))
    else:
        text_surface = font.render(text, True, color)
        surface.blit(text_surface, (x, y))

# Draw hearts
def draw_hearts(x, y, lives, max_lives):
    for i in range(max_lives):
        heart_img = FULL_HEART if i < lives else EMPTY_HEART
        screen.blit(pygame.transform.scale(heart_img, (30, 30)), (x + i * 40, y))

# Player's turn logic
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

    # Check for game over
    if enemy_lives <= 0:
        game_over = True
        bottom_message = "You won the food fight!"

# Enemy turn logic
def enemy_turn():
    global player_lives, bottom_message, turn_ended, game_over

    food_choice = random.choice(list(ENEMY_FOOD.keys()))
    action = random.choice(["Attack", "Block", "Dodge"])

    turn_ended = False
    if action == "Attack":
        damage = random.randint(*ENEMY_FOOD[food_choice]["damage"])
        player_lives -= 1
        bottom_message = f"{ENEMY_FOOD[food_choice]['message']} You took {damage} damage!"
    elif action == "Block":
        bottom_message = "Student blocks with lunch tray!"
    else:
        bottom_message = "Student dodges your attack!"

    # Check for game over
    if player_lives <= 0:
        game_over = True
        bottom_message = "You lost the food fight!"

# Draw game screen
def draw_game():
    screen.fill(LILAC)

    # Display food assets in the corners
    screen.blit(RED_APPLE_IMG, (WIDTH - 70, 20))  # Top-right corner
    screen.blit(GREEN_APPLE_IMG, (20, HEIGHT - 70))  # Bottom-left corner
    screen.blit(CABBAGE_IMG, (WIDTH - 70, HEIGHT - 70))  # Bottom-right corner

    # Draw hearts
    draw_hearts(50, 20, player_lives, PLAYER_LIVES)
    draw_hearts(600, 20, enemy_lives, ENEMY_LIVES)

    if instructions_displayed:
        draw_text(screen, message, 50, 150, PIXEL_FONT, PURPLE)
        draw_text(screen, "Press any key to start!", 50, 200, PIXEL_FONT, WHITE)
    else:
        # Draw action menu
        draw_text(screen, "Your Actions:", 50, 100, PIXEL_FONT, PURPLE)
        actions = list(PLAYER_FOOD.keys()) + ["Coffee", "Food Tray"]
        for i, action in enumerate(actions):
            if action in PLAYER_FOOD:
                damage_text = f"(Dmg: {PLAYER_FOOD[action]['damage'][0]}-{PLAYER_FOOD[action]['damage'][1]})"
            else:
                damage_text = ""
            draw_text(screen, f"{i + 1}. {action} {damage_text}", 50, 200 + i * 25, PIXEL_FONT, WHITE)

        draw_text(screen, bottom_message, 50, HEIGHT - 100, PIXEL_LARGE_FONT, WHITE)

    if game_over:
        # Display win screen with options
        draw_text(screen, "You won the food fight!", 50, 100, PIXEL_LARGE_FONT, GREEN)
        draw_text(screen, "Press 'R' to try again or 'Q' to quit.", 50, 150, PIXEL_FONT, WHITE)

    pygame.display.update()

# Reset game function
def reset_game():
    global player_lives, enemy_lives, coffee_used, game_over, turn_ended
    player_lives = PLAYER_LIVES
    enemy_lives = ENEMY_LIVES
    coffee_used = False
    game_over = False
    turn_ended = False
    bottom_message = "The student chooses what to throw!"
    instructions_displayed = True

# Quit game function
def quit_game():
    pygame.quit()
    sys.exit()

# Main game loop
def main():
    global running, instructions_displayed

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
                break

            if event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_r:
                        reset_game()
                    elif event.key == pygame.K_q:
                        quit_game()
                        break
                elif instructions_displayed:
                    instructions_displayed = False
                elif turn_ended:
                    enemy_turn()
                else:
                    actions = list(PLAYER_FOOD.keys()) + ["Coffee", "Food Tray"]
                    if event.key == pygame.K_1:
                        player_turn(actions[0])
                    elif event.key == pygame.K_2:
                        player_turn(actions[1])
                    elif event.key == pygame.K_3:
                        player_turn(actions[2])
                    elif event.key == pygame.K_4:
                        player_turn(actions[3])
                    elif event.key == pygame.K_5:
                        player_turn(actions[4])

        draw_game()

    pygame.quit()
    sys.exit()

# Run the game
if __name__ == "__main__":
    main()
