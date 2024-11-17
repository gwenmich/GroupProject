import pygame

class StressBar():
    def __init__(self, x, y, w, h, max_stress):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.stress = 75
        self.max_stress = max_stress

    def draw(self, surface):
        ratio = self.stress / self.max_stress
        pygame.draw.rect(surface, (126, 237, 255),(self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, (255, 58, 58), (self.x, self.y, self.w * ratio, self.h))



stress_bar = StressBar(900, 30, 70, 16, 100)



# to put after screen initialisation before while loop
stress_icon = pygame.image.load('stress.png').convert_alpha()


# to put in while loop
stress_bar.draw(screen)
screen.blit(stress_icon, (780, 22))

