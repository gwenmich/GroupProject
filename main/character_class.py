import pygame
from main_config import *
from handlers.hitboxes import *
from utilities.speech_bubble_map import MapBubbles

class Character:

    def __init__(self, surface, spritesheet_image, animation_frames, bg_colour, width, height):
        self.width = width
        self.height = height
        # position of character and its rect
        self.player_position = pygame.Vector2(surface.get_width() / 2, surface.get_height() / 2 + 40)
        self.character_rect = pygame.Rect(self.player_position.x, self.player_position.y, width, height)

        # character animation
        self.spritesheet_image = pygame.image.load(spritesheet_image).convert_alpha()
        print(self.spritesheet_image.get_width(), self.spritesheet_image.get_height())
        self.bg_colour = bg_colour
        self.last_animation_time = pygame.time.get_ticks()
        self.animation_cooldown = 300
        self.frame = 0
        self.load_frames(animation_frames)
        self.building_bubble = MapBubbles(surface, 0, 0, "")




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

        # pygame.draw.rect(surface, (255, 0, 0), self.character_rect)

    def move(self, speed, dt):
        """Character movement"""
        keyboard = pygame.key.get_pressed()

        # we need to create a new variable that's a copy of the player to position to check collision without updating
        # player position
        new_position = self.player_position.copy()

        if keyboard[pygame.K_UP] and self.character_rect.y > 20:
            self.player_position.y -= speed * dt
        if keyboard[pygame.K_DOWN] and self.character_rect.y < SCREEN_HEIGHT - 83:
            self.player_position.y += speed * dt
        if keyboard[pygame.K_LEFT] and self.character_rect.x > 5:
            self.player_position.x -= speed * dt
        if keyboard[pygame.K_RIGHT] and self.character_rect.x < SCREEN_WIDTH - 67:
            self.player_position.x += speed * dt

        # same as new position, we need a copy of rect to check collision
        new_rect = self.character_rect.copy()
        new_rect.topleft = self.player_position

        # calling check_collision function that checks against dict with all hitboxes
        collision_detected = check_collision(new_rect, hitboxes)

        # bubble_collision = check_collision_items()
        # if

        # Only update the position if no collision is detected
        if collision_detected == False:
            # if no collision update player position to those coordinates
            self.character_rect.topleft = self.player_position
        else:
            print("Collision detected, movement prevented.")
            # the position stays the same as the variable we saved before the move
            self.player_position = new_position
            self.character_rect.topleft = self.player_position

            self.building_bubble.handler(new_rect, buildings_bubble_hitboxes, bubble_position)
            if self.building_bubble.visible_bubble == True:
                self.building_bubble.draw()