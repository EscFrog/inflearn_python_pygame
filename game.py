import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Escfrog Game") # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("assets/efgame_background.png")

# 캐릭터 스프라이트 불러오기
character = pygame.image.load("assets/efgame_character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 넓이
character_height = character_size[1] # 캐릭터의 높이
character_x_pos = (screen_width - character_width) / 2  # 화면 가로의 절반 크기의 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로의 가장 아래에 해당하는 곳에 위치

# 이동할 좌표
move_x = 0
move_y = 0

# 이동 속도
character_speed = 0.5

# 적 캐릭터
enemy = pygame.image.load("assets/efgame_enemy.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 넓이
enemy_height = enemy_size[1] # 캐릭터의 높이
enemy_x_pos = (screen_width - enemy_width) / 2  # 화면 가로의 절반 크기의 해당하는 곳에 위치
enemy_y_pos = (screen_height - enemy_height) / 2 # 화면 세로의 가장 아래에 해당하는 곳에 위치


# 이벤트 루프 (프레임 마다 실행)
isGameOn = True # 게임이 진행중인가?
while isGameOn:
  dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정
  # print("fps : " + str(clock.get_fps()))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      isGameOn = False
    
    # 키 눌렀을 때 입력값 처리
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        move_x -= character_speed
      elif event.key == pygame.K_RIGHT:
        move_x += character_speed
      elif event.key == pygame.K_UP:
        move_y -= character_speed
      elif event.key == pygame.K_DOWN:
        move_y += character_speed

    # 키 뗏을 때 이벤트 처리
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        move_x = 0
      elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        move_y = 0

  character_x_pos += move_x * dt
  character_y_pos += move_y * dt

  # 가로 경계값 처리
  if character_x_pos < 0:
    character_x_pos = 0
  elif character_x_pos > (screen_width - character_width):
    character_x_pos = (screen_width - character_width)

  # 세로 경계값 처리
  if character_y_pos < 0:
    character_y_pos = 0
  elif character_y_pos > (screen_height - character_height):
    character_y_pos = (screen_height - character_height)

  # 충돌 처리를 위한 rect 정보 업데이트
  character_rect = character.get_rect()
  character_rect.left = character_x_pos
  character_rect.top = character_y_pos

  enemy_rect = enemy.get_rect()
  enemy_rect.left = enemy_x_pos
  enemy_rect.top = enemy_y_pos

  # 충돌 체크
  if character_rect.colliderect(enemy_rect):
    print("충돌!")
    isGameOn = False

  # screen.fill((91, 110, 87)) # 배경에 색 채우기
  screen.blit(background, (0, 0)) # 배경 그리기

  screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
  
  screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 캐릭터 그리기

  pygame.display.update() # 게임 화면을 다시 그리기!

# pygame 종료
pygame.quit()