class Game(): 
    def __init__(self):
        self.level = 1 
        self.level_complete = False 


        #memory card images
        self.all_cards = ["add_value", "beliefe_self", "can_do_this","capable","enjoy_process","grateful","I_am_smart", "mistake_progress", "not_compare", "nothing_perfect", "okay_rest", "proud_myself"]
        self.img_width, self.img_height =(447,445)
        self.padding =20
        self.margin_top = 160
        self.cols = 4
        self.rows =2 
        self.witdth = 1000
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
                if event.type == pygame.MOUSEBUTTINBDOWN and event.button ==1:
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
    
    def generate_level(self,level)
        self.cards = self.select_random_cards(self.level)
        self.level_complete = False
        self.rows = self.level +1
        self.cols =4
        self.generate_cardset(self.cards)
 
    def generate_cardset(self,cards):
        self.cols = self.rows = self.cols if self.cols >= self.rows else self.rows 

        CARDS_WIDTH =((self.img_width + self.padding) * (i % self.cols))
        LEFT_MARGIN = RIGHT_MARGIN = (self.width - CARDS_QIDTH) // 2
        self.cards_group.empty()

        for i in range (len(cards)):
            x= LEFT_MARGIN + ((self.img_width + self.padding) * (i % self.cols))
            y= self.margin_top + (i //self.rows * (self.img_height + self.padding))
            card =Card(cards[i],x,y)
            self.cards_group.add(card)

    
    def draw(self):
        background_image = pygame.image.load('prototypes/johanna_manja_groening/images/wellbeing_background.png').convert() 
        screen.blit(background_image,(0,0))

        #define the font i want to use #font ines suggested
        font_path = "prototypes/johanna_manja_groening/fonts/PressStart2P-Regular.ttf"
        content_font = pygame.font.Font(font_path, 30)
        title_font = pygame.font.Font(font_path, 40)

        #text 
        title_text = title_font.render("Wellbeing Affirmations", True, BLACK)
        
        level_text = content_font_render("Level" + str(self.level),True,BLACK)
        screen.blit(title_text, level_text)
        