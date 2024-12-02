import pygame
import sys

#initialize Pygame
pygame.init()

#mixer for sound
pygame.mixer.init()

#Screen dimensions
width, height = 1000, 700
#Colours used
pink = (232, 123, 222)
white = (255, 255, 255)
black = (0, 0, 0)

#making the display and giving it the title typing challenge
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Typing Challenge")

#font details
font = "assets/typing_game/PressStart2P.ttf"
title_size = 32
font_size = 14

#setting the timer
timer = 19

#sentences to type
sentences = [
    "Hand in your thesis before the deadline!",
    "This is your final chance to save your PhD!",
    "Type this sentence as fast as you can!",
    "Are you stressed yet? You should be!",
    "This is the final test. Don't give up now!"
]

#sound effects
click = pygame.mixer.Sound("assets/typing_game/click.mp3")
background_music = "assets/typing_game/Scream_Villain.mp3"

#background images
background_image = pygame.image.load("assets/typing_game/background.png").convert()
background_image = pygame.transform.scale(background_image, (width, height))

#manages colours and fonts
class Config:
    @staticmethod
    def colors():
        return {"pink": pink, "white": white, "black": black}

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

    #splits text into lines that fit into the width (so they fit on the screen) and writes it out for the user
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
        y_start = (height // 2) - total_height // 2 + y_offset
        for i, line in enumerate(lines):
            text_surface = font.render(line, True, color)
            text_rect = text_surface.get_rect(center=(width // 2, y_start + i * line_spacing))
            self.screen.blit(text_surface, text_rect)

    #creates buttons to be used in other functions
    def draw_button(self, button_text, y_offset, callback):
        button_width, button_height = 300, 60
        button_x = width // 2 - button_width // 2
        button_y = height // 2 + y_offset
        mouse_pos = pygame.mouse.get_pos()
        hover = pygame.Rect(button_x, button_y, button_width, button_height).collidepoint(mouse_pos)
        scale_factor = 1.1 if hover else 1
        button_width = int(300 * scale_factor)
        button_height = int(60 * scale_factor)
        button_rect = pygame.Rect(width // 2 - button_width // 2, button_y, button_width, button_height)
        pygame.draw.rect(self.screen, black, button_rect)
        pygame.draw.rect(self.screen, white, button_rect, 3)
        text_surface = self.fonts["text"].render(button_text, True, white)
        text_rect = text_surface.get_rect(center=button_rect.center)
        self.screen.blit(text_surface, text_rect)
        if hover and pygame.mouse.get_pressed()[0]:
            pygame.time.delay(200)
            callback()
            click.play()
        return button_rect

    def draw_input_box(self, input_text):
        input_box = pygame.Rect(width // 2 - 300, height // 2 + 100, 600, 50)
        pygame.draw.rect(self.screen, black, input_box)
        pygame.draw.rect(self.screen, white, input_box, 3)
        text_surface = self.fonts["text"].render(input_text, True, white)
        self.screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))

class TypingGame:
    def __init__(self, screen):
        self.screen = screen
        self.game_screen = GameScreen(screen)
        self.current_screen = "intro"
        self.current_challenge = 0
        self.user_input = ""
        self.timer = timer
        self.timer_started = False
        self.typed_text = ""
        self.typing_complete = False
        pygame.mixer.music.load(background_music)
        pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=1000)

    #reset
    def reset_game(self):
        self.current_challenge = 0
        self.user_input = ""
        self.timer = timer
        self.timer_started = False
        self.typed_text = ""
        self.typing_complete = False
        self.current_screen = "intro"

    #displays the introduction screen and give background information as well as the continue button
    def intro_screen(self):
        self.screen.blit(background_image, (0, 0))
        self.game_screen.draw_text("Thesis Typing", self.game_screen.fonts["title"], black, -120, line_spacing=50)
        self.game_screen.draw_text("Challenge!", self.game_screen.fonts["title"], black, -80, line_spacing=50)
        self.game_screen.draw_text("Oh no! Your computer crashed! Rewrite the sentences to save your thesis!", self.game_screen.fonts["text"], black, -20, line_spacing=30)
        button = self.game_screen.draw_button("Continue", 100, self.instructions_screen)

    #displays the instruction screen which tells user how to play as well as start button
    def instructions_screen(self):
        self.screen.blit(background_image, (0, 0))
        self.current_screen = "instructions"
        self.game_screen.draw_text("Instructions:", self.game_screen.fonts["title"], black, -150)
        self.game_screen.draw_text("1. Type the sentences shown on screen.", self.game_screen.fonts["text"], black, -100)
        self.game_screen.draw_text("2. You have 15 seconds per challenge.", self.game_screen.fonts["text"], black, -60)
        self.game_screen.draw_text("3. Press backspace to fix mistakes.", self.game_screen.fonts["text"], black, -20)
        button = self.game_screen.draw_button("Start Challenge", 150, self.typing_challenges)

    #this is for the typing animation in the challenges
    def animate_text(self, text, font, color, y_offset=0, speed=100, max_width=700):
        self.typed_text = ""
        self.typing_complete = False
        for i in range(len(text)):
            self.typed_text += text[i]
            self.screen.fill(pink)
            self.screen.blit(background_image, (0, 0))
            self.game_screen.draw_text(f"Challenge {self.current_challenge + 1}", self.game_screen.fonts["title"], black, -150)
            self.game_screen.draw_text(self.typed_text, font, color, y_offset, max_width=max_width)
            pygame.display.flip()
            pygame.time.delay(speed)
        self.typing_complete = True

    #the challenges
    def typing_challenges(self):
        if self.current_challenge >= len(sentences):
            self.result_screen(True)
            return
        self.current_screen = "challenge"
        self.screen.fill(pink)
        self.screen.blit(background_image, (0, 0))
        if not self.timer_started:
            self.timer = timer
            pygame.time.set_timer(pygame.USEREVENT, 1000)
            self.timer_started = True
        self.game_screen.draw_text(f"Challenge {self.current_challenge + 1}", self.game_screen.fonts["title"], black, -150)
        if not self.typing_complete:
            self.animate_text(sentences[self.current_challenge], self.game_screen.fonts["text"], black, -100)
        if self.typing_complete:
            self.game_screen.draw_text(self.typed_text, self.game_screen.fonts["text"], black, -100)
        self.game_screen.draw_text(f"Time left: {self.timer}", self.game_screen.fonts["text"], black, 50, center=False)
        self.game_screen.draw_input_box(self.user_input)
        #checks if the users input it right to continue to the next challenge
        if self.user_input == sentences[self.current_challenge]:
            self.timer_started = False
            pygame.time.set_timer(pygame.USEREVENT, 0)
            self.current_challenge += 1
            self.user_input = ""
            self.typing_complete = False

    #gives the congratulations or times up message
    def result_screen(self, success):
        self.screen.blit(background_image, (0, 0))
        self.current_screen = "result"
        if success:
            self.game_screen.draw_text("Congratulations! You Win!", self.game_screen.fonts["title"], black, -50)
        else:
            self.game_screen.draw_text("Time's Up! Try Again!", self.game_screen.fonts["title"], black, -50)

        button = self.game_screen.draw_button("Play Again", 100, self.reset_game)

    #deals with the timer
    def update_timer(self):
        if self.timer > 0:
            self.timer -= 1
        else:
            self.result_screen(False) #calls results screen if timer runs out

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
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
            if self.current_screen == "intro":
                self.intro_screen()
            elif self.current_screen == "instructions":
                self.instructions_screen()
            elif self.current_screen == "challenge":
                self.typing_challenges()
            elif self.current_screen == "result":
                self.result_screen(self.timer > 0)
            pygame.display.flip()
            clock.tick(60)

#entry point
if __name__ == "__main__":
    game = TypingGame(screen)
    game.run()