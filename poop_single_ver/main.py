import os
import pygame
############################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 기본 경로 및 에셋 경로 설정
current_dir = os.path.dirname(__file__)
bg_img_path = os.path.join(current_dir, "..", 'assets', 'bg_paper.png')
character_img_path = os.path.join(current_dir, "..", 'assets', 'character_dog.png')
enemy_img_path = os.path.join(current_dir, "..", 'assets', 'enemy_poop.png')

# 배경 화면 불러오기
background = pygame.image.load(bg_img_path)
bg_size = background.get_rect()

# 화면 크기 설정
screen_width = bg_size.width
screen_height = bg_size.height
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Evading Poop") # 게임 이름

# FPS
clock = pygame.time.Clock()
############################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 캐릭터 스프라이트 불러오기
character = pygame.image.load(character_img_path)
character_rect = character.get_rect() # 이미지의 크기를 구해옴
character_width = character_rect.width # 캐릭터의 넓이
character_height = character_rect.height # 캐릭터의 높이
character_rect.x = (screen_width - character_width) / 2  # 화면 가로의 절반 크기의 해당하는 곳에 위치
character_rect.y = screen_height - character_height # 화면 세로의 가장 아래에 해당하는 곳에 위치

# 적 스프라이트 불러오기
enemy = pygame.image.load(enemy_img_path)
enemy_rect = enemy.get_rect()
enemy_width = enemy_rect.width
enemy_height = enemy_rect.height
enemy_rect.x = (screen_width - enemy_width) / 2
enemy_rect.y = 0

character_speed = 1
enemy_speed = 0.5

# 이벤트 루프 (프레임 마다 실행)
isGameOn = True
while isGameOn:
  dt = clock.tick(60)

  # 2. 이벤트 처리 (키보드, 마우스 등)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      isGameOn = False

  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
      character_rect.x -= character_speed * dt
  if keys[pygame.K_RIGHT]:
      character_rect.x += character_speed * dt
    
  # 3. 게임 캐릭터 위치 정의

  # 4. 충돌 처리
  # 가로 경계값 처리
  if character_rect.x < 0:
    character_rect.x = 0
  elif character_rect.x > (screen_width - character_width):
    character_rect.x = (screen_width - character_width)
  
  # 5. 화면에 그리기
  screen.blit(background, (0, 0)) # 배경 그리기
  screen.blit(character, (character_rect.x, character_rect.y))
  screen.blit(enemy, (enemy_rect.x, enemy_rect.y))


  pygame.display.update() # 게임 화면을 다시 그리기!

# pygame 종료
pygame.quit()