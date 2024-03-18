# main.py
import os
import pygame
import settings
from game_objects import Character, Enemy
import game_functions as gf

pygame.init()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption(settings.title)

current_dir = os.path.dirname(__file__)
bg_img_path = os.path.join(current_dir, "..", 'assets', 'bg_desert.png')
character_img_path = os.path.join(current_dir, "..", 'assets', 'character_girl.png')
enemy_img_path = os.path.join(current_dir, "..", 'assets', 'enemy_zombie.png')

background = pygame.image.load(bg_img_path)
character = Character(character_img_path)
enemy = Enemy(enemy_img_path)

isGameOn = True
clock = pygame.time.Clock()

while isGameOn:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character.rect.x -= character.speed * dt
    if keys[pygame.K_RIGHT]:
        character.rect.x += character.speed * dt
    if keys[pygame.K_UP]:
        character.rect.y -= character.speed * dt
    if keys[pygame.K_DOWN]:
        character.rect.y += character.speed * dt

    if gf.check_collision(character, enemy):
        print("충돌 발생!")
        isGameOn = False

    gf.update_screen(screen, background, character, enemy)

pygame.time.delay(1000) # 1초 정도 대기
pygame.quit()
