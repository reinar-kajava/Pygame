import pygame

from Settings import Settings
from ship import Ship
import functions as gf

def run_game():
    # init game and create display object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Example Game")

    # create ship
    ship = Ship(game_settings, screen)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(game_settings, screen, ship)
# test game
run_game()