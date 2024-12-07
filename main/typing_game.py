import pygame
import sys
from main_config import *
import time
# Initialise Pygame
pygame.init()

# Mixer for sound
pygame.mixer.init()

# Setting the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Font details
font = "assets/typing_game/PressStart2P.ttf"
title_size = 32
font_size = 14

# Setting the timer
timer = 20

# Sentences to be typed
sentences = [
    "Hand in your thesis before the deadline!",
    "This is your final chance to save your PhD!",
    "Type this sentence as fast as you can!",
    "Are you stressed yet? You should be!",
    "This is the final test. Don't give up now!"
]

# Sound effects
click = pygame.mixer.Sound("assets/typing_game/click.mp3")
background_music = "assets/typing_game/Scream_Villain.mp3"

# Background images
background_image = pygame.image.load("assets/typing_game/background.png").convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Manages colours and fonts
class Config:
    @staticmethod
    def colors():
        return {"pink": PINK, "white": WHITE, "black": BLACK}

    @staticmethod
    def fonts():
        return {
            "title": pygame.font.Font(font, title_size),
            "text": pygame.font.Font(font, font_size)
        }

class GameScreen:
    def __init__(self, screen):
        self.screen = screen
        self.fonts = Config.fonts()
        self.colors = Config.colors()

    # Splits text into lines that fit into the width of the screen and writes it out for the user
    def draw_text(self, text, font, color, y_offset=0, line_spacing=30, center=True, max_width=700):
        words = text.split()
        lines = []
        current_line = []
        for word in words:
            current_line.append(word)
            line_width = font.size(' '.join(current_line))[0]
            if line_width > max_width:
                current_line.pop()
                lines.append(' '.join(current_line))
                current_line = [word]
        lines.append(' '.join(current_line))
        total_height = len(lines) * line_spacing
        y_start = (SCREEN_HEIGHT // 2) - total_height // 2 + y_offset
        for i, line in enumerate(lines):
            text_surface = font.render(line, True, color)
            text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, y_start + i * line_spacing))
            self.screen.blit(text_surface, text_rect)

    # Creates buttons to be used in other functions
    def draw_button(self, button_text, y_offset, callback):
        button_width, button_height = 300, 60
        button_x = SCREEN_WIDTH // 2 - button_width // 2
        button_y = SCREEN_HEIGHT // 2 + y_offset
        mouse_pos = pygame.mouse.get_pos()
        hover = pygame.Rect(button_x, button_y, button_width, button_height).collidepoint(mouse_pos)
        scale_factor = 1.1 if hover else 1
        button_width = int(300 * scale_factor)
        button_height = int(60 * scale_factor)
        button_rect = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, button_y, button_width, button_height)
        pygame.draw.rect(self.screen, BLACK, button_rect)
        pygame.draw.rect(self.screen, WHITE, button_rect, 3)
        text_surface = self.fonts["text"].render(button_text, True, WHITE)
        text_rect = text_surface.get_rect(center=button_rect.center)
        self.screen.blit(text_surface, text_rect)
        if hover and pygame.mouse.get_pressed()[0]:
            pygame.time.delay(200)
            callback()
            click.play()
        return button_rect

    # Draws box for player to input text
    def draw_input_box(self, input_text):
        input_box = pygame.Rect(SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 + 100, 600, 50)
        pygame.draw.rect(self.screen, BLACK, input_box)
        pygame.draw.rect(self.screen, WHITE, input_box, 3)
        text_surface = self.fonts["text"].render(input_text, True, WHITE)
        self.screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))

