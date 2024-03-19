import os

# 화면 크기 설정
screen_width = 480
screen_height = 640

# 게임 타이틀
title = "Escfrog Game"

# 총 플레이 시간
total_time = 10

# 캐릭터와 적의 속도 설정
character_speed = 0.5

current_dir = os.path.dirname(__file__)
asset_path = os.path.join(current_dir, "..", 'assets')

bg_img_path = os.path.join(asset_path, 'bg_desert.png')
character_img_path = os.path.join(asset_path, 'character_girl.png')
enemy_img_path = os.path.join(asset_path, 'enemy_zombie.png')