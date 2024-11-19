
import sys
from menu_map.map_creation import *

pygame.init()

# Music
pygame.mixer.music.load('lofi1.mp3')
pygame.mixer.music.play(-1)

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Sets the screen size
pygame.display.set_caption("Thesis Quest")

# Load the menu background image
menu_background = pygame.image.load('menu_assets/Thesis quest.png').convert()

# Load fonts
font_path = "fonts/PressStart2P-Regular.ttf"
font = pygame.font.Font(font_path, 30)
menu_font = pygame.font.Font(font_path, 40)

# Colours
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Start with menu
game_state = "menu"

# Menu options
menu_options = ["Start Game", "Quit"]
selected_option = 0


# Function to display the menu
def display_menu():
    screen.blit(menu_background, (0, 0))
    title_text = menu_font.render("Main Menu", True, WHITE)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 120))

    for i, option in enumerate(menu_options):
        color = PURPLE if i == selected_option else WHITE
        option_text = font.render(option, True, color)
        screen.blit(option_text, (SCREEN_WIDTH // 2 - option_text.get_width() // 2, 200 + i * 60))

    pygame.display.flip()


# Function for menu input
def handle_menu_input(event):
    global selected_option, game_state
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            selected_option = (selected_option + 1) % len(menu_options)  # Cycle through options
        elif event.key == pygame.K_UP:
            selected_option = (selected_option - 1) % len(menu_options)  # Cycle through options
        elif event.key == pygame.K_RETURN:
            if selected_option == 0:  # "Start Game" option
                game_state = "game"  # Transition to the game state
            elif selected_option == 1:  # "Quit" option
                pygame.quit()
                sys.exit()


# Function to start the game (using the game loop from main.py)
def game_loop():
    player_position = pygame.Vector2(530, 410)

    # Load character image and get its rectangle
    character = pygame.image.load('girl64.png').convert_alpha()
    x = character.get_width()
    y = character.get_height()

    clock = pygame.time.Clock()

    # Game loop
    running = True
    while running:
        dt = clock.tick(FPS) / 1000

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
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.flip()  # Updates the display
    pygame.quit()
    sys.exit()


# Main loop for the menu and game transition
def main():
    global game_state, selected_option
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if game_state == "menu":
                handle_menu_input(event)  # Handle menu navigation and selection

        if game_state == "menu":
            display_menu()  # Display the menu screen
        elif game_state == "game":
            game_loop()  # Run the game loop

        pygame.display.flip()  # Update the display each frame
        pygame.time.Clock().tick(60)  # Ensure the game runs at 60 FPS


if __name__ == "__main__":
    main()
