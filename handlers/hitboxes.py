import pygame

# Initializing
pygame.init()

# hitboxes for buildings to determine collisions and create walls
# Rect creates a rectangle at the set coordinates with the specified dimensions

# IT dept hitboxes
it_dept_A_1 = pygame.Rect(185, 80, 120, 95)
it_dept_A_2 = pygame.Rect(185, 170, 40, 40)
it_dept_A_3 = pygame.Rect(270, 170, 35, 40)

# library hitboxes
library_B_1 = pygame.Rect(190, 525, 110, 40)
library_B_2 = pygame.Rect(180, 560, 40, 50)
library_B_3 = pygame.Rect(270, 560, 40, 50)

# counselling office hitboxes
counselling_office_1 = pygame.Rect(465, 300, 120, 50)
counselling_office_2 = pygame.Rect(465, 330, 38, 50)
counselling_office_3 = pygame.Rect(550, 330, 38, 50)
counselling_office_4 = pygame.Rect(520, 265, 25, 30)

# classroom
classroom_1 = pygame.Rect(725, 140, 120, 60)
classroom_2 = pygame.Rect(725, 210, 30, 20)
classroom_3 = pygame.Rect(815, 210, 30, 20)
classroom_4 = pygame.Rect(773, 103, 25, 40)

# cafeteria hitboxes
cafeteria_1 = pygame.Rect(797, 462, 97, 90)
cafeteria_2 = pygame.Rect(797, 540, 60, 50)

# dictionary with hitboxes to check collisions against in character movement in character movement file
hitboxes = {
    "it_dept_1": it_dept_A_1,
    "it_dept_2": it_dept_A_2,
    "it_dept_3": it_dept_A_3,
    "library_1": library_B_1,
    "library_2": library_B_2,
    "library_3": library_B_3,
    "counselling_office_1": counselling_office_1,
    "counselling_office_2": counselling_office_2,
    "counselling_office_3": counselling_office_3,
    "counselling_office_4": counselling_office_4,
    "classroom_1": classroom_1,
    "classroom_2": classroom_2,
    "classroom_3": classroom_3,
    "classroom_4": classroom_4,
    "cafeteria_1": cafeteria_1,
    "cafeteria_2": cafeteria_2
}


# hitbox collision function, you pass the new rectangle matching player position and the intended hitbox dictionary
def check_collision(new_rect, hitboxes):
    # if there's a match between a coordinates of a hitbox in the dict and new_rect(new player position) return true
    for hitbox in hitboxes.values():
        if new_rect.colliderect(hitbox):
            return True
    return False

if __name__ == "__main__":

    # THIS IS THE CODE I HAD PREVIOUSLY IMPLEMENTED IN THE MAIN FILE TO IMPLEMENT THE HITBOXES

    # we need a new_position variable to check for collision, before we update player position
    new_position = player_position.copy()

    # movement of character
    if keyboard[pygame.K_UP] and character_rect.y > 20:
        new_position.y -= 250 * dt
    if keyboard[pygame.K_DOWN] and character_rect.y < SCREEN_HEIGHT - 77:
        new_position.y += 250 * dt
    if keyboard[pygame.K_LEFT] and character_rect.x > 20:
        new_position.x -= 250 * dt
    if keyboard[pygame.K_RIGHT] and character_rect.x < SCREEN_WIDTH - 52:
        new_position.x += 250 * dt

    # updates player hitbox position
    new_rect = character.get_rect(center=new_position)

    # checks for collision
    collision_detected = check_collision(new_rect, hitboxes)
    # it will only update if collision returns false
    if collision_detected == False:
        player_position = new_position
