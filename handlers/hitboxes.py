import pygame

# Initializing
pygame.init()

# hitboxes for buildings to determine collisions and create walls
# Rect creates a rectangle at the set coordinates with the specified dimensions

# IT dept hitboxes
it_dept_A_1 = pygame.Rect(185, 80, 120, 95)
it_dept_A_2 = pygame.Rect(185, 170, 10, 40)
it_dept_A_3 = pygame.Rect(295, 170, 10, 40)

# library hitboxes
library_B_1 = pygame.Rect(190, 525, 110, 40)
library_B_2 = pygame.Rect(180, 560, 10, 50)
library_B_3 = pygame.Rect(297, 560, 10, 50)

# counselling office hitboxes
counselling_office_1 = pygame.Rect(465, 300, 120, 50)
counselling_office_2 = pygame.Rect(465, 330, 10, 50)
counselling_office_3 = pygame.Rect(580, 330, 10, 50)
counselling_office_4 = pygame.Rect(520, 265, 25, 30)

# classroom
classroom_1 = pygame.Rect(725, 140, 120, 60)
classroom_2 = pygame.Rect(725, 210, 10, 20)
classroom_3 = pygame.Rect(835, 210, 10, 20)
classroom_4 = pygame.Rect(773, 103, 25, 40)

# cafeteria hitboxes
cafeteria_1 = pygame.Rect(797, 462, 97, 90)
cafeteria_2 = pygame.Rect(797, 540, 10, 50)

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


# TEXT BUBBLE COORDINATES CODE
library_rect_B = pygame.Rect(175, 515, 140, 100)
cafeteria_rect_B = pygame.Rect(780, 450, 130, 150)
counselling_rect_B = pygame.Rect(452, 280, 150, 115)
classroom_rect_B = pygame.Rect(710, 120, 150, 120)
it_dept_rect_B = pygame.Rect(175, 75, 140, 140)

buildings_bubble_hitboxes = {
    "Library": library_rect_B,
    "Cafeteria": cafeteria_rect_B,
    "Counselling": counselling_rect_B,
    "Classroom": classroom_rect_B,
    "IT Dept.": it_dept_rect_B
}

# for the speech bubble on the menu
bubble_position = {
    "Library": (280, 500),
    "Classroom": (815, 120),
    "Cafeteria": (815, 420),
    "IT Dept.": (280, 120),
    "Counselling": (480, 190)
}

# EXCEPTIONS FOR COLLISION TESTING

# custom exception invalid input
class InvalidInput(Exception):
    """Raised for invalid input value"""
    pass

class TooManyArguments(Exception):
    """Raised when too many arguments are passed"""
    pass

# hitbox collision function, you pass the new rectangle matching player position and the intended hitbox dictionary
def check_collision(new_rect, hitboxes, *args):
    # isinstance will check if the argument new_rect which represents the hero sprite is a pygame.Rect. isinstance is
    # commonly used to test classes
    if not isinstance(new_rect, pygame.Rect):
        raise InvalidInput("Input must be pygame.Rect")

    # error state - more args
    if len(args) > 0:
        raise TooManyArguments("Too many arguments provided.")

    # if there's a match between a coordinates of a hitbox in the dict and new_rect(new player position) return true
    for hitbox in hitboxes.values():
        if new_rect.colliderect(hitbox):
            print(f"Collision detected with: {hitbox}")
            return True
    # if no match found, False
    return False


# similar colision function but checks items not values
def check_collision_items(new_rect, hitboxes):
    for name, rect in hitboxes.items():
        if new_rect.colliderect(rect):
            # if found returns the name so i can get the right coordinates from the their dict by name
            return name
    # if no match found, False
    return False


# Mini Game trigger hitboxes
# buildings' sizes and coordinates on map
library = pygame.Rect(230, 540, 35, 40)
cafeteria = pygame.Rect(850, 525, 40, 40)
counselling_office = pygame.Rect(510, 327, 35, 40)
classroom = pygame.Rect(760, 183, 50, 40)
it_dept = pygame.Rect(230, 150, 35, 40)



def enter_building(character_rect):
    """
    if the character collides with a building and hasn't won that challenge will call the building's mini-game
    """

    entry_hitboxes = {
        "library": library,
        "cafeteria": cafeteria,
        "counselling_office": counselling_office,
        "classroom": classroom,
        "it_dept": it_dept
    }


    games_won = {
        "library": "Not won",
        "cafeteria": "Not won",
        "counselling_office": "Not won",
        "classroom": "Not won",
        "it_dept": "Not won"
    }


    for building, building_rect in entry_hitboxes.items():
        if character_rect.colliderect(building_rect):
            if building == "counselling_office" or games_won[building] == "Not won":
                print(f"you found the entrance to {building}")
                return building
            else:
                print("Sorry, you've already won this game, time to visit another building!")





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
