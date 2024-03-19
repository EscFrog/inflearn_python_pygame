import pygame
import settings

class Character(pygame.sprite.Sprite):
    def __init__(self, img_source):
        super().__init__()
        self.image = pygame.image.load(img_source)
        self.rect = self.image.get_rect()
        self.rect.x = (settings.screen_width - self.rect.width) / 2
        self.rect.y = settings.screen_height - self.rect.height
        self.speed = settings.character_speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self, img_source):
        super().__init__()
        self.image = pygame.image.load(img_source)
        self.rect = self.image.get_rect()
        self.rect.x = (settings.screen_width - self.rect.width) / 2
        self.rect.y = (settings.screen_height / 2) - self.rect.height
