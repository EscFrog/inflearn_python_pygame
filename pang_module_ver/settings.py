import os
import pygame

# 게임 타이틀
title = "Escfrog Pang!"

# 총 플레이 시간
total_time = 60

# 리소스 경로 세팅
current_dir = os.path.dirname(__file__)
asset_path = os.path.join(current_dir, "..", 'assets')

bg_img = os.path.join(asset_path, 'background.png')
stage_img = os.path.join(asset_path, 'stage.png')
character_img = os.path.join(asset_path, 'character.png')
weapon_img = os.path.join(asset_path, 'weapon.png')

# 공 이미지 리스트. 공이 분열하려면 이 리스트를 참조해서 다음 공이 있는지를 판단한다.
ball_images = [
  os.path.join(asset_path, 'ball1.png'),
  os.path.join(asset_path, 'ball2.png'),
  os.path.join(asset_path, 'ball3.png'),
  os.path.join(asset_path, 'ball4.png')
  ]

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

# 캐릭터 속도
character_speed = 0.5

# 무기 속도
weapon_speed = 0.5

# 공 속도
ball_speed = [(0.3, -1.0), (0.3, -0.84), (0.3, -0.68), (0.3, -0.52)]

# 공에 적용할 중력
gravity = 0.05