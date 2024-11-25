import pygame, random

#from game import Game
#from memory_card import Card 

class Card(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        super().__init__()

        self.name = filename.split('.')[0]

        self.original_image = pygame.image.load('prototypes/johanna_manja_groening/images/' + filename).convert()
        
        
        self.back_image = pygame.image.load('prototypes/johanna_manja_groening/images/affirmations.png').convert()

        self.image = self.back_image
        self.rect =self.image.get_rect(topleft=(x,y))
        self.shown = False

    def update(self):
        self.image = self.original_image if self.shown else self.back_image

    def show(self):
        self.shown = True

    def hide(self):
        self.shown = False


class Game(): 
    def __init__(self):
        self.screen=screen
        self.level = 1 
        self.level_complete = False 


        #memory card images
        self.all_cards = ["add_value.png", "beliefe_self.png", "can_do_this.png","capable.png","enjoy_process.png","grateful.png","I_am_smart.png", "mistake_progress.png", "not_compare.png", "nothing_perfect.png", "okay_rest.png", "proud_myself.png"]
        self.img_width, self.img_height =(100,100)
        self.padding =20
        self.margin_top = 160
        self.rows = 4
        self.cols = 6
        self.width = 1000
        self.cards_group = pygame.sprite.Group()

        self.flipped =[]
        self.frame_count = 0
        self.block_game = False

        #first level
        self.generate_level()

    def update(self, event_list):
        self.user_input(event_list)
        self.draw()
        self.check_level_complete(event_list)

    def check_level_complete(self,event_list):
        if not self.block_game:
            for event in event_list:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1: #if left mouse button is clicked 
                    for card in self.cards_group:
                        if card.rect.collidepoint(event.pos):
                            self.flipped.append(card.name) #if tile is flipped add it to the flip array above 
                            card.show()
                            if len(self.flipped) ==2: #if there are two images in the flipped array 
                                if self.flipped[0] !=self.flipped[1]: #and the names of those are different 
                                    self.block_game =True #blcok the game 
                                else: #if the images are the same 
                                    self.flipped =[] #clear the flipped array
                                    for card in self.cards_group:
                                        if card.shown: #if every card is shown 
                                            self.level_complete =True #level complete will be true
                                        else:
                                            self.level_complete=False #otherwise it will be false 
                                            break
        else: #if the game is blocked 
            self.frame_count += 1 
            if self.frame_count ==FPS: #if one second passes (60s)
                self.frame_count =0
                self.block_game = False #unblock the game 

                for card in self.cards_group:
                    if card.name in self.flipped: #chekout the tiles in the flipped array 
                        card.hide() #hide those tiles 
                self.flipped =[]  #clear the flipped array
    
    def generate_level(self):
        self.cards = self.select_random_cards()
        self.level_complete = False
        self.rows=4
        self.cols=6
        self.generate_cardset(self.cards)
 
    def generate_cardset(self,cards):
        #self.cols = self.rows = self.cols if self.cols >= self.rows else self.rows 

        CARDS_WIDTH =(self.img_width * self.cols + self.padding *3) 
        LEFT_MARGIN = RIGHT_MARGIN = (self.width - CARDS_WIDTH) // 2
        self.cards_group.empty()

        for i in range (len(cards)):
            x= LEFT_MARGIN + ((self.img_width + self.padding) * (i % self.cols))
            y= self.margin_top + (i //self.cols * (self.img_height + self.padding))
            card =Card(cards[i],x,y)
            self.cards_group.add(card)
    
    def select_random_cards(self):
        cards =random.sample(self.all_cards,12) #(self.level + self.level +2))
        cards_copy = cards.copy()
        cards.extend(cards_copy)
        random.shuffle(cards)
        return cards
 
    def user_input(self, event_list):
            for event in event_list:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.level_complete:
                        #self.level +=1
                       # if self.level >=6:
                            #self.level=1
                        self.generate_level()

    
    def draw(self):
        #BLACK =(0,0,0)
        #SCREEN_WIDTH = 1000
        #SCREEN_HEIGHT = 700
        #screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        #pygame.display.set_caption("Wellbeing Room")
        background_image = pygame.image.load('prototypes/johanna_manja_groening/images/wellbeing_background.png').convert() 
        #screen.fill(BLACK) 
        self.screen.blit(background_image,(0,0))

        #define the font i want to use #font ines suggested
        #font_path = "prototypes/johanna_manja_groening/fonts/PressStart2P-Regular.ttf"
        #content_font = pygame.font.Font(font_path, 30)
        #title_font = pygame.font.Font(font_path, 40)

        #text 
       # title_text = title_font.render("Wellbeing Affirmations", True, BLACK)
        
       # level_text = content_font.render("Level" + str(self.level),True,BLACK)
       # screen.blit(title_text, (50,50))
        #screen.blit(level_text, (50,100))

        self.cards_group.draw(screen)
        self.cards_group.update()


pygame.init()
pygame.mixer.init()


#add music from the soundsfolder and loop them indefenitely
pygame.mixer.music.load("prototypes/johanna_manja_groening/sounds/cozy-lofi-beat-split-memmories-248205.mp3")
pygame.mixer.music.play(-1)

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wellbeing Room")
start_image = pygame.image.load('prototypes/johanna_manja_groening/images/wellbeing_room_start.png').convert()

FPS = 60
clock =pygame.time.Clock()

game=Game()

#gameloop 
#finishes the game when closebotton is clicked 
running = True 
while running:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False

    game.update(event_list)
  
    
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()