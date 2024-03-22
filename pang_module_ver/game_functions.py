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

def update_screen(screen, character, weapons, balls, timer):
  screen.blit(settings.background, (0, 0))
  for weapon in weapons:
    screen.blit(weapon.image, weapon.rect)
  screen.blit(settings.stage, (0, settings.floor_pos))
  for ball in balls:
    screen.blit(ball.image, ball.rect)
  screen.blit(character.image, character.rect)
  screen.blit(timer, (10, 10))
  pygame.display.update()
