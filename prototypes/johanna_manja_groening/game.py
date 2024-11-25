import pygame
import random
from memory_card import Card 


class Game(): 
    def __init__(self):
        self.level = 1 
        self.level_complete = False 


        #memory card images
        self.all_cards = ["add_value.png", "beliefe_self.png", "can_do_this.png","capable.png","enjoy_process.png","grateful.png","I_am_smart.png", "mistake_progress.png", "not_compare.png", "nothing_perfect.png", "okay_rest.png", "proud_myself.png"]
        self.img_width, self.img_height =(447,445)
        self.padding =20
        self.margin_top = 160
        self.cols = 4
        self.rows =2 
        self.width = 1000
        self.cards_group = pygame.sprite.Group()

        self.flipped =[]
        self.frame_count = 0
        self.block_game = False

        #first level
        self.generate_level(self.level)

    def update(self, event_list):
        self.user_input(event_list)
        self.draw()
        self.check_level_complete(event_list)

    def check_level_complete(self,event):
        if not self.block_game:
            for event in event_list:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                    for card in self.cards_group:
                        self.flipped.append(card.name)
                        card.show()
                        if len(self.flipped) ==2:
                            if self.flipped[0] !=self.flipped[1]:
                                self.block_game =True
                            else:
                                self.flipped =[]
                                for card in self.cards_group:
                                    if card.shown:
                                        self.level_complete =True
                                    else:
                                        self.level_complete=False
                                        break
        else:
            self.frame_count += 1
            if self.frame_count ==FPS:
                self.frame_count =0
                self.block_game = False

                for card in self.cards_group:
                    if card.name in self.flipped:
                        card.hide()
                self.flipped =[]
    
    def generate_level(self,level):
        self.cards = self.select_random_cards(self.level)
        self.level_complete = False
        self.rows = self.level +1
        self.cols =4
        self.generate_cardset(self.cards)
 
    def generate_cardset(self,cards):
        self.cols = self.rows = self.cols if self.cols >= self.rows else self.rows 

        CARDS_WIDTH =(self.img_width * self.cols + self.padding *3) 
        LEFT_MARGIN = RIGHT_MARGIN = (self.width - CARDS_WIDTH) // 2
        self.cards_group.empty()

        for i in range (len(cards)):
            x= LEFT_MARGIN + ((self.img_width + self.padding) * (i % self.cols))
            y= self.margin_top + (i //self.rows * (self.img_height + self.padding))
            card =Card(cards[i],x,y)
            self.cards_group.add(card)
    
    def select_random_cards(self, level):
        cards =random.sample(self.all_cards, (self.level + self.level +2))
        cards_copy = cards.copy()
        cards.extend(cards_copy)
        random.shuffle(cards)
        return cards
 
    def user_input(self, event_list):
            for event in event_list:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.level_complete:
                        self.level +=1
                        if self.level >=6:
                            self.level=1
                        self.generate_level(self.level)

    
    def draw(self):
        BLACK =(0,0,0)
        SCREEN_WIDTH = 1000
        SCREEN_HEIGHT = 700
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Wellbeing Room")
        background_image = pygame.image.load('prototypes/johanna_manja_groening/images/wellbeing_background.png').convert() 
        screen.blit(background_image,(0,0))

        #define the font i want to use #font ines suggested
        font_path = "prototypes/johanna_manja_groening/fonts/PressStart2P-Regular.ttf"
        content_font = pygame.font.Font(font_path, 30)
        title_font = pygame.font.Font(font_path, 40)

        #text 
        title_text = title_font.render("Wellbeing Affirmations", True, BLACK)
        
        level_text = content_font.render("Level" + str(self.level),True,BLACK)
        screen.blit(title_text, (50,50))
        screen.blit(level_text, (50,100))

        self.cards_group.draw(screen)
