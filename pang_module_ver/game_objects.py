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
    def __init__(self, pos_x, pos_y, ball_type_num=0, init_direction="right"):
        super().__init__(settings.ball_images[ball_type_num])
        self.ball_type = ball_type_num
        self.rect.x = pos_x
        self.rect.y = pos_y
        
        # 처음 속도는 설정 속도의 2/3
        if init_direction == "left":
            self.velocity_x = -settings.ball_speed[ball_type_num][0] * (2 / 3)
        else:
            self.velocity_x = settings.ball_speed[ball_type_num][0] * (2 / 3)
        self.velocity_y = settings.ball_speed[ball_type_num][1] * (2 / 3)
        
        self.initial_velocity_y = settings.ball_speed[ball_type_num][1]  # 초기 낙하 속도 저장
        self.deletable = False
    
    def bounce(self, dt):
        self.rect.x += self.velocity_x * dt
        self.rect.y += self.velocity_y * dt

        self.velocity_y += settings.gravity
         
        # 가로벽에 닿았을 때 공 이동 위치 변경 (튕겨 나오는 효과)
        if self.rect.x < 0 or self.rect.x > settings.screen_width - self.rect.width:
            self.velocity_x *= -1

        # 바닥에 닿았을 때 튕겨 오르기
        if self.rect.y >= settings.screen_height - settings.stage_height - self.rect.height:
            self.rect.y = settings.screen_height - settings.stage_height - self.rect.height  # 위치 조정
            self.velocity_y = -abs(self.initial_velocity_y)  # 초기 세로 속도로 재설정


class Weapon(Game_object):
    def __init__(self, img_source, character):
        super().__init__(img_source)
        self.rect.x = character.rect.x
        self.rect.y = character.rect.y
        self.speed = settings.weapon_speed
        self.deletable = False
    
    def flyProjectile(self, dt):
        self.rect.y -= self.speed * dt
        # 화면 밖으로 나가면 삭제 가능으로 표시
        if self.rect.y + self.rect.height <= 0:
            self.deletable = True