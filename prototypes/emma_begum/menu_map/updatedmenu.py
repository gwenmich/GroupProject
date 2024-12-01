import sys
from menu_map.map_creation import *

pygame.init()

# Display
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)
FPS = 60

# Game states
class GameState:
    MAIN_MENU = "main_menu"
    GAME = "game"

# Game Manager
class GameManager:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Thesis Quest")
        self.clock = pygame.time.Clock()
        self.game_state = GameState.MAIN_MENU
        self.selected_option = 0
        self.menu = Menu(self)
        self.game = Game(self)
        self.setup_music()

    def setup_music(self):
        pygame.mixer.music.load('prototypes/emma_begum/menu_map/music/lofi1.mp3')
        pygame.mixer.music.play(-1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.game_state == GameState.MAIN_MENU:
                    self.menu.handle_input(event)
                elif self.game_state == GameState.GAME:
                    self.game.handle_input(event)

            if self.game_state == GameState.MAIN_MENU:
                self.menu.display()
            elif self.game_state == GameState.GAME:
                self.game.loop()

            self.clock.tick(FPS)

# Menu
class Menu:
    def __init__(self, manager):
        self.manager = manager
        self.font_path = "assets/main_menu/PressStart2P-Regular.ttf"
        self.title_font = pygame.font.Font(self.font_path, 40)
        self.option_font = pygame.font.Font(self.font_path, 30)
        self.click_sound = pygame.mixer.Sound('assets/main_menu/click.mp3')
        self.start_sound = pygame.mixer.Sound('assets/main_menu/starts.mp3')
        self.menu_options = ["Start Game", "High Scores", "Quit"]
        self.menu_background = pygame.image.load('assets/main_menu/thesisquest.png').convert()

    def display(self):
        self.manager.screen.blit(self.menu_background, (0, 0))
        title_text = self.title_font.render("Main Menu", True, WHITE)
        self.manager.screen.blit(
            title_text,
            (
                SCREEN_WIDTH // 2 - title_text.get_width() // 2,
                120,
            ),
        )

        for i, option in enumerate(self.menu_options):
            color = PURPLE if i == self.manager.selected_option else WHITE
            option_text = self.option_font.render(option, True, color)
            self.manager.screen.blit(
                option_text,
                (
                    SCREEN_WIDTH // 2 - option_text.get_width() // 2,
                    180 + i * 45,
                ),
            )

        pygame.display.flip()

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.click_sound.play()
                self.manager.selected_option = (self.manager.selected_option + 1) % len(self.menu_options)
            elif event.key == pygame.K_UP:
                self.click_sound.play()
                self.manager.selected_option = (self.manager.selected_option - 1) % len(self.menu_options)
            elif event.key == pygame.K_RETURN:
                self.start_sound.play()
                self.select_option()

    def select_option(self):
        if self.manager.selected_option == 0:  # Start Game
            self.manager.game_state = GameState.GAME
            pygame.mixer.music.load('assets/main_menu/mapmusic.mp3')
            pygame.mixer.music.play(-1)
        elif self.manager.selected_option == 1:  # High Scores
            pass  # Add functionality
        elif self.manager.selected_option == 2:  # Quit
            pygame.quit()
            sys.exit()

# Game Map
class Game:
    def __init__(self, manager):
        self.manager = manager
        self.player_position = pygame.Vector2(530, 410)
        self.character = pygame.image.load('girl64.png').convert_alpha()
        self.character_rect = self.character.get_rect(center=self.player_position)
        self.speed = 250

    def loop(self):
        dt = self.manager.clock.tick(FPS) / 1000
        self.character_rect = self.character.get_rect(center=self.player_position)

        self.manager.screen.fill((0, 200, 110))
        draw_tile_map()
        self.manager.screen.blit(self.character, self.character_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.character_rect.y > 0:
            self.player_position.y -= self.speed * dt
        if keys[pygame.K_DOWN] and self.character_rect.y < SCREEN_HEIGHT - self.character_rect.height:
            self.player_position.y += self.speed * dt
        if keys[pygame.K_LEFT] and self.character_rect.x > 0:
            self.player_position.x -= self.speed * dt
        if keys[pygame.K_RIGHT] and self.character_rect.x < SCREEN_WIDTH - self.character_rect.width:
            self.player_position.x += self.speed * dt

        pygame.display.flip()

    def handle_input(self, event):
        pass

if __name__ == "__main__":
    game_manager = GameManager()
    game_manager.run()
