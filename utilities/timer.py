import pygame


class Timer:
    # time limit in seconds
    def __init__(self, timer_duration):
        self.timer_duration = timer_duration
        # storing the timer duration a second time to save its start value for the function to calculate the score
        self.initial_duration = timer_duration

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
        timer_text_rect = timer_text.get_rect(topleft=(20, 23))
        surface.blit(timer_text, timer_text_rect)


    def get_time_taken(self):
        # by subtraction the current time left from the start time we get how long player took for higgh scores
        time_taken = self.initial_duration - self.timer_duration
        minutes = time_taken // 60
        seconds = time_taken % 60
        # return in string format for the database
        return f"{minutes:02}:{seconds:02}"




