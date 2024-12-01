class Menu:
    def __init__(self, manager):
        self.manager = manager
        self.font_path = "assets/main_menu/PressStart2P-Regular.ttf"
        self.title_font = pygame.font.Font(self.font_path, 40)
        self.option_font = pygame.font.Font(self.font_path, 30)
        self.click_sound = pygame.mixer.Sound('assets/main_menu/click.mp3')
        self.start_sound = pygame.mixer.Sound('assets/main_menu/starts.mp3')
        self.menu_options = ["Start Game", "High Scores", "Quit"]
        self.menu_background = pygame.image.load('assets/main_menu/thesisquest.png').convert()

    def display(self):
        self.manager.screen.blit(self.menu_background, (0, 0))
        title_text = self.title_font.render("Main Menu", True, WHITE)
        self.manager.screen.blit(
            title_text,
            (
                SCREEN_WIDTH // 2 - title_text.get_width() // 2,
                120,
            ),
        )

        for i, option in enumerate(self.menu_options):
            color = PURPLE if i == self.manager.selected_option else WHITE
            option_text = self.option_font.render(option, True, color)
            self.manager.screen.blit(
                option_text,
                (
                    SCREEN_WIDTH // 2 - option_text.get_width() // 2,
                    180 + i * 45,
                ),
            )

        pygame.display.flip()

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.click_sound.play()
                self.manager.selected_option = (self.manager.selected_option + 1) % len(self.menu_options)
            elif event.key == pygame.K_UP:
                self.click_sound.play()
                self.manager.selected_option = (self.manager.selected_option - 1) % len(self.menu_options)
            elif event.key == pygame.K_RETURN:
                self.start_sound.play()
                self.select_option()

    def select_option(self):
        if self.manager.selected_option == 0:  # Start Game
            self.manager.game_state = GameState.GAME
            pygame.mixer.music.load('assets/main_menu/mapmusic.mp3')
            pygame.mixer.music.play(-1)
        elif self.manager.selected_option == 1:  # High Scores
            pass  # Add functionality
        elif self.manager.selected_option == 2:  # Quit
            pygame.quit()
            sys.exit()