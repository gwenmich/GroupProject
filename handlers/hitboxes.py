import pygame


# Initializing
pygame.init()


# IT dept hitboxes
it_dept_A_1 = pygame.Rect(185, 80, 120, 95)
it_dept_A_2 = pygame.Rect(185, 170, 40, 40)
it_dept_A_3 = pygame.Rect(270, 170, 35, 40)
# library hitboxes
library_B_1 = pygame.Rect(190, 525, 110, 40)
library_B_2 = pygame.Rect(180, 560, 40, 50)
library_B_3 = pygame.Rect(270, 560, 40, 50)
# councelling office hir=tboxes
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
