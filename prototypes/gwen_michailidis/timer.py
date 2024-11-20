import pygame


class Timer:
    # time limit in seconds
    def __init__(self, time_limit):
        self.time_limit = time_limit

    def countdown(self, surface):
        if self.time_limit > 0:
            seconds = self.time_limit % 60
            minutes = int(self.time_limit / 60) % 60
        else:
            # game over code here
            seconds, minutes = 0, 0

        # display and position timer
        FONT = pygame.font.Font("PressStart2P-Regular.ttf", 20)
        timer_text = FONT.render(f"{minutes:02}:{seconds:02}", True, "black")
        timer_text_rect = timer_text.get_rect(topleft=(20, 20))
        surface.blit(timer_text, timer_text_rect)



