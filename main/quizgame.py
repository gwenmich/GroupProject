import pygame
import sys
import os
import textwrap

# Initialize Pygame
pygame.init()

# File Paths
FONT_PATH = "assets/fight_quiz/PressStart2P-Regular.ttf"
BACKGROUND_PATH = "assets/fight_quiz/Library.png"


# Ensure font file and background image exist
if not os.path.exists(FONT_PATH):
    raise FileNotFoundError(f"Font file not found at {FONT_PATH}")
if not os.path.exists(BACKGROUND_PATH):
    raise FileNotFoundError(f"Background image not found at {BACKGROUND_PATH}")

# Game Settings
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quiz Game")

# Colours
WHITE = (255, 255, 255)

# Font files, pixellated
try:
    FONT = pygame.font.Font(FONT_PATH, 14)
    LARGE_FONT = pygame.font.Font(FONT_PATH, 24)
    SMALL_FONT = pygame.font.Font(FONT_PATH, 16)
except Exception as e:
    print(f"Error loading font: {e}")
    sys.exit()

# Game states
MAIN_MENU = "MAIN_MENU"
QUIZ_GAME = "QUIZ_GAME"
Librarian_INTRO = "LIBRARIAN_INTRO"
END_SCREEN = "END_SCREEN"
# CURRENT_STATE = MAIN_MENU

# Question class for the quiz
class Question:
    def __init__(self, question_text, choices, answer_index):
        self.question_text = question_text
        self.choices = choices
        self.answer_index = answer_index

    def draw(self, screen, selected_choice=None):
        y_offset = 150
        question_lines = textwrap.wrap(self.question_text, width=50)  # Wrap the question text
        for line in question_lines:
            question_surface = FONT.render(line, True, WHITE)
            screen.blit(question_surface, (50, y_offset))
            y_offset += 20

        # Draw choices
        for i, choice in enumerate(self.choices):
            choice_surface = FONT.render(choice, True, WHITE)
            screen.blit(choice_surface, (100, y_offset))
            if selected_choice == i:
                pygame.draw.circle(screen, (0, 255, 0), (90, y_offset), 5)  # Appears right next to the letter
            y_offset += 30

