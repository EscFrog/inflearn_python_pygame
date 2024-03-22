import pygame
import random
import settings

class Game_object(pygame.sprite.Sprite):
    def __init__(self, img_source):
        super().__init__()
        self.image = pygame.image.load(img_source)
        self.rect = self.image.get_rect()


class Character(Game_object):
    def __init__(self, img_source):
        super().__init__(img_source)
        self.rect.x = (settings.screen_width - self.rect.width) / 2
        self.rect.y = settings.floor_pos - self.rect.height
        self.speed = settings.character_speed


class Ball(Game_object):
    def __init__(self, img_source):
        super().__init__(img_source)
        self.rect.x = random.randint(0, settings.screen_width - self.rect.width)
        self.rect.y = 0
        self.speed = settings.enemy_speed
    
    def bounce(self, dt):
        self.rect.y += self.speed * dt


class Weapon(Game_object):
    def __init__(self, img_source, character):
        super().__init__(img_source)
        self.rect.x = character.rect.x
        self.rect.y = character.rect.y
        self.speed = settings.weapon_speed
        self.Deletable = False
    
    def flyProjectile(self, dt):
        self.rect.y -= self.speed * dt
        # 화면 밖으로 나간 무기는 삭제 가능으로 변경
        if self.rect.y + self.rect.height <= 0:
            self.Deletable = True