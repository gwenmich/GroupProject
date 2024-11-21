import pygame
import sys
from abc import ABC, abstractmethod


class Screen(ABC):

    def __init__(self, screen, height, width, tile_size):
        self.screen = screen
        self.height = height
        self.width = width
        self.tile_size = tile_size

    @abstractmethod
    def draw(self):
        pass

class GameScreen(Screen):


class MenuScreen(Screen):