# Quiz Game
class QuizGame:
    def __init__(self):
        self.player_location = "library"
        self.victory_status = "Not won"
        self.questions = [
            Question("Which keyword is used to define a function in Python?",
                     ["A. func", "B. def", "C. define", "D. method"], 1),
            Question("How do you select all columns from a table in SQL?",
                     ["A. SELECT *", "B. SELECT ALL", "C. GET *", "D. FETCH ALL"], 0),
            Question("Which data structure is LIFO?", ["A. List", "B. Queue", "C. Stack", "D. Set"], 2),
            Question("What command creates a new table in SQL?",
                     ["A. MAKE TABLE", "B. CREATE TABLE", "C. NEW TABLE", "D. ADD TABLE"], 1),
            Question("What symbol is used to comment in Python?", ["A. //", "B. <!-- -->", "C. #", "D. %"], 2)
        ]
        self.current_question = 0
        self.selected_choice = None
        self.score = 0
        self.current_state = MAIN_MENU

    def check_answer(self):
        if self.selected_choice == self.questions[self.current_question].answer_index:
            self.score += 1

    def next_question(self):
        self.current_question += 1
        self.selected_choice = None

    def draw(self, screen):
        # Draw the background image
        try:
            background = pygame.image.load(BACKGROUND_PATH)
            background = pygame.transform.scale(background, (WIDTH, HEIGHT))
            screen.blit(background, (0, 0))
        except pygame.error as e:
            print(f"Error loading background image: {e}")

        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            question.draw(screen, self.selected_choice)
        else:
            # Set game state to END_SCREEN when questions are finished
            self.current_state = END_SCREEN
            self.draw_end_screen(screen)

    def draw_end_screen(self, screen):
        if self.score >= 3:
            end_message = "Well done, you passed!"
            self.victory_status = "Won"
        else:
            end_message = "Good try, but try again!"

        result_message = f"Your score: {self.score}/{len(self.questions)}"
        end_surface = LARGE_FONT.render(end_message, True, WHITE)
        result_surface = FONT.render(result_message, True, WHITE)

        # Makes sure text is centered on the screen
        screen.blit(end_surface,
                    (WIDTH // 2 - end_surface.get_width() // 2, HEIGHT // 2 - end_surface.get_height()))
        screen.blit(result_surface, (WIDTH // 2 - result_surface.get_width() // 2, HEIGHT // 2 + 50))

        if self.score <= 3:
        # Add restart and exit options
            restart_surface = FONT.render("Press R to Restart", True, WHITE)
            screen.blit(restart_surface, (WIDTH // 2 - restart_surface.get_width() // 2, HEIGHT // 2 + 100))

        exit_surface = FONT.render("Press E to Exit", True, WHITE)
        screen.blit(exit_surface, (WIDTH // 2 - exit_surface.get_width() // 2, HEIGHT // 2 + 150))

    # Main Menu
    def draw_main_menu(self):
        try:
            background = pygame.image.load(BACKGROUND_PATH)
            background = pygame.transform.scale(background, (WIDTH, HEIGHT))
            screen.blit(background, (0, 0))
        except pygame.error as e:
            print(f"Error loading background image: {e}")

        title_surface = LARGE_FONT.render("Welcome to the Quiz Game!", True, WHITE)
        play_surface = FONT.render("Press Enter to Play", True, WHITE)
        exit_surface = FONT.render("Press ESC to Quit", True, WHITE)

        screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, HEIGHT // 2 - 100))
        screen.blit(play_surface, (WIDTH // 2 - play_surface.get_width() // 2, HEIGHT // 2))
        screen.blit(exit_surface, (WIDTH // 2 - exit_surface.get_width() // 2, HEIGHT // 2 + 50))

        pygame.display.update()

    # Librarian Introduction
    def draw_librarian_intro(self):
        try:
            background = pygame.image.load(BACKGROUND_PATH)
            background = pygame.transform.scale(background, (WIDTH, HEIGHT))
            screen.blit(background, (0, 0))
        except pygame.error as e:
            print(f"Error loading background image: {e}")

        # Split text if it's too long
        intro_text = "Hey you! You need to complete this quiz before you can hand in any thesis work!"
        lines = textwrap.wrap(intro_text, width=50)

        y_offset = HEIGHT // 2 - len(lines) * 20
        for line in lines:
            line_surface = SMALL_FONT.render(line, True, WHITE)
            screen.blit(line_surface, (WIDTH // 2 - line_surface.get_width() // 2, y_offset))
            y_offset += 20

        instruction_surface = SMALL_FONT.render("Press Enter to start the quiz!", True, WHITE)
        screen.blit(instruction_surface, (WIDTH // 2 - instruction_surface.get_width() // 2, y_offset + 40))

        pygame.display.update()

    # Game Loop
    def play(self):
        # global CURRENT_STATE
        # quiz = QuizGame()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if self.current_state == MAIN_MENU:
                        if event.key == pygame.K_RETURN:
                            self.current_state = Librarian_INTRO
                        elif event.key == pygame.K_ESCAPE:
                            self.player_location = "Map"
                            running = False

                    elif self.current_state == Librarian_INTRO:
                        if event.key == pygame.K_RETURN:
                            self.current_state = QUIZ_GAME

                    elif self.current_state == QUIZ_GAME:
                        if event.key in [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d]:
                            self.selected_choice = ["a", "b", "c", "d"].index(pygame.key.name(event.key))
                        elif event.key == pygame.K_RETURN and self.selected_choice is not None:
                            self.check_answer()
                            self.next_question()

                    elif self.current_state == END_SCREEN:
                        if event.key == pygame.K_r:
                            self.__init__()
                            self.current_state = QUIZ_GAME
                        elif event.key == pygame.K_e and self.victory_status == "Not won":
                            self.__init__()
                            self.player_location = "Map"
                            running = False
                        elif event.key == pygame.K_e:
                            self.player_location = "Map"
                            running = False

            # Draw current state
            if self.current_state == MAIN_MENU:
                self.draw_main_menu()
            elif self.current_state == Librarian_INTRO:
                self.draw_librarian_intro()
            elif self.current_state == QUIZ_GAME:
                self.draw(screen)
            elif self.current_state == END_SCREEN:
                self.draw_end_screen(screen)

            pygame.display.flip()

if __name__ == "__main__":
    library_game = QuizGame()
    library_game.play()