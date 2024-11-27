import pygame
from config import *

class Character:

    def __init__(self, surface, sprite_image, bg_colour):
        # position of character
        self.player_position = pygame.Vector2(surface.get_width() / 2, surface.get_height() / 2)
        self.character_rect = pygame.Rect(self.player_position.x, self.player_position.y, 64, 64)

        # character animation
        self.sprite_image = pygame.image.load(sprite_image).convert_alpha()
        self.bg_colour = bg_colour
        self.animation_list = []
        self.animation_steps = 2
        self.last_animation_update = pygame.time.get_ticks()
        self.animation_cooldown = 300
        self.frame = 0





    def load_frames(self, frame, width, height):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image.set_colorkey(self.bg_colour)
        return image

    def animate(self, surface):
        a

        for x in range(animation_steps):
            animation_list.append(SpriteSheet.get_image(x, 64, 64, self.bg_colour))

        current_animation_time = pygame.time.get_ticks()
        if current_animation_time - last_animation_update >= animation_cooldown:
            frame += 1
            last_animation_update = current_animation_time
            if frame >= len(animation_list):
                frame = 0

        surface.blit(animation_list[frame], Character.character_rect.topleft)

    def move(self):
        """Character movement"""
        keyboard = pygame.key.get_pressed()

        if keyboard[pygame.K_UP] and self.character_rect.y > 0:
            self.player_position.y -= 250 * dt
        if keyboard[pygame.K_DOWN] and self.character_rect.y < SCREEN_HEIGHT - 64:
            self.player_position.y += 250 * dt
        if keyboard[pygame.K_LEFT] and self.character_rect.x > 0:
            self.player_position.x -= 250 * dt
        if keyboard[pygame.K_RIGHT] and self.character_rect.x < SCREEN_WIDTH - 64:
            self.player_position.x += 250 * dt

        # syncs character position with it's rect
        self.character_rect.topleft = self.player_position