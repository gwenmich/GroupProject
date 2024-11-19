# hitbox coordinates for character building collision file
library = pygame.Rect(230, 540, 35, 40)
cafeteria = pygame.Rect(850, 525, 40, 40)
counselling_office = pygame.Rect(510, 327, 35, 40)
classroom = pygame.Rect(852, 527, 35, 40)
it_dept = pygame.Rect(230, 150, 35, 40)

# blocking building logic for character collision file
games_won = {
    "library": "Not won",
    "cafeteria": "Not won",
    "counselling_office": "Not won",
    "classroom": "Not won",
    "it_dept": "Not won"
}
for building, building_rect in buildings.items():
    if character_rect.colliderect(building_rect):
        if building == "counselling_office" or games_won[building] == "Not won":
            mini_game(building)
        else:
            print("Sorry, you've already won this game, time to visit another building!")




# GameBar Class
class GamesBar():
    def __init__(self, x, y, w, h, total_wins):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.wins = 0
        self.max_wins = total_wins

    def draw(self, surface):
        ratio = self.wins / self.max_wins
        pygame.draw.rect(surface, (126, 237, 255),(self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, (255, 255, 0), (self.x, self.y, self.w * ratio, self.h))

    def update(self, mini_game_result):
        if mini_game_result == "Win" and self.wins < self.max_wins:
            self.wins += 1



games_bar = GamesBar(500, 30, 70, 16, 4)


# to put after screen initialisation before while loop
games_icon = pygame.image.load('stress.png').convert_alpha()

# to put in while loop
games_bar.draw(screen)
screen.blit(games, (780, 22))