import pygame
import sys
from prototypes.ines_duarte.menus.screen_classes import Screen
from prototypes.ines_duarte.map.map_config import *

DUSTY_PINK = (231, 84, 128)
SKY_BLUE = (135, 206, 235)
DUSTY_YELLOW = (239, 228, 176)
FONT_PATH = "path_to_your_custom_font.ttf"  # Replace with your font file path


class GameOverScreen(Screen):
    def __init__(self):
        super().__init__()
        self.font_large = pygame.font.Font(r"C:\Users\inesd\PycharmProjects\CFGDegree-GroupProjectTeam1\prototypes\ines_duarte\menus\PressStart2P-Regular.ttf", 90)  # Adjust the size as needed
        self.font_medium = pygame.font.Font(r"C:\Users\inesd\PycharmProjects\CFGDegree-GroupProjectTeam1\prototypes\ines_duarte\menus\PressStart2P-Regular.ttf", 40)  # Adjust the size as needed
        self.font_small = pygame.font.Font(r"C:\Users\inesd\PycharmProjects\CFGDegree-GroupProjectTeam1\prototypes\ines_duarte\menus\PressStart2P-Regular.ttf", 15)  # Adjust the size as needed
        self.blink_interval = 450

    def load_image(self, path, size=None):
        image = pygame.image.load(path)
        if size:
            return pygame.transform.scale(image, size)
        return image


    def draw(self, game_state=None):
        self.screen.fill(DUSTY_PINK)
        current_time = pygame.time.get_ticks()

        if (current_time // self.blink_interval) % 2 == 0:
            game_over_text = self.font_large.render("GAME OVER", True, DUSTY_YELLOW)
            self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2,
                                              SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))

        replay = self.font_medium.render("Try again?", True, SKY_BLUE)
        self.screen.blit(replay, (SCREEN_WIDTH // 2 - replay.get_width() // 2, 500))

        yes_no = self.font_small.render("Type y(Yes) or n(No)", True, DUSTY_YELLOW)
        self.screen.blit(yes_no, (SCREEN_WIDTH // 2 - yes_no.get_width() // 2, 570))

        icon = self.load_image(r'C:\Users\inesd\PycharmProjects\CFGDegree-GroupProjectTeam1\prototypes\ines_duarte\menus\menu_assets\stress-test.png', (200, 200))
        self.screen.blit(icon, (SCREEN_WIDTH // 2 - icon.get_width() // 2, 100))


    def menu_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n or event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_y:
                    main()
                    return

def main():
    # Initialize Pygame
    pygame.init()

    # Create the Game Over screen object
    game_over_screen = GameOverScreen()

    clock = pygame.time.Clock()

    while True:
        game_over_screen.menu_handler()

        # Draw the Game Over screen
        game_over_screen.draw()

        # Update the display
        pygame.display.flip()

        # Cap the frame rate at 60 FPS
        clock.tick(60)

if __name__ == "__main__":
    main()
