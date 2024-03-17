import pygame
import settings
from game_objects import Character, Enemy
import game_functions as gf

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Escfrog Game")
    clock = pygame.time.Clock()
    character = Character()
    enemy = Enemy()
    
    isGameOn = True
    while isGameOn:
        isGameOn = gf.handle_events(character)
        gf.update_game(character, enemy)
        gf.check_collisions(character, enemy)
        # 화면 그리기 로직
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    run_game()
