
def hitbox_square_helper(building, y, x, w, h):
    building = pygame.Rect(y, x, w, h)
    transparent_surface = pygame.Surface((building.width, building.height), pygame.SRCALPHA)
    transparent_surface.fill((255, 0, 0, 128))  # 128 is the alpha value

    # Blit the semi-transparent hitbox onto the screen
    screen.blit(transparent_surface, (building.x, building.y))