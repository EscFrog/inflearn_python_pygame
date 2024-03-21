import os
import pygame
############################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Escfrog Game") # 게임 이름

# FPS
clock = pygame.time.Clock()
############################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 이미지 경로 설정
current_path = os.path.dirname(__file__)
img_path = os.path.join(current_path, "images",)

bg_img = os.path.join(img_path, "background.png")
stage_img = os.path.join(img_path, "stage.png")
character_img = os.path.join(img_path, "character.png")
weapon_img = os.path.join(img_path, "weapon.png")

# 배경 만들기
bg = pygame.image.load(bg_img)

# 스테이지 만들기
stage = pygame.image.load(stage_img)
stage_height = stage.get_rect().height

# 캐릭터 만들기
character = pygame.image.load(character_img)
character_width = character.get_rect().width
character_height = character.get_rect().height
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - stage_height - character_height

# 이벤트 루프 (프레임 마다 실행)
isGameOn = True
while isGameOn:
  dt = clock.tick(30)

  # 2. 이벤트 처리 (키보드, 마우스 등)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      isGameOn = False

  # 3. 게임 캐릭터 위치 정의

  # 4. 충돌 처리
  
  # 5. 화면에 그리기
  screen.blit(bg, (0, 0))
  screen.blit(stage, (0, screen_height - stage_height))
  screen.blit(character, (character_x_pos, character_y_pos))

  pygame.display.update() # 게임 화면을 다시 그리기!

# pygame 종료
pygame.quit()