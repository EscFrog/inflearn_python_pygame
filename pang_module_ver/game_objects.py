import pygame
import random
import settings

class Character(pygame.sprite.Sprite):
    def __init__(self, img_source):
        super().__init__()
        self.image = pygame.image.load(img_source)
        self.rect = self.image.get_rect()
        self.rect.x = (settings.screen_width - self.rect.width) / 2
        self.rect.y = settings.screen_height - self.rect.height
        self.speed = settings.character_speed

class Ball(pygame.sprite.Sprite):
    def __init__(self, img_source):
        super().__init__()
        self.image = pygame.image.load(img_source)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, settings.screen_width - self.rect.width)
        self.rect.y = 0
        self.speed = settings.enemy_speed
    
    def bounce(self, dt):
        self.rect.y += self.speed * dt

class Weapon(pygame.sprite.Sprite):
    def __init__(self, img_source):
        super().__init__()
        self.image = pygame.image.load(img_source)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speed = settings.weapon_speed