class TypingGame:
    def __init__(self, surface):
        self.screen = surface
        self.game_screen = GameScreen(screen)
        self.current_screen = "intro"
        self.current_challenge = 0
        self.user_input = ""
        self.timer = timer
        self.timer_started = False
        self.typed_text = ""
        self.typing_complete = False
        self.victory_status = "Not won"
        self.player_location = "classroom"
        pygame.mixer.music.load(background_music)
        pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=1000)
        self.running = True

    # Reset game
    def reset_game(self):
        self.current_challenge = 0
        self.user_input = ""
        self.timer = timer
        self.timer_started = False
        self.typed_text = ""
        self.typing_complete = False
        self.current_screen = "intro"

    # Displays the introduction screen, give background information and a continue button
    def intro_screen(self):
        self.screen.blit(background_image, (0, 0))
        self.game_screen.draw_text("Thesis Typing", self.game_screen.fonts["title"], BLACK, -120, line_spacing=50)
        self.game_screen.draw_text("Challenge!", self.game_screen.fonts["title"], BLACK, -80, line_spacing=50)
        self.game_screen.draw_text("Oh no! Your computer crashed! Rewrite the sentences to save your thesis!", self.game_screen.fonts["text"], BLACK, -20, line_spacing=30)
        button = self.game_screen.draw_button("Continue", 100, self.instructions_screen)

    # Displays the instruction screen and start button
    def instructions_screen(self):
        self.screen.blit(background_image, (0, 0))
        self.current_screen = "instructions"
        self.game_screen.draw_text("Instructions:", self.game_screen.fonts["title"], BLACK, -150)
        self.game_screen.draw_text("1. Type the sentences shown on screen.", self.game_screen.fonts["text"], BLACK, -100)
        self.game_screen.draw_text("2. You have 15 seconds per challenge.", self.game_screen.fonts["text"], BLACK, -60)
        self.game_screen.draw_text("3. Press backspace to fix mistakes.", self.game_screen.fonts["text"], BLACK, -20)
        button = self.game_screen.draw_button("Start Challenge", 150, self.typing_challenges)

    # Typing animation for the challenges
    def animate_text(self, text, font, color, y_offset=0, speed=100, max_width=700):
        self.typed_text = ""
        self.typing_complete = False
        for i in range(len(text)):
            self.typed_text += text[i]
            self.screen.fill(PINK)
            self.screen.blit(background_image, (0, 0))
            self.game_screen.draw_text(f"Challenge {self.current_challenge + 1}", self.game_screen.fonts["title"], BLACK, -150)
            self.game_screen.draw_text(self.typed_text, font, color, y_offset, max_width=max_width)
            pygame.display.flip()
            pygame.time.delay(speed)
        self.typing_complete = True

    # The typing challenges
    def typing_challenges(self):
        if self.current_challenge >= len(sentences):
            self.result_screen(True)
            return
        self.current_screen = "challenge"
        self.screen.fill(PINK)
        self.screen.blit(background_image, (0, 0))
        if not self.timer_started:
            self.timer = timer
            pygame.time.set_timer(pygame.USEREVENT, 1000)
            self.timer_started = True
        self.game_screen.draw_text(f"Challenge {self.current_challenge + 1}", self.game_screen.fonts["title"], BLACK, -150)
        if not self.typing_complete:
            self.animate_text(sentences[self.current_challenge], self.game_screen.fonts["text"], BLACK, -100)
        if self.typing_complete:
            self.game_screen.draw_text(self.typed_text, self.game_screen.fonts["text"], BLACK, -100)
        self.game_screen.draw_text(f"Time left: {self.timer}", self.game_screen.fonts["text"], BLACK, 50, center=False)
        self.game_screen.draw_input_box(self.user_input)
        # Checks if the user's input is correct to continue to the next challenge
        if self.user_input == sentences[self.current_challenge]:
            self.timer_started = False
            pygame.time.set_timer(pygame.USEREVENT, 0)
            self.current_challenge += 1
            self.user_input = ""
            self.typing_complete = False

    # Gives the congratulations or time's up message
    def result_screen(self, success):
        self.screen.blit(background_image, (0, 0))
        self.current_screen = "result"
        if success:
            self.game_screen.draw_text("Congratulations! You Win!", self.game_screen.fonts["title"], BLACK, -50)
            self.victory_status = "Won"
            button = self.game_screen.draw_button("Exit", 100, self.exit_game)

        else:
            # self.victory_status = "Not won"
            button = self.game_screen.draw_button("Exit", 250, self.exit_game)
            self.game_screen.draw_text("Time's Up! Try Again!", self.game_screen.fonts["title"], BLACK, -50)
            button = self.game_screen.draw_button("Play Again", 100, self.reset_game)

    def exit_game(self):
        self.player_location = "Map"  # Transition back to the map
        self.running = False  # Stop the game loop, transitioning to the map screen

    # Timer mechanics
    def update_timer(self):
        if self.timer > 0:
            self.timer -= 1
        else:
            self.result_screen(False) # Presents results screen if timer runs out

    def load_music(self):
        pygame.mixer.music.load(background_music)
        pygame.mixer.music.play(-1)

    # Game loop
    def play(self):
        clock = pygame.time.Clock()
        pygame.display.set_caption("Typing Challenge")
        self.load_music()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_game()
                    # pygame.quit()
                    # sys.exit()
                if event.type == pygame.USEREVENT:
                    if self.current_screen == "challenge" and self.timer > 0:
                        self.timer -= 1
                    if self.timer <= 0:
                        self.result_screen(False)  # Display the result screen when time is up
                if event.type == pygame.KEYDOWN:
                    if self.current_screen == "challenge":
                        if event.key == pygame.K_BACKSPACE:
                            self.user_input = self.user_input[:-1]
                        elif event.key == pygame.K_RETURN and self.user_input == sentences[self.current_challenge]:
                            self.timer_started = False
                            pygame.time.set_timer(pygame.USEREVENT, 0)
                            self.current_challenge += 1
                            self.user_input = ""
                            self.typing_complete = False
                        else:
                            if len(self.user_input) < 43:
                                self.user_input += event.unicode
                    if self.current_screen == "result":
                        if event.key == pygame.K_e and self.victory_status == "Not won":
                            self.__init__()
                            self.player_location = "Map"
                            self.running = False
                        elif event.key == pygame.K_e:
                            self.player_location = "Map"
                            self.running = False

            if self.current_screen == "intro":
                self.intro_screen()
            elif self.current_screen == "instructions":
                self.instructions_screen()
            elif self.current_screen == "challenge":
                self.typing_challenges()
            elif self.current_screen == "result":
                self.result_screen(self.timer > 0)

            pygame.display.flip()
            clock.tick(FPS)

#entry point
if __name__ == "__main__":
    game = TypingGame(screen)
    game.play()