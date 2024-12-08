import pygame
import random
import sys

# Initialise Pygame and mixer
pygame.init()
pygame.mixer.init()


# Screen dimensions
width, height = 1000, 700
tile_size = 40
rows, columns = height // tile_size, width // tile_size

# Manages colours and fonts
class Config:
    @staticmethod
    def colours():
        return {
            "text": (255, 255, 255),
            "maze_wall": (0, 0, 0),
            "endpoint": (255, 255, 255),
            "button_yes": (232, 93, 230),
            "button_no": (232, 93, 230),
            "retry": (232, 93, 230)
        }

    @staticmethod
    def fonts():
        return {
            "default": pygame.font.Font("assets/maze/PressStart2P.ttf", 18),
            "title": pygame.font.Font("assets/maze/PressStart2P.ttf", 25)
        }

# Setting the display
screen = pygame.display.set_mode((width, height))

# Loading assets
player = pygame.image.load("assets/maze/girl.png")
player = pygame.transform.scale(player, (tile_size - 8, tile_size - 8))
obstacle = pygame.image.load("assets/maze/stop.png")
obstacle = pygame.transform.scale(obstacle, (tile_size + 10, tile_size + 10))
background = pygame.image.load("assets/maze/background.png")
background = pygame.transform.scale(background, (width, height))


