import pygame
from pygame.sprite import Group

from Settings import Settings
from ship import Ship
from Aliens import Alien
import functions as gf

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Example Game")

    ship = Ship(game_settings, screen)
    bullets = Group()
    alien = Alien(game_settings, screen)

    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(game_settings, screen, ship, alien, bullets,)

# test game
run_game()