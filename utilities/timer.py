import pygame


class Timer:
    # time limit in seconds
    def __init__(self, timer_duration):
        self.timer_duration = timer_duration

    def countdown(self, surface):
        if self.timer_duration > 0:
            seconds = self.timer_duration % 60
            minutes = int(self.timer_duration / 60) % 60
        else:
            # game over code here
            seconds, minutes = 0, 0

        # display and position timer
        FONT = pygame.font.Font("world/PressStart2P-Regular.ttf", 20)
        timer_text = FONT.render(f"{minutes:02}:{seconds:02}", True, "black")
        timer_text_rect = timer_text.get_rect(topleft=(20, 20))
        surface.blit(timer_text, timer_text_rect)



