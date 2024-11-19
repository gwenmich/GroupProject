import time, pygame



class Timer:

    def __init__(self, time_limit):
        self.time_limit = time_limit



    def countdown(self):
        pass




pygame.init()
screen = pygame.display.set_mode((1000, 700))

# timer = Timer(1800)
clock = pygame.time.Clock()
FONT = pygame.font.Font("PressStart2P-Regular.ttf", 20)

current_seconds = 1800


run = True

while run:

    screen.fill("white")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.USEREVENT:
            current_seconds -= 1

    if current_seconds >= 0:
        display_seconds = current_seconds % 60
        display_minutes = int(current_seconds / 60) % 60

    timer_text = FONT.render(f"{display_minutes:02}:{display_seconds:02}", True, "black")
    timer_text_rect = timer_text.get_rect(topleft=(20, 20))
    screen.blit(timer_text, timer_text_rect)

    pygame.display.flip()

pygame.quit()

