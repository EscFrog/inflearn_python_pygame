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
ball1_img = os.path.join(img_path, "ball1.png")
ball2_img = os.path.join(img_path, "ball2.png")
ball3_img = os.path.join(img_path, "ball3.png")
ball4_img = os.path.join(img_path, "ball4.png")

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

# 캐릭터 이동 방향
character_to_x = 0

# 캐릭터 이동 속도
character_speed = 0.4

# 무기 만들기
weapon = pygame.image.load(weapon_img)
weapon_width = weapon.get_rect().width
weapon_height = weapon.get_rect().height

# 무기는 한 번에 여러 발 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 0.6

# 공 만들기 (4개 크기에 대해 따로 처리)
ball_images = [
  pygame.image.load(ball1_img),
  pygame.image.load(ball2_img),
  pygame.image.load(ball3_img),
  pygame.image.load(ball4_img)
]

# 공 크기에 따른 최초 스피드
ball_speed_y = [-1.2, -0.9, -0.6, -0.3]

# 공들
balls = []

# 최초 발생하는 큰 공 추가
balls.append({
  "pos_x": 50,
  "pos_y": 50,
  "img_idx": 0,
  "to_x": 0.3,
  "to_y": -0.3,
  "init_spd_y": ball_speed_y[0]
})

# 이벤트 루프 (프레임 마다 실행)
isGameOn = True
while isGameOn:
  dt = clock.tick(60)

  # 2. 이벤트 처리 (키보드, 마우스 등)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      isGameOn = False
    
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        character_to_x -= character_speed
      elif event.key == pygame.K_RIGHT:
        character_to_x += character_speed
      elif event.key == pygame.K_SPACE:
        weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
        weapon_y_pos = character_y_pos
        weapons.append([weapon_x_pos, weapon_y_pos])
    
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        character_to_x = 0
    
  # 3. 게임 캐릭터 위치 정의
  character_x_pos += character_to_x * dt

  # 무기 움직임
  weapons = [[w[0], w[1] - (weapon_speed * dt)] for w in weapons]

  # 천장에 닿은 무기 없애기
  weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

  # 공 위치 정의
  for ball_idx, ball_val in enumerate(balls):
    ball_pos_x = ball_val["pos_x"]
    ball_pos_y = ball_val["pos_y"]
    ball_img_idx = ball_val["img_idx"]

    ball_width = ball_images[ball_img_idx].get_rect().width
    ball_height = ball_images[ball_img_idx].get_rect().height

    # 가로벽에 닿았을 때 공 이동 위치 변경 (튕겨 나오는 효과)
    if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
      ball_val["to_x"] *= -1

    # 세로 위치
    if ball_pos_y >= screen_height - stage_height - ball_width:
      ball_val["to_y"] = ball_val["init_spd_y"]
    else:
      ball_val["to_y"] += 0.04

    ball_val["pos_x"] += ball_val["to_x"] * dt
    ball_val["pos_y"] += ball_val["to_y"] * dt


  # 4. 충돌 처리
  if character_x_pos < 0:
    character_x_pos = 0
  elif character_x_pos > screen_width - character_width:
    character_x_pos = screen_width - character_width
  
  # 5. 화면에 그리기
  screen.blit(bg, (0, 0))
  
  for weapon_x_pos, weapon_y_pos in weapons:
    screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
  
  for idx, val in enumerate(balls):
    ball_pos_x = val["pos_x"]
    ball_pos_y = val["pos_y"]
    ball_img_idx = val["img_idx"]
    screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

  screen.blit(stage, (0, screen_height - stage_height))
  screen.blit(character, (character_x_pos, character_y_pos))

  pygame.display.update() # 게임 화면을 다시 그리기!

# pygame 종료
pygame.quit()