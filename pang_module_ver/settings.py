import os
import pygame

current_dir = os.path.dirname(__file__)
asset_path = os.path.join(current_dir, "..", 'assets')

bg_img = os.path.join(asset_path, 'background.png')
stage_img = os.path.join(asset_path, 'stage.png')
character_img = os.path.join(asset_path, 'character.png')
weapon_img = os.path.join(asset_path, 'weapon.png')
ball1_img = os.path.join(asset_path, 'ball1.png')
ball2_img = os.path.join(asset_path, 'ball2.png')
ball3_img = os.path.join(asset_path, 'ball3.png')
ball4_img = os.path.join(asset_path, 'ball4.png')

background = pygame.image.load(bg_img) # 배경 이미지 로드
bg_size = background.get_rect() # 배경이미지 크기 가져오기

# 배경이미지 크기에 맞춰서 스크린 크기 세팅
screen_width = bg_size.width
screen_height = bg_size.height

# 게임 타이틀
title = "Escfrog Pang!"

# 폰트 세팅
game_font = pygame.font.Font(None, 40)

# 총 플레이 시간
total_time = 120

# 캐릭터와 적의 속도 설정
character_speed = 0.5
enemy_speed = 0.3
weapon_speed = 0.3