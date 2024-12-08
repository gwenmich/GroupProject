import pygame
from game_class import Game




class PlayGame:
    pygame.init()
    pygame.mixer.init()
    game = Game()
    game.menu.setup_music()
    game.loop()





if __name__ == "__main__":
    play = PlayGame()