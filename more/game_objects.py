import pygame
from settings import *

class Character:
    def __init__(self):
        self.image = pygame.image.load("assets/efgame_character.png")
        self.x_pos = (screen_width - self.image.get_width()) / 2
        self.y_pos = screen_height - self.image.get_height()

class Enemy:
    def __init__(self):
        self.image = pygame.image.load("assets/efgame_enemy.png")
        self.x_pos = (screen_width - self.image.get_width()) / 2
        self.y_pos = (screen_height - self.image.get_height()) / 2
