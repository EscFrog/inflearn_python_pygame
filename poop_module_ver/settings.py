import os
import pygame

current_dir = os.path.dirname(__file__)
asset_path = os.path.join(current_dir, "..", 'assets')

bg_img_path = os.path.join(asset_path, 'bg_paper.png')
character_img_path = os.path.join(asset_path, 'character_dog.png')
enemy_img_path = os.path.join(asset_path, 'enemy_poop.png')

background = pygame.image.load(bg_img_path) # 배경 이미지 로드
bg_size = background.get_rect() # 배경 크기 세팅

screen_width = bg_size.width
screen_height = bg_size.height

# 게임 타이틀
title = "Escfrog Game"

# 총 플레이 시간
total_time = 120

# 캐릭터와 적의 속도 설정
character_speed = 0.5