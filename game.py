
#Games author: Reinar Kajava
# Games main file that is needed to run the game.

#Nessecary imports which allow this file to use other files and classes inside of them
import pygame
from pygame.sprite import Group

from Settings import Settings
from ship import Ship
from alien import Alien
from Stats import Stats
import functions as gf
from button import Button
from Score import Score

def run_game():


    # init game and create display object


    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Example Game")

    # makes a play button

    playbutton = Button(game_settings, screen, "play" )


    # Game statistics

    stats = Stats(game_settings)

    # Scoreboard

    sb = Score(game_settings, screen, stats)


    # create ship

    ship = Ship(game_settings, screen)
    bullets = Group()

    # create alien group

    aliens = Group()
    gf.create_fleet(game_settings, screen, ship, aliens)

    while True:
        gf.check_events(game_settings, screen, ship, bullets, stats, playbutton)
        if stats.game_active == True:
            ship.update()
            gf.update_bullets(game_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(game_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(game_settings, screen, stats, sb, ship, aliens, bullets, playbutton)


# test game

run_game()
