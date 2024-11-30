import pygame
from config import *

class Character:

    def __init__(self, surface, spritesheet_image, animation_frames, bg_colour, width, height):
        self.width = width
        self.height = height
        # position of character and its rect
        self.player_position = pygame.Vector2(surface.get_width() / 2, surface.get_height() / 2)
        self.character_rect = pygame.Rect(self.player_position.x, self.player_position.y, width, height)

        # character animation
        self.spritesheet_image = pygame.image.load(spritesheet_image).convert_alpha()
        self.bg_colour = bg_colour
        self.last_animation_time = pygame.time.get_ticks()
        self.animation_cooldown = 300
        self.frame = 0
        self.load_frames(animation_frames)



    def load_frames(self, animation_frames):
        self.animation_list = []
        for frame in range(animation_frames):
            frame_image = pygame.Surface((self.width, self.height)).convert_alpha()
            frame_image.blit(self.spritesheet_image, (0, 0), ((frame * self.width), 0, self.width, self.height))
            frame_image.set_colorkey(self.bg_colour)
            self.animation_list.append(frame_image)


    def animate(self, surface):

        self.current_animation_time = pygame.time.get_ticks()
        if self.current_animation_time - self.last_animation_time >= self.animation_cooldown:
            self.frame += 1
            self.last_animation_time = self.current_animation_time
            if self.frame >= len(self.animation_list):
                self.frame = 0

        surface.blit(self.animation_list[self.frame], self.character_rect.topleft)


    def move(self, speed, dt):
        """Character movement"""
        keyboard = pygame.key.get_pressed()

        if keyboard[pygame.K_UP] and self.character_rect.y > 0:
            self.player_position.y -= speed * dt
        if keyboard[pygame.K_DOWN] and self.character_rect.y < SCREEN_HEIGHT - self.height:
            self.player_position.y += speed * dt
        if keyboard[pygame.K_LEFT] and self.character_rect.x > 0:
            self.player_position.x -= speed * dt
        if keyboard[pygame.K_RIGHT] and self.character_rect.x < SCREEN_WIDTH - self.width:
            self.player_position.x += speed * dt

        # syncs character position with it's rect
        self.character_rect.topleft = self.player_position