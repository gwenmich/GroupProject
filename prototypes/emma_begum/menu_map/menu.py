import sys
from menu_map.map_creation import *

pygame.init()

# Music
pygame.mixer.music.load('music/lofi1.mp3')
pygame.mixer.music.play(-1)

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Thesis Quest")

# Menu background image
menu_background = pygame.image.load('menu_assets/thesisquest.png').convert()
# Pause background image
pause_background = pygame.image.load('menu_assets/pause.png').convert()

# Menu font
font_path = "fonts/PressStart2P-Regular.ttf"
font = pygame.font.Font(font_path, 30)
menu_font = pygame.font.Font(font_path, 40)

# Colours
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Sounds
click_sound = pygame.mixer.Sound('music/click.mp3')
start_sound = pygame.mixer.Sound('music/starts.mp3')

# Game states
game_state = "main_menu"

# Menu options
menu_options = ["Start Game", "High Scores", "Quit"]
pause_options = ["Resume Game","Main Menu", "Quit"]
selected_option = 0

def display_menu():
    if game_state == "main_menu":
        screen.blit(menu_background, (0, 0))  # Main menu background
        title_text = menu_font.render("Main Menu", True, WHITE)
        options = menu_options
    elif game_state == "pause_menu":
        screen.blit(pause_background, (0, 0))  # Pause menu background
        title_text = menu_font.render("Pause Menu", True, WHITE)
        options = pause_options


    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 120))


    for i, option in enumerate(options):
        color = PURPLE if i == selected_option else WHITE
        option_text = font.render(option, True, color)
        screen.blit(option_text, (SCREEN_WIDTH // 2 - option_text.get_width() // 2, 180 + i * 45))

    pygame.display.flip()

    for i, option in enumerate(options):
        color = PURPLE if i == selected_option else WHITE
        option_text = font.render(option, True, color)
        screen.blit(option_text, (SCREEN_WIDTH // 2 - option_text.get_width() // 2, 180 + i * 45))

    pygame.display.flip()

# Function for menu input
def handle_menu_input(event):
    global selected_option, game_state
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            click_sound.play()
            selected_option = (selected_option + 1) % len(menu_options if game_state == "main_menu" else pause_options)
        elif event.key == pygame.K_UP:
            click_sound.play()
            selected_option = (selected_option - 1) % len(menu_options if game_state == "main_menu" else pause_options)
        elif event.key == pygame.K_RETURN:
            start_sound.play()
            if game_state == "main_menu":
                if selected_option == 0:  # "Start Game"
                    game_state = "game"
                    pygame.mixer.music.load('music/mapmusic.mp3')
                    pygame.mixer.music.play(-1)
                    game_state = "game"  # Transition to the game state
                elif selected_option == 1:  # High Scores goes here

                    pass
                elif selected_option == 2:  # "Quit"
                    pygame.quit()
                    sys.exit()
            elif game_state == "pause_menu":
                if selected_option == 0:  # "Resume Game"
                    game_state = "game"  # Resume game
                elif selected_option == 1:  # "Main Menu"
                    game_state = "main_menu"  # Go back to main menu
                    pygame.mixer.music.load('music/lofi1.mp3')
                    pygame.mixer.music.play(-1)
                elif selected_option == 2:  # "Quit"
                    pygame.quit()
                    sys.exit()


# Function to start the game (using the game loop from main.py)
def game_loop():
    global game_state
    player_position = pygame.Vector2(530, 410)

    # Load character
    character = pygame.image.load('girl64.png').convert_alpha()
    x = character.get_width()
    y = character.get_height()

    clock = pygame.time.Clock()

    # Game loop
    while game_state == "game":
        dt = clock.tick(60) / 1000

        character_rect = character.get_rect(center=player_position)

        screen.fill((0, 200, 110))
        draw_tile_map()  # Function in map_creation.py
        screen.blit(character, character_rect)

        keyboard = pygame.key.get_pressed()

        if keyboard[pygame.K_UP] and character_rect.y > 0:
            player_position.y -= 250 * dt
        if keyboard[pygame.K_DOWN] and character_rect.y < SCREEN_HEIGHT - y:
            player_position.y += 250 * dt
        if keyboard[pygame.K_LEFT] and character_rect.x > 0:
            player_position.x -= 250 * dt
        if keyboard[pygame.K_RIGHT] and character_rect.x < SCREEN_WIDTH - x:
            player_position.x += 250 * dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_state = "pause_menu"  # Switch to pause menu
                    return

        pygame.display.flip()  # Updates display


# Main loop for managing game state
def main():
    global game_state, selected_option
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if game_state in ["main_menu", "pause_menu"]:
                handle_menu_input(event)

        if game_state in ["main_menu", "pause_menu"]:
            display_menu()
        elif game_state == "game":
            game_loop()

        pygame.time.Clock().tick(60)  # Ensures game runs at 60 FPS


if __name__ == "__main__":
    main()