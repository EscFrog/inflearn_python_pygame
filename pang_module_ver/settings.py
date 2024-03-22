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

 # 배경 이미지 로드 및 크기 세팅
background = pygame.image.load(bg_img)
bg_rect = background.get_rect()

# 배경이미지 크기에 맞춰서 스크린 크기 세팅
screen_width = bg_rect.width
screen_height = bg_rect.height

# 스테이지 로드 및 크기 세팅
stage = pygame.image.load(stage_img)
stage_height = stage.get_rect().height

# 바닥 위치 세팅
floor_pos = screen_height - stage_height

# 게임 타이틀
title = "Escfrog Pang!"

# 총 플레이 시간
total_time = 120

# 캐릭터와 적의 속도 설정
character_speed = 0.5
enemy_speed = 0.3
weapon_speed = 0.3