import time, pygame



class Timer:
    # time limit in seconds
    def __init__(self, time_limit):
        self.time_limit = time_limit

    def countdown(self):
        if self.time_limit > 0:
            seconds = self.time_limit % 60
            minutes = int(self.time_limit / 60) % 60
        else:
            # game over code here
            seconds, minutes = 0, 0

        # display and position timer
        timer_text = FONT.render(f"{minutes:02}:{seconds:02}", True, "black")
        timer_text_rect = timer_text.get_rect(topleft=(20, 20))
        screen.blit(timer_text, timer_text_rect)





# sample boilerplate to see it working
pygame.init()
screen = pygame.display.set_mode((1000, 700))


clock = pygame.time.Clock()

# font for timer
FONT = pygame.font.Font("PressStart2P-Regular.ttf", 20)

# timer for 30 minutes -> 1800 seconds
timer = Timer(1800)
# creating timer where a userevent is posted to event queue every 1 second (1000 milliseconds)
pygame.time.set_timer(pygame.USEREVENT, 1000)


run = True

while run:

    screen.fill("white")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # decreases timer by 1 second
        if event.type == pygame.USEREVENT:
            timer.time_limit -= 1

    # calling timer countdown method
    timer.countdown()


    pygame.display.flip()

pygame.quit()

