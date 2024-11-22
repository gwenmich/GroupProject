import pygame
import sys
from abc import ABC, abstractmethod
from prototypes.ines_duarte.map.map_config import *
from prototypes.gwen_michailidis.bars_classes import *
from prototypes.gwen_michailidis.timer import *


class Screen(ABC):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.title = "Thesis Quest"
        pygame.display.set_caption(self.title)
        self.tile_size = TILE_SIZE
        self.game_icon = pygame.image.load(r'C:\Users\inesd\PycharmProjects\CFGDegree-GroupProjectTeam1\prototypes\ines_duarte\map\map_assets\school_2.png')
        pygame.display.set_icon(self.game_icon)


    @abstractmethod
    def load_image(self, path, size=None):
        pass

    @abstractmethod
    def draw(self, game_state):
        pass



class MapScreen(Screen):
    def __init__(self):
        super().__init__()
        self.screen_fill = self.screen.fill((0, 200, 110))
        self.stress_bar = StressBar(900, 20, 70, 16, 100)
        self.games_bar = GamesBar(510, 20, 70, 16, 4)
        self.timer = Timer(1800)
        pygame.time.set_timer(pygame.USEREVENT, 1000)


        self.tile_images = {
            'W': self.load_image(r'C:\Users\inesd\PycharmProjects\CFGDegree-GroupProjectTeam1\prototypes\ines_duarte\map\map_assets\wall_1.png', (WALL_SIZE, WALL_SIZE)),
            'A': self.load_image(r'C:\Users\inesd\PycharmProjects\CFGDegree-GroupProjectTeam1\prototypes\ines_duarte\map\map_assets\police-station.png', (BUILDING_SIZE, BUILDING_SIZE)),
            'B': self.load_image(r'C:\Users\inesd\PycharmProjects\CFGDegree-GroupProjectTeam1\prototypes\ines_duarte\map\map_assets\school.png', (BUILDING_SIZE, BUILDING_SIZE)),
            'C': self.load_image(r'C:\Users\inesd\PycharmProjects\CFGDegree-GroupProjectTeam1\prototypes\ines_duarte\map\map_assets\royal-palace.png', (BUILDING_SIZE, BUILDING_SIZE)),
            'D': self.load_image(r'C:\Users\inesd\PycharmProjects\CFGDegree-GroupProjectTeam1\prototypes\ines_duarte\map\map_assets\apartment.png', (BUILDING_SIZE, BUILDING_SIZE)),
            'E': self.load_image(r'C:\Users\inesd\PycharmProjects\CFGDegree-GroupProjectTeam1\prototypes\ines_duarte\map\map_assets\museum.png', (BUILDING_SIZE, BUILDING_SIZE)),
            'G': self.load_image(r'C:\Users\inesd\PycharmProjects\CFGDegree-GroupProjectTeam1\prototypes\ines_duarte\map\map_assets\grass.png', (GRASS_SIZE, GRASS_SIZE)),
            'T': self.load_image(r'C:\Users\inesd\PycharmProjects\CFGDegree-GroupProjectTeam1\prototypes\ines_duarte\map\map_assets\tree.png', (TREE_SIZE, TREE_SIZE)),
            'S': self.load_image(r'C:\Users\inesd\PycharmProjects\CFGDegree-GroupProjectTeam1\prototypes\ines_duarte\map\map_assets\sakura.png', (TREE_SIZE, TREE_SIZE)),
            'F': self.load_image(r'C:\Users\inesd\PycharmProjects\CFGDegree-GroupProjectTeam1\prototypes\ines_duarte\map\map_assets\bench.png', (BENCH_SIZE, BENCH_SIZE)),
        }


    def load_image(self, path, size=None):
        image = pygame.image.load(path)
        if size:  # Scale to a custom size
            return pygame.transform.scale(image, size)
        return image

    def draw(self):
        self.screen_fill = self.screen.fill((0, 200, 110))

        for y, row in enumerate(TILE_MAP):
            for x, tile in enumerate(row):
                if tile in self.tile_images:
                    self.screen.blit(self.tile_images[tile], (x * TILE_SIZE, y * TILE_SIZE))

        self.stress_bar.draw(self.screen)
        self.stress_bar.draw_text(self.screen)

        self.games_bar.draw(self.screen)
        self.games_bar.draw_text(self.screen)

        self.timer.countdown(self.screen)





# class MenuScreen(Screen):
#
#
#
#
# class Game:
#     def __init__(self):
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.runnin = True
#
#     def new_game(self):
#         self.playing = True
#
#     def update(self):
#
#
#     def win_lose(self):

    return game_state


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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            # decreases timer by 1 second every second
            if event.type == pygame.USEREVENT:
                map_screen.timer.time_limit -= 1

        map_screen.draw()

        # Update the display
        pygame.display.flip()

        # framerate in seconds - the time difference between two frames
        pygame.time.Clock().tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
