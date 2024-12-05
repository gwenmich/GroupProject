import pygame
import sys

class VictoryScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.text = self.font.render("You Won All Games!", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(500, 350))

    def display(self):
        self.screen.fill((245, 66, 197))
        self.screen.blit(self.text, self.text_rect)
        pygame.display.flip()
        self.handle_input()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                print("Exiting Victory Screen.")
                pygame.quit()
                sys.exit()
