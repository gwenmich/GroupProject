from unittest import TestCase
from handlers.hitboxes import check_collision, TooManyArguments, InvalidInput
import pygame


# the collision function is central to the game, as it is a first step in creating boundaries for the hero character, as
# well as setting the triggers for the minigames

class TestCollisionCheck(TestCase):
    # standard test
    def test_collision_True(self):
        # test character rect and position
        character_rect = pygame.Rect(200, 200, 64, 64)

        # mock hit box list
        hitboxes = {
            "classroom": pygame.Rect(190, 525, 110, 40),
            "library": pygame.Rect(190, 200, 110, 40),
            "it_dept": pygame.Rect(190, 525, 110, 40),
            "cafeteria": pygame.Rect(190, 525, 110, 40),
            "counselling_office": pygame.Rect(190, 525, 110, 40)
        }

        # expecting to find a collision
        expected = True
        result = check_collision(character_rect, hitboxes)
        self.assertEqual(expected, result)

    # test for no collision found
    def test_collision_False(self):
        # test character rect and position
        character_rect = pygame.Rect(800, 500, 64, 64)

        # mock hit box list
        hitboxes = {
            "classroom": pygame.Rect(200, 300, 110, 40),
            "library": pygame.Rect(500, 100, 110, 40),
            "it_dept": pygame.Rect(90, 600, 110, 40),
            "cafeteria": pygame.Rect(800, 100, 110, 40),
            "counselling_office": pygame.Rect(500, 550, 110, 40)
        }

        # expecting not to find a collision
        expected = False
        result = check_collision(character_rect, hitboxes)
        self.assertEqual(expected, result)


    # Raising Exception test
    def test_too_many_args_input(self):
        with self.assertRaises(TooManyArguments):

            # test character rect and position
            character_rect = pygame.Rect(200, 200, 64, 64)

            # mock hit box list
            hitboxes = {
                "classroom": pygame.Rect(190, 525, 110, 40),
                "library": pygame.Rect(190, 200, 110, 40),
                "it_dept": pygame.Rect(190, 525, 110, 40),
                "cafeteria": pygame.Rect(190, 525, 110, 40),
                "counselling_office": pygame.Rect(190, 525, 110, 40)
            }

            check_collision(character_rect, hitboxes, hitboxes)


    # Raising Exception test
    def test_incorrect_input(self):
        with self.assertRaises(InvalidInput):
            # in this case we are passing a tuple instead of using pygame
            character_rect = (200, 200, 64, 64)
            # mock hit box list
            hitboxes = {
                "classroom": pygame.Rect(190, 525, 110, 40),
                "library": pygame.Rect(190, 200, 110, 40),
                "it_dept": pygame.Rect(190, 525, 110, 40),
                "cafeteria": pygame.Rect(190, 525, 110, 40),
                "counselling_office": pygame.Rect(190, 525, 110, 40)
            }
            check_collision(character_rect, hitboxes)



if __name__ == '__main__':
    main()
