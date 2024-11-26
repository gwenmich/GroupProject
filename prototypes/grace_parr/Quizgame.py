import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# File Paths
FONT_PATH = r"C:\Users\Lenap\PycharmProjects\CFGDegree-GroupProjectTeam1\prototypes\grace_parr\PressStart2P-Regular.ttf"
BACKGROUND_PATH = r"C:\Users\Lenap\PycharmProjects\CFGDegree-GroupProjectTeam1\prototypes\grace_parr\Library.png"  # Updated background path

# Ensure font file and background image exist
if not os.path.exists(FONT_PATH):
    raise FileNotFoundError(f"Font file not found at {FONT_PATH}")
if not os.path.exists(BACKGROUND_PATH):
    raise FileNotFoundError(f"Background image not found at {BACKGROUND_PATH}")

# Game Settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quiz Game")

# Colors
WHITE = (255, 255, 255)
PURPLE = (138, 43, 226)

# Fonts
try:
    FONT = pygame.font.Font(FONT_PATH, 18)  # Reduced font size to fit text
    LARGE_FONT = pygame.font.Font(FONT_PATH, 24)  # Slightly larger for titles
    SMALL_FONT = pygame.font.Font(FONT_PATH, 16)  # Smaller for intro messages
except Exception as e:
    print(f"Error loading font: {e}")
    sys.exit()

# Game states
MAIN_MENU = "MAIN_MENU"
QUIZ_GAME = "QUIZ_GAME"
Librarian_INTRO = "LIBRARIAN_INTRO"
END_SCREEN = "END_SCREEN"
CURRENT_STATE = MAIN_MENU


# Function to break text into multiple lines if it's too long (I had a lot of problems with this!)
def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        # Check the width of the current line with the new word
        test_line = current_line + ' ' + word if current_line else word
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)  # Add the last line
    return lines


# Question class for the quiz
class Question:
    def __init__(self, question_text, choices, answer_index):
        self.question_text = question_text
        self.choices = choices
        self.answer_index = answer_index

    def draw(self, screen):
        y_offset = 150
        question_surface = LARGE_FONT.render(self.question_text, True, WHITE)
        screen.blit(question_surface, (50, 50))

        # Draw choices
        for i, choice in enumerate(self.choices):
            choice_surface = FONT.render(choice, True, WHITE)
            screen.blit(choice_surface, (100, y_offset))
            y_offset += 50


# Quiz Game
class QuizGame:
    def __init__(self):
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
            background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Scale the image to fit the screen
            screen.blit(background, (0, 0))
        except pygame.error as e:
            print(f"Error loading background image: {e}")

        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            question.draw(screen)

            if self.selected_choice is not None:
                y_offset = 150 + 50 * self.selected_choice
                pygame.draw.circle(screen, PURPLE, (75, y_offset + 15), 10)
        else:
            # Set game state to END_SCREEN when questions are finished
            global CURRENT_STATE
            CURRENT_STATE = END_SCREEN
            self.draw_end_screen(screen)

    def draw_end_screen(self, screen):
        if self.score >= 3:
            end_message = "Well done, you passed!"
        else:
            end_message = "Good try, but try again!"

        result_message = f"Your score: {self.score}/{len(self.questions)}"
        end_surface = LARGE_FONT.render(end_message, True, WHITE)
        result_surface = FONT.render(result_message, True, WHITE)

        # Ensure text is centered on the screen
        screen.blit(end_surface,
                    (WIDTH // 2 - end_surface.get_width() // 2, HEIGHT // 2 - end_surface.get_height()))
        screen.blit(result_surface, (WIDTH // 2 - result_surface.get_width() // 2, HEIGHT // 2 + 50))

        # Add restart and exit options
        restart_surface = FONT.render("Press R to Restart", True, WHITE)
        exit_surface = FONT.render("Press E to Exit", True, WHITE)
        screen.blit(restart_surface, (WIDTH // 2 - restart_surface.get_width() // 2, HEIGHT // 2 + 100))
        screen.blit(exit_surface, (WIDTH // 2 - exit_surface.get_width() // 2, HEIGHT // 2 + 150))


# Main Menu
def draw_main_menu():
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
def draw_librarian_intro():
    try:
        background = pygame.image.load(BACKGROUND_PATH)
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
        screen.blit(background, (0, 0))
    except pygame.error as e:
        print(f"Error loading background image: {e}")

    # Split text if it's too long
    intro_text = "Hey you! You need to complete this quiz before you can hand in any thesis work!"
    lines = wrap_text(intro_text, SMALL_FONT, WIDTH - 40)  # 40 pixels padding on each side

    y_offset = HEIGHT // 2 - len(lines) * 20  # Adjust y_offset for multiple lines
    for line in lines:
        line_surface = SMALL_FONT.render(line, True, WHITE)
        screen.blit(line_surface, (WIDTH // 2 - line_surface.get_width() // 2, y_offset))
        y_offset += 20  # Move to the next line

    instruction_surface = SMALL_FONT.render("Press Enter to start the quiz!", True, WHITE)
    screen.blit(instruction_surface, (WIDTH // 2 - instruction_surface.get_width() // 2, y_offset + 40))

    pygame.display.update()


# Main Game Loop
def main():
    global CURRENT_STATE
    quiz = QuizGame()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if CURRENT_STATE == MAIN_MENU:
                    if event.key == pygame.K_RETURN:
                        CURRENT_STATE = Librarian_INTRO
                    elif event.key == pygame.K_ESCAPE:
                        running = False

                elif CURRENT_STATE == Librarian_INTRO:
                    if event.key == pygame.K_RETURN:
                        CURRENT_STATE = QUIZ_GAME

                elif CURRENT_STATE == QUIZ_GAME:
                    if event.key in [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d]:
                        quiz.selected_choice = ["a", "b", "c", "d"].index(pygame.key.name(event.key))
                    elif event.key == pygame.K_RETURN and quiz.selected_choice is not None:
                        quiz.check_answer()
                        quiz.next_question()

                elif CURRENT_STATE == END_SCREEN:
                    if event.key == pygame.K_r:
                        quiz = QuizGame()
                        CURRENT_STATE = QUIZ_GAME
                    elif event.key == pygame.K_e:
                        running = False

        # Draw current state
        if CURRENT_STATE == MAIN_MENU:
            draw_main_menu()
        elif CURRENT_STATE == Librarian_INTRO:
            draw_librarian_intro()
        elif CURRENT_STATE == QUIZ_GAME:
            quiz.draw(screen)
        elif CURRENT_STATE == END_SCREEN:
            quiz.draw_end_screen(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
