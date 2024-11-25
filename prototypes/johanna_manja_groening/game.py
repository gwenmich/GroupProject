class Game(): 
    def __init__(self):
        self.level = 1 
        self.level_complete = False 
    
    def update(self, event_list):
        pass

    def draw(self):  #draws all the images on the screen
        background_image = pygame.image.load('prototypes/johanna_manja_groening/images/affirmations.png').convert()
        pygame.display.blit(background_image, (0, 0))

        #define the font i want to use #font ines suggested
        font_path = "prototypes/johanna_manja_groening/fonts/PressStart2P-Regular.ttf"
        content_font = pygame.font.Font(font_path, 30)
        title_font = pygame.font.Font(font_path, 40)

        #text 
        title_text = title_font.render("Wellbeing Affirmations", True, BLACK)
        
        level_text = content_font_render("Level" + str(self.level),True,BLACK)
        screen.blit(title_text, level_text)
