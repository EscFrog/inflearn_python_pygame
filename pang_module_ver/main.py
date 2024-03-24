# main.py
import pygame
from random import randint
import settings
from game_objects import Character, Ball, Weapon
import game_functions as gf

pygame.init()
pygame.display.set_caption(settings.title)

# 게임 화면 생성
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

isGameOn = True
clock = pygame.time.Clock()

# 시작 시간 확인
start_ticks = pygame.time.get_ticks()

# 폰트 객체 생성
game_font = pygame.font.Font(None, 40)

# 게임 종료 메시지
game_result = "Game Over"

# 캐릭터 객체 인스턴스화
character = Character(settings.character_img)

# 무기 인스턴스를 담을 배열 선언
weapons = []

# 공 인스턴스를 담을 배열 선언
balls = []

# 최초 공 생성
dir_choice = randint(0, 1)
if dir_choice == 0:
    balls.append(Ball(settings.first_ball_pos_x, settings.first_ball_pos_y, init_direction="right")) 
else:
    balls.append(Ball(settings.first_ball_pos_x, settings.first_ball_pos_y, init_direction="left")) 

while isGameOn:
    dt = clock.tick(30)
    current_time = pygame.time.get_ticks()  # 현재 시간을 가져옴

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameOn = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                weapons.append(Weapon(settings.weapon_img, character))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character.move(dt, "left")
    if keys[pygame.K_RIGHT]:
        character.move(dt, "right")

    # 무기 움직임 실행
    for weapon in weapons:
        weapon.move(dt)

    # 공 움직임 실행
    for ball in balls:
        ball.move(dt)

    # 공과 캐릭터 충돌 처리
    for ball in balls:
        if character.rect.colliderect(ball.rect):
            isGameOn = False

    # 무기와 공의 충돌 처리
    new_balls = [] # 무기에 닿았을 때 분열될 공들을 담을 리스트
    for weapon in weapons:
        for ball in balls:
            if ball.rect.colliderect(weapon.rect) and not ball.deletable:
                weapon.deletable = True
                ball.deletable = True
                new_balls.extend(ball.split())  # 새로운 공들을 생성하여 리스트에 추가

    # 새로운 공들을 기존의 공 리스트에 추가
    balls.extend(new_balls)
    
    # 삭제 가능한 공과 무기들을 빼고 나머지를 리스트에 다시 담기
    weapons = [weapon for weapon in weapons if not weapon.deletable]
    balls = [ball for ball in balls if not ball.deletable]
    
    # 공 리스트에 공이 하나도 남지 않으면 게임 성공
    if len(balls) == 0:
        game_result = "Mission Complete"
        isGameOn = False

    # 경과 시간 계산 및 글자 객체 생성
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 경과 시간(ms)을 1000으로 나누어 초 단위로 표시.
    timer = game_font.render(str(int(settings.total_time - elapsed_time)), True, (255, 0, 0))

    # 경과 시간이 끝나면 게임 종료
    if elapsed_time >= settings.total_time:
        game_result = "Time Over"
        isGameOn = False

    # 화면 업데이트
    gf.update_screen(screen, character, weapons, balls, timer)

# 메인 루프 종료시 마지막 처리
msg = game_font.render(game_result, True, (255, 255, 0))
msg_rect = msg.get_rect(center=(int(settings.screen_width / 2), int(settings.screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()

pygame.time.delay(1500) # 1.5초 정도 대기
pygame.quit()
