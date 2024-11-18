import pygame

pygame.init()

# pass where you are bliting and the coordinates
def hitbox_visible_square(surface, y, x, w, h):
    building = pygame.Rect(y, x, w, h)
    # give it transparency
    transparent_surface = pygame.Surface((building.width, building.height), pygame.SRCALPHA)
    transparent_surface.fill((255, 0, 0, 128))  # 128 is the alpha value

    # Blit the semi-transparent hitbox onto the screen
    surface.blit(transparent_surface, (building.x, building.y))