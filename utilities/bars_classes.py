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
    def update(self):
        pass

    @abstractmethod
    def draw_text(self, surface):
        pass






class StressBar(Bars):

    def __init__(self, x, y, w, h, max_stress):
        super().__init__(x, y, w, h)
        self.stress = 7
        self.max_stress = max_stress

    def draw(self, surface):
        ratio = self.stress / self.max_stress
        pygame.draw.rect(surface, (126, 237, 255),(self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, (255, 58, 58), (self.x, self.y, self.w * ratio, self.h))


    def update(self):
        if self.stress <= self.max_stress:
            self.stress += 1

    # def update_win(self):
    #     if self.stress >= 1:
    #         self.stress -= 1

    def update_wellbeing(self):
        self.stress -= 3

    def draw_text(self, surface):
        FONT = pygame.font.Font("assets/high_scores/PressStart2P-Regular.ttf", 20)
        stress_text = FONT.render("STRESS", True, "black")
        stress_text_rect = stress_text.get_rect(topleft=(770, 23))
        surface.blit(stress_text, stress_text_rect)



class GamesBar(Bars):

    def __init__(self, x, y, w, h, total_wins):
        super().__init__(x, y, w, h)
        self.wins = 0
        self.max_wins = total_wins

    def draw(self, surface):
        ratio = self.wins / self.max_wins
        pygame.draw.rect(surface, (126, 237, 255),(self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, (255, 255, 0), (self.x, self.y, self.w * ratio, self.h))

    def update(self):
        if self.wins < self.max_wins:
            self.wins += 1


    def draw_text(self, surface):
        FONT = pygame.font.Font("assets/high_scores/PressStart2P-Regular.ttf", 20)
        games_text = FONT.render("CHALLENGES", True, "black")
        games_text_rect = games_text.get_rect(topleft=(300, 23))
        surface.blit(games_text, games_text_rect)

