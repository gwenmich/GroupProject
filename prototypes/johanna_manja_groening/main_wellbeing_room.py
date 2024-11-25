import pygame, random


class Card(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        super().__init__()

        self.name = filename.split('.')[0]

        self.original_image = pygame.image.load('images/' + filename)

        self.back_image = pygame.image.load('images/affirmations')

        self.image = self.back_image
        self.shown = False

    def update(self):
        self.image = self.original_image if self.shown else self.back_image

    def show(self):
        self.shown = True

    def hide(self):
        self.shown = False


class Game(): 
    def __init__(self):
        self.level = 1 
        self.level_complete = False 
    
    def update(self, event_list):
        pass

    def draw(self):  #draws all the images on the screen 
        background_image = pygame.image.load('images/wellbeing_background.png')
        screen.blit(background_image, (0, 0))

        #define the font i want to use #font ines suggested
        font_path = "fonts/PressStart2P-Regular.ttf"
        content_font = pygame.font.Font(font_path, 30)
        title_font = pygame.font.Font(font_path, 40)

        #text 
        title_text = title_font.render("Wellbeing Affirmations", True, BLACK)




pygame.init()


BLACK =(0,0,0)


# Music
pygame.mixer.music.load('sounds/cozy-lofi-beat-split-memmories-248205.mp3')
pygame.mixer.music.play(-1)

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wellbeing Room")

#wellbeing _room background image start
wellbeing_room_start_background = pygame.image.load('images/wellbeing_room_start.png').convert()
# memory game background image 
wellbeing_room_background = pygame.image.load('images/wellbeing_background.png').convert()

# Menu font
font_path = "fonts/PressStart2P-Regular.ttf"
font = pygame.font.Font(font_path, 30)
title_font = pygame.font.Font(font_path, 40)

FPS =60
clock =pygame.time.Clock()

game= Game()

#gameloop 
#finishes the game when closebotton is clicked 
running = TRUE 
while running: 
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False


    game.update(event_list)

    pygame.display.update()
    clock.tick(FPS)


pygame.quit()