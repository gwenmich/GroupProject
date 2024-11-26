import pygame
# do we need sys?????
import sys
from abc import ABC, abstractmethod
from world.map_config import *
from prototypes.gwen_michailidis.bars_classes import *
from prototypes.gwen_michailidis.timer import *



# Create a Class for all Game Screens
class Screen(ABC):
    # initialize
    def __init__(self):
        pygame.init()
        # set screen size calling varibales from Config File
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.title = "Thesis Quest"
        # set titles in game window
        pygame.display.set_caption(self.title)
        # set default tile size
        self.tile_size = TILE_SIZE
        # load image for game window
        self.game_icon = pygame.image.load('assets/main_map/school_2.png')
        pygame.display.set_icon(self.game_icon)


    # abstract methods to be overwritten by child classes
    @abstractmethod
    def load_image(self, path, size=None):
        pass

    # abstract methods to be overwritten by child classes
    @abstractmethod
    def draw(self):
        pass



class MapScreen(Screen):
    def __init__(self):
        # initialize parent lcass
        super().__init__()
        # set map color
        self.screen_fill = self.screen.fill((0, 200, 110))
        # instantiating Bar Class and giving coordinates
        self.stress_bar = StressBar(900, 20, 70, 16, 100)
        self.games_bar = GamesBar(510, 20, 70, 16, 4)
        # instantiating Timer and passing timer duration
        self.timer = Timer(1800)
        # creating a pygame for to set how often timer updates, every second
        pygame.time.set_timer(pygame.USEREVENT, 1000)


        # creating a dictionary to contain and load the images for the map, using the function bellow to resize
        # the keys are the letter that match the tile map
        self.tile_images = {
            'W': self.load_image('assets/main_map/wall_1.png', (WALL_SIZE, WALL_SIZE)),
            'A': self.load_image('assets/main_map/police-station.png', (BUILDING_SIZE, BUILDING_SIZE)),
            'B': self.load_image('assets/main_map/school.png', (BUILDING_SIZE, BUILDING_SIZE)),
            'C': self.load_image('assets/main_map/royal-palace.png', (BUILDING_SIZE, BUILDING_SIZE)),
            'D': self.load_image('assets/main_map/apartment.png', (BUILDING_SIZE, BUILDING_SIZE)),
            'E': self.load_image('assets/main_map/museum.png', (BUILDING_SIZE, BUILDING_SIZE)),
            'G': self.load_image('assets/main_map/grass.png', (GRASS_SIZE, GRASS_SIZE)),
            'T': self.load_image('assets/main_map/tree.png', (TREE_SIZE, TREE_SIZE)),
            'S': self.load_image('assets/main_map/sakura.png', (TREE_SIZE, TREE_SIZE)),
            'F': self.load_image('assets/main_map/bench.png', (BENCH_SIZE, BENCH_SIZE)),
        }

    # function to load and resize images, size is NONE by default unless it needs resizing
    # takes path and size as arguments
    def load_image(self, path, size=None):
        image = pygame.image.load(path)
        # if size is given, rescale image
        if size:
            return pygame.transform.scale(image, size)
        else:
            # is not just assumes NONE and returns image
            return image

    # function to draw the screen
    def draw(self):
        # background color
        self.screen_fill = self.screen.fill((0, 200, 110))

        # using enumerate and passing the tile map to iterate through every row and column checking index and value
        for y, row in enumerate(TILE_MAP):
            for x, tile in enumerate(row):
                # if it find the letter in the tile image dictionary it blits the image with the matching Key Value
                if tile in self.tile_images:
                    self.screen.blit(self.tile_images[tile], (x * TILE_SIZE, y * TILE_SIZE))

        # drawing the bars and timers and the matching texts
        # self.stress_bar.draw(self.screen)
        # self.stress_bar.draw_text(self.screen)
        #
        # self.games_bar.draw(self.screen)
        # self.games_bar.draw_text(self.screen)
        #
        # self.timer.countdown(self.screen)




if __name__ == "__main__":

    # UNCOMMENT TO TEXT
    # Main function
    def main():
        # Create the MapScreen
        map_screen = MapScreen()

        # Game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                # decreases timer by 1 second every second
                # elif event.type == pygame.USEREVENT:
                #     map_screen.timer.timer_duration -= 1

            map_screen.draw()

            # Update the display
            pygame.display.flip()

            # framerate in seconds - the time difference between two frames
            pygame.time.Clock().tick(FPS)

        pygame.quit()
        sys.exit()

    main()



