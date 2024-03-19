# main.py
import pygame
import settings
from game_objects import Character, Enemy
import game_functions as gf

pygame.init()
pygame.display.set_caption(settings.title)

character = Character(settings.character_img_path)
enemy = Enemy(settings.enemy_img_path)

screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

isGameOn = True
clock = pygame.time.Clock()

# 시간 시간 정보
start_ticks = pygame.time.get_ticks() # 시작 tick을 가져옴

# 폰트 객체 생성
game_font = pygame.font.Font(None, 60)

while isGameOn:
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character.rect.x -= character.speed * dt
    if keys[pygame.K_RIGHT]:
        character.rect.x += character.speed * dt

    if gf.check_collision(character, enemy):
        print("충돌 발생!")
        isGameOn = False

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 경과 시간(ms)을 1000으로 나누어 초 단위로 표시.
    timer = game_font.render(str(int(settings.total_time - elapsed_time)), True, (255, 0, 0))

    if elapsed_time >= settings.total_time:
        isGameOn = False
    
    gf.update_screen(screen, settings.background, character, enemy, timer)

pygame.time.delay(1000) # 1초 정도 대기
pygame.quit()
