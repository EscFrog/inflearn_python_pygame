# main.py
import pygame
import settings
from game_objects import Character, Ball
import game_functions as gf

pygame.init()
pygame.display.set_caption(settings.title)

character = Character(settings.character_img)
enemies = []

screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

isGameOn = True
clock = pygame.time.Clock()

# 시간 시간 정보
start_ticks = pygame.time.get_ticks() # 시작 tick을 가져옴

# 폰트 객체 생성
game_font = pygame.font.Font(None, 60)

last_enemy_spawn_time = 0 # 적을 마지막으로 생성한 시점
spawn_enemy_interval = 1000 # 적을 생성하는 간격 (밀리초 단위)

while isGameOn:
    dt = clock.tick(30)
    current_time = pygame.time.get_ticks()  # 현재 시간을 가져옴

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character.rect.x -= character.speed * dt
    if keys[pygame.K_RIGHT]:
        character.rect.x += character.speed * dt
    
    # 적 생성
    if current_time - last_enemy_spawn_time > spawn_enemy_interval:
        enemies.append(Ball(settings.ball1_img))
        last_enemy_spawn_time = current_time  # 마지막 적 생성 시간 업데이트

    # 적 이동 업데이트
    for enemy in enemies:
        enemy.bounce(dt)
        if enemy.rect.y > settings.screen_height:
            enemies.remove(enemy)  # 화면 밖으로 나간 적 제거

    if gf.check_collision(character, enemies):
        print("충돌 발생!")
        isGameOn = False

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 경과 시간(ms)을 1000으로 나누어 초 단위로 표시.
    timer = game_font.render(str(int(settings.total_time - elapsed_time)), True, (255, 0, 0))

    if elapsed_time >= settings.total_time:
        isGameOn = False

    gf.update_screen(screen, settings.background, character, enemies, timer)

pygame.time.delay(1000) # 1초 정도 대기
pygame.quit()
