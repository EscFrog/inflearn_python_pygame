# main.py
import pygame
import settings
from game_objects import Character, Ball, Weapon
import game_functions as gf

pygame.init()
pygame.display.set_caption(settings.title)

# 캐릭터 객체 인스턴스화
character = Character(settings.character_img)

# 무기 인스턴스를 담을 배열 선언
weapons = []

# 공 인스턴스를 담을 배열 선언
balls = []

screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

isGameOn = True
clock = pygame.time.Clock()

# 시간 시간 확인
start_ticks = pygame.time.get_ticks()

# 폰트 객체 생성
game_font = pygame.font.Font(None, 40)

# 최초 공 생성
balls.append(Ball(0, 50)) 

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
        character.rect.x -= character.speed * dt
    if keys[pygame.K_RIGHT]:
        character.rect.x += character.speed * dt


    # 무기 움직임 실행
    for weapon in weapons:
        weapon.flyProjectile(dt)

    # 공 움직임 실행
    for ball in balls:
        ball.bounce(dt)

    # 공과 무기 충돌 처리
    for weapon_idx, weapon_instance in enumerate(weapons):
        for ball_index, ball_instance in enumerate(balls):
            if ball_instance.rect.colliderect(weapon_instance.rect):
                # 충돌한 인스턴스들 삭제 가능으로 표시
                if not weapon_instance.deletable:
                    weapon_instance.deletable = True
                    ball_instance.deletable = True

                 # 다음에 소환할 공이 있으면 다음 단계 공 생성
                if ball_instance.ball_type + 1 < len(settings.ball_images):
                    balls.append(
                        Ball(
                            ball_instance.rect.x,
                            ball_instance.rect.y,
                            ball_type_num = ball_instance.ball_type + 1,
                            init_direction = "right"
                            )
                        )
                    # 다음 단계 공 생성
                    balls.append(
                        Ball(
                            ball_instance.rect.x,
                            ball_instance.rect.y,
                            ball_type_num = ball_instance.ball_type + 1,
                            init_direction = "left"
                            )
                        )
    
    # 삭제 예정으로 처리한 공과 무기들 삭제
    for weapon_index, weapon_instance in enumerate(weapons):
        if weapon_instance.deletable == True:
            del weapons[weapon_index]
    
    for ball_index, ball_instance in enumerate(balls):
        if ball_instance.deletable == True:
            del balls[ball_index]

    # # 공과 캐릭터 충돌 처리
    # if gf.check_collision(character, balls):
    #     isGameOn = False
    
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 경과 시간(ms)을 1000으로 나누어 초 단위로 표시.
    timer = game_font.render(str(int(settings.total_time - elapsed_time)), True, (255, 0, 0))

    if elapsed_time >= settings.total_time:
        isGameOn = False

    gf.update_screen(screen, character, weapons, balls, timer)

pygame.time.delay(1000) # 1초 정도 대기
pygame.quit()
