from character_class import Character
import pygame

class Game:
    def __init__(self, manager):
        self.manager = manager
        self.screen = Screen()
        self.player = Character(screen, "girl_sprite.png", 2, "#ff00d6", 64, 64)

    def loop(self):
        dt = self.manager.clock.tick(FPS) / 1000


        self.manager.screen.fill((0, 200, 110))
        # need function to draw map

        self.player.animate(screen)
        self.player.move(250, dt)

        pygame.display.flip()

    def handle_input(self, event):
        pass
