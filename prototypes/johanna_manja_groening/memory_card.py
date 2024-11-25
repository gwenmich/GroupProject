class Card(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        super().__init__()

        self.name = filename.split('.')[0]

        self.original_image = pygame.image.load('prototypes/johanna_manja_groening/images' + filename)

        self.back_image = pygame.image.load('prototypes/johanna_manja_groening/images/affirmations')

        self.image = self.back_image
        self.shown = False

    def update(self):
        self.image = self.original_image if self.shown else self.back_image

    def show(self):
        self.shown = True

    def hide(self):
        self.shown = False
