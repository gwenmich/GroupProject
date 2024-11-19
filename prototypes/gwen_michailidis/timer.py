import time, pygame



class Timer:

    def __init__(self, time_limit):
        self.time_limit = time_limit



    def countdown(self):

        elapsed_time = time.time() - start_time
        print(self.time_limit - int(elapsed_time))
        if elapsed_time > self.time_limit:
            print("GAME OVER")



pygame.init()
screen = pygame.display.set_mode((1000, 700))

timer = Timer(1800)
start_time = time.time()
run = True

while run:

    timer.countdown()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()

