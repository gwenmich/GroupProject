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

    @abstractmethod
    def draw_text(self, surface):
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

    def draw_text(self, surface):
        FONT = pygame.font.Font("PressStart2P-Regular.ttf", 20)
        stress_text = FONT.render("STRESS", True, "black")
        stress_text_rect = stress_text.get_rect(topleft=(770, 20))
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

    def update(self, mini_game_result):
        if mini_game_result == "Win" and self.wins < self.max_wins:
            self.wins += 1


    def draw_text(self, surface):
        FONT = pygame.font.Font("PressStart2P-Regular.ttf", 20)
        games_text = FONT.render("CHALLENGES", True, "black")
        games_text_rect = games_text.get_rect(topleft=(300, 20))
        surface.blit(games_text, games_text_rect)

