import sys
import pygame
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(game_settings, screen, ship):
    screen.fill(game_settings.bg_color)
    ship.blitme()
    pygame.display.flip()