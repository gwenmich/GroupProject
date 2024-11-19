import pygame
from abc import ABC, abstractmethod


class Bars(ABC):

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


    @abstractmethod
    def draw(self, surface):
        pass

    @abstractmethod
    def update(self, mini_game_result):
        pass








class StressBar(Bars):

    def __init__(self, x, y, w, h, max_stress):
        super().__init__(x, y, w, h)
        self.stress = 75
        self.max_stress = max_stress

    def draw(self, surface):
        ratio = self.stress / self.max_stress
        pygame.draw.rect(surface, (126, 237, 255),(self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, (255, 58, 58), (self.x, self.y, self.w * ratio, self.h))


    def update(self, mini_game_result):
        if mini_game_result == "Lose" and self.stress >= 5:
            self.stress += 5
        elif mini_game_result == "Win" and self.stress <= 95:
            self.stress -= 5




class GamesBar(Bars):

    def __init__(self, x, y, w, h, total_wins):
        super().__init__(x, y, w, h)
        self.wins = 0
        self.max_wins = total_wins

    def draw(self, surface):
        ratio = self.wins / self.max_wins
        pygame.draw.rect(surface, (126, 237, 255),(self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, (255, 255, 0), (self.x, self.y, self.w * ratio, self.h))

    def update(self, mini_game_result):
        if mini_game_result == "Win" and self.wins < self.max_wins:
            self.wins += 1











# code for implementing stress bar in main.py

stress_bar = StressBar(900, 30, 70, 16, 100)



# to put after screen initialisation before while loop
stress_icon = pygame.image.load('stress.png').convert_alpha()


# to put in while loop
stress_bar.draw(screen)
screen.blit(stress_icon, (780, 22))



