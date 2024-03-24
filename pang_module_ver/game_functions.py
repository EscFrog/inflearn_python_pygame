import pygame
import settings


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
