import pygame



# pass where you are bliting and the coordinates
def hitbox_visible_square(surface, x, y, w, h):
    pygame.init()
    building = pygame.Rect(x, y, w, h)
    # give it transparency
    transparent_surface = pygame.Surface((building.width, building.height), pygame.SRCALPHA)
    # 128 is the alpha value
    transparent_surface.fill((255, 0, 0, 128))

    # Blit the semi-transparent hitbox onto the screen
    surface.blit(transparent_surface, (building.x, building.y))