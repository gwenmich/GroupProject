import pygame
from game_class import Game


# event
pygame.init()
pygame.mixer.init()

class PlayGame:
    game = Game()
    game.menu.setup_music()
    game.loop()

# game loop






# render








if __name__ == "__main__":
    play = PlayGame()