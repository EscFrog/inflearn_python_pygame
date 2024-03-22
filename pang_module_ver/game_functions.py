import pygame
import settings

def check_collision(character, enemies):
  # 가로 경계값 처리
  if character.rect.x < 0:
    character.rect.x = 0
  elif character.rect.x > (settings.screen_width - character.rect.width):
    character.rect.x = (settings.screen_width - character.rect.width)

  # 세로 경계값 처리
  if character.rect.y < 0:
    character.rect.y = 0
  elif character.rect.y > (settings.screen_height - character.rect.height):
    character.rect.y = (settings.screen_height - character.rect.height)

  for enemy in enemies:
    if character.rect.colliderect(enemy.rect):
      return True

def update_screen(screen, background, character, enemies, timer):
  screen.blit(background, (0, 0))
  screen.blit(character.image, character.rect)
  for enemy in enemies:
    screen.blit(enemy.image, enemy.rect)
  screen.blit(timer, (10, 10))
  pygame.display.update()
