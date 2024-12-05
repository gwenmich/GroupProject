import pygame, random

FPS = 60

#initialize the Card class with the parentclasse pygame sprite
class Card(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        super().__init__()
        #get the filename without .png
        self.name = filename.split('.')[0]
        #load the original image of the card
        self.original_image = pygame.image.load('assets/wellbeing_room/images/' + filename).convert()
        #load the backimage of the card
        self.back_image = pygame.image.load('assets/wellbeing_room/images/affirmations.png').convert()
        #set the image to the backimage of the card
        self.image = self.back_image
        #get the area of the card and set the corners to the x,y, coordinates 
        self.rect =self.image.get_rect(topleft=(x,y))
        #image first not shown but backimage
        self.shown = False


    #update the image of the card as either shown or not shown
    def update(self):
        self.image = self.original_image if self.shown else self.back_image
    #show image
    def show(self):
        self.shown = True
    #hige image
    def hide(self):
        self.shown = False

#initialize gameclass
class WellbeingGame():
    def __init__(self):
        SCREEN_WIDTH = 1000
        SCREEN_HEIGHT = 700
        self.screen= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
        #empty list to eep track of the cards that have been flipped
        self.flipped =[]
        self.frame_count = 0
        #this is used to block the game when two non-matching cards are turned
        self.block_game = False
        self.player_location = "counselling_office"
        pygame.mixer.init()
        # Add music from the sounds folder and loop them indefinitely
        pygame.mixer.music.load("assets/wellbeing_room/sounds/cozy-lofi-beat-split-memmories-248205.mp3")
        pygame.mixer.music.play(-1)

        self.generate_level()
        #sets up the cards

    def update(self, event_list):
        #handles suser input events
        self.user_input(event_list)
        #draws the game elements on screen
        self.draw()
        self.check_level_complete(event_list)

    def check_level_complete(self,event_list):
        if not self.block_game:
        #if the game is not blocked checkk for mouseclick events
            for event in event_list:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1: #if left mouse button is clicked 
                    for card in self.cards_group:
                        #if the click is on the card
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
            if self.frame_count == FPS: #if one second passes (60s)
                self.frame_count =0
                self.block_game = False #unblock the game 

                for card in self.cards_group:
                    if card.name in self.flipped: #chekout the tiles in the flipped array 
                        card.hide() #hide those tiles 
                self.flipped =[]  #clear the flipped array
    #defines how many cards are randomly selected and how many rows cols
    def generate_level(self):
        self.cards = self.select_random_cards()
        self.level_complete = False
        self.rows=4
        self.cols=6
        self.generate_cardset(self.cards)
  #calculates the positions occupied by the cards and creates card objects
    def generate_cardset(self,cards): 
        CARDS_WIDTH =(self.img_width * self.cols + self.padding *3) 
        LEFT_MARGIN = RIGHT_MARGIN = (self.width - CARDS_WIDTH) // 2
        self.cards_group.empty()

        for i in range (len(cards)):
            x= LEFT_MARGIN + ((self.img_width + self.padding) * (i % self.cols))
            y= self.margin_top + (i //self.cols * (self.img_height + self.padding))
            card =Card(cards[i],x,y)
            self.cards_group.add(card)
    
    #selects cards randomly form the images and duplicates them
    def select_random_cards(self):
        cards =random.sample(self.all_cards,12) 
        cards_copy = cards.copy()
        cards.extend(cards_copy)
        random.shuffle(cards)
        return cards
 
    def user_input(self, event_list):
            for event in event_list:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.level_complete:
                        self.generate_level()



    def draw(self):
        background_image = pygame.image.load('assets/wellbeing_room/images/wellbeing_background.png').convert()
        self.screen.blit(background_image,(0,0))
        self.cards_group.draw(self.screen)
        self.cards_group.update()
        #adds image with congratlations to the end of the game
        end_of_game_image = pygame.image.load('assets/wellbeing_room/images/end_of_game.png').convert()
        if self.level_complete:
            self.screen.blit(end_of_game_image,(0,0))


    def game_loop(self):
        pygame.init()

        pygame.display.set_caption("Wellbeing Room")

        clock = pygame.time.Clock()

        running = True
        while running:
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e and self.level_complete:
                        self.__init__()
                        self.player_location = "Map"
                        running = False

            self.update(event_list)
            pygame.display.update()
            clock.tick(FPS)



if __name__ == "__main__":
    well_being = WellbeingGame()
    well_being.game_loop()