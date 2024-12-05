from unittest import TestCase
from handlers.hitboxes import check_collision, TooManyArguments, InvalidInput, enter_building
import pygame

# the goal of this test suite is to check if when a collision is detected is returning the correct the building name
class TestEnterBuilding(TestCase):

    # building entrance hitbox coordinates
    library = pygame.Rect(230, 540, 35, 40)
    cafeteria = pygame.Rect(850, 525, 40, 40)
    counselling_office = pygame.Rect(510, 327, 35, 40)
    classroom = pygame.Rect(760, 183, 50, 40)
    it_dept = pygame.Rect(230, 150, 35, 40)


    # Library test
    def test_enter_library(self):
        # made the player rect coincide with building rect to test for collision detection
        character_rect = pygame.Rect(230, 540, 64, 64)
        # pass which building it should find
        expected = "library"
        # use assert equal to test the function
        self.assertEqual(enter_building(character_rect), expected)

    # Cafeteria Test - all of the these follow the same pattern as the first one, except they look for collision with each of the 5 buildings
    # by changing the player rect to overlap with those coordinates
    def test_enter_cafeteria(self):
        character_rect = pygame.Rect(850, 525, 64, 64)
        expected = "cafeteria"
        self.assertEqual(enter_building(character_rect), expected)

    # Counselling Office Test
    def test_enter_counselling_office(self):
        character_rect = pygame.Rect(510, 327, 64, 64)
        expected = "counselling_office"
        self.assertEqual(enter_building(character_rect), expected)

    # Classroom Test
    def test_enter_classroom(self):
        character_rect = pygame.Rect(760, 183, 64, 64)
        expected = "classroom"
        self.assertEqual(enter_building(character_rect), expected)

    # IT Dept Test
    def test_enter_it_dept(self):
        character_rect = pygame.Rect(230, 150, 64, 64)
        expected = "it_dept"
        self.assertEqual(enter_building(character_rect), expected)

    # No Collision Test
    def test_enter_no_collision(self):
        # passing coordinates in the middle of grass where there are no buildings
        character_rect = pygame.Rect(600, 400, 64, 64)
        # it is not assert equal as the response on the absense of collision if a FALSE, so I used assertFalse
        expected = False
        self.assertFalse(enter_building(character_rect), expected)