class MazeGame:
    def __init__(self):
        self.level = 1
        self.timer = 50  # Timer
        self.start_time = None # Stores time once game starts
        self.player_position = [1, 1] # Player's initial position
        self.maze = [] # Stores the maze
        self.obstacles = [] # Stores the obstacles in the maze
        self.running = True
        self.endpoint_position = [rows - 2, columns - 2] # Position of the goal
        self.questions = [ # List of tuples that contain questions for the obstacles and the time changes
            ("Your friend wants coffee. Do you join?", -5),
            ("You found a shortcut! Do you take it?", 5),
            ("A friend invites you to the pub. Do you go?", -10),
            ("You feel sleepy. Do you rest?", -15),
            ("You see a shop. Do you get a drink?", 5),
            ("You found a secret path. Do you take it?", -10),
            ("A stranger asks for directions. Do you help?", 10),
            ("You find a detour. Do you go through?", -10),
            ("A friend calls you. Do you pick up?", -5),
            ("You found a map! Do you follow it?", 5),
        ]
        self.victory_status = "Not won"
        self.player_location = "it_dept"

    def draw_background(self):
        screen.blit(background, (0, 0))

    def show_title_screen(self):
        self.draw_background()
        # Title text
        title_text = Config.fonts()["title"].render("The IT Department is such a maze", True, Config.colours()["text"])
        good_luck = Config.fonts()["title"].render("good luck finding your way out...", True, Config.colours()["text"])
        # Instructions text
        instructions_title = Config.fonts()["default"].render("Instructions:", True, Config.colours()["text"])
        instructions_text1 = Config.fonts()["default"].render("1. Navigate the maze with arrow keys.", True, Config.colours()["text"])
        instructions_text2 = Config.fonts()["default"].render("2. Avoid obstacles and answer questions.", True, Config.colours()["text"])
        instructions_text3 = Config.fonts()["default"].render("3. Reach the endpoint before time runs out!", True, Config.colours()["text"])
        # Start text
        start_text = Config.fonts()["default"].render("Press any key to start", True, Config.colours()["text"])
        # Draw all texts to the screen
        screen.blit(title_text, (width // 2 - title_text.get_width() // 2, height // 3))
        screen.blit(good_luck, (width // 2 - good_luck.get_width() // 2, height // 3 + 40))
        screen.blit(instructions_title, (width // 2 - instructions_title.get_width() // 2, height // 2 + 50))
        screen.blit(instructions_text1, (width // 2 - instructions_text1.get_width() // 2, height // 2 + 80))
        screen.blit(instructions_text2, (width // 2 - instructions_text2.get_width() // 2, height // 2 + 110))
        screen.blit(instructions_text3, (width // 2 - instructions_text3.get_width() // 2, height // 2 + 140))
        screen.blit(start_text, (width // 2 - start_text.get_width() // 2, height // 2))
        pygame.display.flip()
        # Wait for player to press a key to start the game
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    waiting = False


    def generate_maze(self):
        self.maze = [[1 for _ in range(columns)] for _ in range(rows)] # Creates a grid where all squares are initially 1 (wall)
        self.obstacles.clear()
        def carve_path(x, y): # Recursive function to generate the maze by setting adjacent tiles to 0 to make the path
            directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
            random.shuffle(directions) # Random shuffle to change the maze every time
            for dx, dy in directions:
                nx, ny = x + dx * 2, y + dy * 2
                if 0 < nx < rows and 0 < ny < columns and self.maze[nx][ny] == 1:
                    self.maze[nx][ny] = 0
                    self.maze[x + dx][y + dy] = 0
                    carve_path(nx, ny)
        self.maze[1][1] = 0
        carve_path(1, 1)
        for _ in range(self.level * 5):
            ox, oy = random.randint(1, rows - 2), random.randint(1, columns - 2)
            if self.maze[ox][oy] == 0 and (ox, oy) != (1, 1) and (ox, oy) != self.endpoint_position: # Specifies the endpoint
                self.obstacles.append((ox, oy)) # Randomly places obstacles for the user to bump into

    def is_walkable(self, row, col): # Checks whether the player can move there (whether the place is a wall or the path)
        if 0 <= row < rows and 0 <= col < columns:
            if self.maze[row][col] == 0 or (row, col) == tuple(self.endpoint_position):
                return True
        return False

    def handle_question(self):
        question, time_change = random.choice(self.questions) # Randomly selects a question when the player hits an obstacle
        self.draw_background()
        question_text = Config.fonts()["default"].render(question, True, Config.colours()["text"])
        screen.blit(question_text, (width // 2 - question_text.get_width() // 2, height // 3))
        yes = pygame.Rect(width // 2 - 100, height // 2 - 25, 200, 50)
        no = pygame.Rect(width // 2 - 100, height // 2 + 35, 200, 50)
        # Displays yes and no buttons for the user to make their choice
        pygame.draw.rect(screen, Config.colours()["button_yes"], yes)
        pygame.draw.rect(screen, Config.colours()["button_no"], no)
        yes_text = Config.fonts()["default"].render("Yes", True, Config.colours()["text"])
        no_text = Config.fonts()["default"].render("No", True, Config.colours()["text"])
        screen.blit(yes_text, (yes.centerx - yes_text.get_width() // 2, yes.centery - yes_text.get_height() // 2))
        screen.blit(no_text, (no.centerx - no_text.get_width() // 2, no.centery - no_text.get_height() // 2))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if yes.collidepoint(event.pos): # If user selects yes - the time change is shown
                        self.timer += time_change
                        result_text = f"Your choice: {time_change} seconds."
                        waiting = False
                    elif no.collidepoint(event.pos):
                        result_text = f"Your choice: no time change" # If player selects no - there is no time change
                        waiting = False
        self.show_result_screen(result_text)

    def show_result_screen(self, result_text): # Displays results
        self.draw_background()
        result_message = Config.fonts()["default"].render(result_text, True, Config.colours()["text"])
        continue_text = Config.fonts()["default"].render("Press any key to continue", True, Config.colours()["text"])
        screen.blit(result_message, (width // 2 - result_message.get_width() // 2, height // 3))
        screen.blit(continue_text, (width // 2 - continue_text.get_width() // 2, height // 2 + 50))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    waiting = False

    def win_screen(self): # Displays a screen saying they won if they made it through all levels
        self.draw_background()
        win_text = Config.fonts()["title"].render("You made it out! You win!", True, Config.colours()["text"])
        screen.blit(win_text, (width // 2 - win_text.get_width() // 2, height // 3))

        self.victory_status = "Won"
        pygame.display.flip()
        pygame.time.wait(3000)

    def loss_screen(self): # Displays loss screen if the user runs out of time and gives a button to let them try again
        self.draw_background()
        lost_text = Config.fonts()["title"].render("Time's up! You lost.", True, Config.colours()["text"])
        screen.blit(lost_text, (width // 2 - lost_text.get_width() // 2, height // 3))
        retry_button = pygame.Rect(width // 2 - 100, height // 2, 200, 50)
        pygame.draw.rect(screen, Config.colours()["retry"], retry_button)
        retry_text = Config.fonts()["default"].render("Try Again", True, Config.colours()["text"])
        screen.blit(retry_text, (retry_button.centerx - retry_text.get_width() // 2, retry_button.centery - retry_text.get_height() // 2))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if retry_button.collidepoint(event.pos):
                        self.level = 1
                        self.timer = 30
                        self.generate_maze()
                        self.start_time = pygame.time.get_ticks()
                        self.player_position = [1, 1]
                        self.running = True
                        waiting = False

    def move_player(self, dx, dy): # Updates player's position in the maze
        new_row = self.player_position[0] + dy
        new_col = self.player_position[1] + dx
        if self.is_walkable(new_row, new_col):
            self.player_position = [new_row, new_col]
            if (new_row, new_col) in self.obstacles:
                self.handle_question()
            if self.player_position == self.endpoint_position:
                if self.level < 3:
                    self.level += 1
                    self.generate_maze()
                    self.start_time = pygame.time.get_ticks()
                    self.player_position = [1, 1]
                else:
                    self.win_screen()

    def load_music(self):
        pygame.mixer.music.load("assets/maze/background_music.mp3")  # Loads the music file
        pygame.mixer.music.play(-1, 0.0)  # Plays the music in a loop (-1) starting immediately

    # Game loop
    def play(self):
        pygame.display.set_caption("Maze Game")
        self.load_music()
        self.show_title_screen()
        self.generate_maze()
        self.start_time = pygame.time.get_ticks()
        while self.running:
            time_used = (pygame.time.get_ticks() - self.start_time) / 1000
            remaining_time = self.timer - time_used
            if remaining_time <= 0:
                self.loss_screen() # Shows the player has lost because they have run out of time
            elif self.victory_status == "Won":
                self.running = False
            self.draw_background()
            for row in range(rows): # If the maze block has a value of 1 it makes it black - this makes the walls
                for col in range(columns):
                    if self.maze[row][col] == 1:
                        pygame.draw.rect(screen, Config.colours()["maze_wall"], pygame.Rect(col * tile_size, row * tile_size, tile_size, tile_size))
            for ox, oy in self.obstacles: # Puts the obstacles on the screen
                screen.blit(obstacle, (oy * tile_size, ox * tile_size))
            pygame.draw.rect(screen, Config.colours()["endpoint"], pygame.Rect(self.endpoint_position[1] * tile_size, self.endpoint_position[0] * tile_size, tile_size, tile_size))#for the endpoint
            screen.blit(player, (self.player_position[1] * tile_size, self.player_position[0] * tile_size)) # Puts the player on the screen
            time_text = Config.fonts()["default"].render(f"Time: {int(remaining_time)}s", True, Config.colours()["text"]) #displays the timer
            screen.blit(time_text, (10, 10)) # Puts timer in left hand corner
            pygame.display.flip() # Updates screen
            for event in pygame.event.get(): # Checks for key presses to move the player
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move_player(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.move_player(1, 0)
                    elif event.key == pygame.K_UP:
                        self.move_player(0, -1)
                    elif event.key == pygame.K_DOWN:
                        self.move_player(0, 1)
                    #     THIS IS A EXTRA COMMAND TO PASS THE MAZE QUICKLY FOR TESTING
                    # elif event.key == pygame.K_w:
                    #     self.player_position = self.endpoint_position
                    elif event.key == pygame.K_e:
                        if self.player_position == self.endpoint_position:
                            self.player_location = "Map"
                            self.running = False



if __name__ == "__main__":
    game = MazeGame()
    game.play()
