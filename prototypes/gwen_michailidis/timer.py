import time, pygame



class Timer:
    # time limit in seconds
    def __init__(self, time_limit):
        self.time_limit = time_limit

    def countdown(self):
        while self.time_limit > 0:
            seconds = self.time_limit % 60
            minutes = int(self.time_limit / 60) % 60
        else:
            # game over code here
            screen.blit(pygame.image.load('girl64.png'), (50, 50))

        # display and position timer
        timer_text = FONT.render(f"{minutes:02}:{seconds:02}", True, "black")
        timer_text_rect = timer_text.get_rect(topleft=(20, 20))
        screen.blit(timer_text, timer_text_rect)




pygame.init()
screen = pygame.display.set_mode((1000, 700))


clock = pygame.time.Clock()
FONT = pygame.font.Font("PressStart2P-Regular.ttf", 20)

timer = Timer(10)
pygame.time.set_timer(pygame.USEREVENT, 1000)


run = True

while run:

    screen.fill("white")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.USEREVENT:
            timer.time_limit -= 1

    timer.countdown()


    pygame.display.flip()

pygame.quit()

