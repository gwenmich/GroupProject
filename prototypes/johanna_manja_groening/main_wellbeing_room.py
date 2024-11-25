import pygame, random







pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wellbeing Room")
background_image = pygame.image.load('prototypes/johanna_manja_groening/images/wellbeing_background.png').convert()
start_image = pygame.image.load('prototypes/johanna_manja_groening/images/wellbeing_room_start.png').convert()

FPS = 60
clock =pygame.time.Clock()

#gameloop 
#finishes the game when closebotton is clicked 
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  
    screen.blit(background_image,(0,0))
    pygame.display.update()

pygame.quit()