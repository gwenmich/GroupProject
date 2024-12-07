#Test for def(animate) to make sure the character will animate as needed. This test is important as if the
#character doesn't animate, then the game can't be played.

from main.character_class import Character
import unittest
from unittest.mock import MagicMock, patch
import pygame

from prototypes.ines_duarte.win_lose_function import initial_time


class TestAnimateMethod(unittest.TestCase):
    def setUp(self):
        pygame.init()
#Initalise pygame

        self.character = Character(
            animation_list=[pygame.Surface((50, 50)) for _ in range(3)],
            character_rect=pygame.Rect(0, 0, 50, 50),
            animation_cooldown=500)# 500 ms cooldown between frame updates

#To quit pygame post test
def teardown(self):
    pygame.quit()


#Testing the animation frames update when enough time has passed
def test_animation_frame_update(self):
    self.character.last_animation_time = pygame.time.get_ticks() - 600
    surface = pygame.surface((800, 600)) #mocked surface to draw on

#Calls the animation method
    self.character.animate(surface)

    self.assertEqual(self.character.frame, 1)

#test for the animation loop and that it goes back to 0 when it reaches the end of a loop.
def test_animation_loop_reset(self):
    self.character.frame = len(self.character.animation_list) - 1
    self.character.last_animation_time = pygame.time.get_ticks() - (self.character.animation_cooldown + 100) #600ms
    surface = pygame.surface((800, 600))

    self.character.animate(surface)

def test_no_frame_update_if_cooldown_not_reached(self):
    self.character.last_animation_time = pygame.time.get_ticks() - (self.character.animation_cooldown - 100) #400ms
    initial_frame = self.character.frame
    surface = pygame.surface((800, 600))

    #Calls animate method
    self.character.animate(surface)
    #Checks frames stay the same
    self.assertequal(self.character.frame, initial_frame)

def test_blit_called_with_correct_frame(self):
    surface = pygame.Surface((800, 600))
    with patch.object(surface, 'blit', wraps=surface.blit) as mock_blit:
        self.character.animate(surface)
#Tests the correct animation frame gets passed to the blit method

#checks the blit was called with the correct frame and position
    mock_blit.assert_called_once_with(
    self.character.animation_list[self.character.frame],
    self.character.character_rect.topleft
    )

if __name__ == '__main__':
    unittest.main