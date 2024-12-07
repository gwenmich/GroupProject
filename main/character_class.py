import pygame
from main_config import *
from handlers.hitboxes import *
from utilities.speech_bubble_map import MapBubbles

class Character:

    def __init__(self, surface, spritesheet_image, animation_frames, bg_colour, width, height):
        self.width = width
        self.height = height
        # Position of character and its rect
        self.character_position = pygame.Vector2(surface.get_width() / 2, surface.get_height() / 2 + 50)
        self.character_rect = pygame.Rect(self.character_position.x, self.character_position.y, width, height)

        # Character animation layout
        self.spritesheet_image = pygame.image.load(spritesheet_image).convert_alpha()
        print(self.spritesheet_image.get_width(), self.spritesheet_image.get_height())
        self.bg_colour = bg_colour
        self.animation_list = []
        self.last_animation_time = pygame.time.get_ticks()
        self.animation_cooldown = 300
        self.frame = 0
        self.load_frames(animation_frames)
        self.building_bubble = MapBubbles(surface, 0, 0, "")
        self.character_location = "Map"




    def load_frames(self, animation_frames):
        """Adds frames from spritesheet into animation list for animation loop"""
        for frame in range(animation_frames):
            frame_image = pygame.Surface((self.width, self.height)).convert_alpha()
            frame_image.blit(self.spritesheet_image, (0, 0), ((frame * self.width), 0, self.width, self.height))
            frame_image.set_colorkey(self.bg_colour)
            self.animation_list.append(frame_image)


    def animate(self, surface):
        """Creates animation loop"""
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

        # Saving the original character position to revert to if collision happens
        new_position = self.character_position.copy()

        if keyboard[pygame.K_UP] and self.character_rect.y > 20:
            self.character_position.y -= speed * dt
        if keyboard[pygame.K_DOWN] and self.character_rect.y < SCREEN_HEIGHT - 83:
            self.character_position.y += speed * dt
        if keyboard[pygame.K_LEFT] and self.character_rect.x > 5:
            self.character_position.x -= speed * dt
        if keyboard[pygame.K_RIGHT] and self.character_rect.x < SCREEN_WIDTH - 67:
            self.character_position.x += speed * dt

        # Same as with new position, we need a copy of rect to check collision
        new_rect = self.character_rect.copy()
        new_rect.topleft = self.character_position

        # Calling check_collision function that checks against dict with all hitboxes
        collision_detected = check_collision(new_rect, hitboxes)

        # Only update the position if no collision is detected
        if not collision_detected:
            # If no collision update character position to those coordinates
            self.character_rect.topleft = self.character_position
        else:
            print("Collision detected, movement prevented.")
            # Character position stays the same as the variable we saved before the move
            self.character_position = new_position
            self.character_rect.topleft = self.character_position

        # Checking if player hit entry hitbox to trigger minigame
        # enter_building(self.character_rect)
        self.character_location = enter_building(self.character_rect)

        # Bubble collision check
        self.building_bubble.handler(new_rect, buildings_bubble_hitboxes, bubble_position)
        if self.building_bubble.visible_bubble == True:
            self.building_bubble.draw()