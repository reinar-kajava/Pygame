import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
from Stats import Stats
"""Keybinds"""

def check_keydown_events(event, game_settings, screen, ship, bullets):
    """Check key down events"""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)
    if event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """Check key up events"""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(game_settings, screen, ship, bullets, stats, playbutton):
    """Check keyboard and mouse events"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            checkplaybutton(game_settings, stats, playbutton, mouse_x, mouse_y)
def checkplaybutton(game_settings, Stats, playbutton, mouse_x, mouse_y,):
    if playbutton.rect.collidepoint(mouse_x, mouse_y,):
        game_settings.init_dynamics
        Stats.game_active = True

"""Screen"""

def update_screen(game_settings, screen, stats, sb, ship, aliens, bullets, playbutton):

    """Update image on screen and draw new screen"""

    # add screen background
    screen.fill(game_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # add ship to screen
    ship.blitme()
    # add alien to screen
    aliens.draw(screen)

    sb.draw_score()
    # if the game is not running then the play button will be drawn
    if stats.game_active == False:
        playbutton.drawbutton()
    # display the last screen
    pygame.display.flip()



"""Bullets"""
def update_bullets(game_settings, screen, stats, sb, ship, aliens, bullets):
    """Update bullets position and  remove old bullets"""

    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(game_settings, screen, stats, sb, ship, aliens, bullets)
"""Checks for collisions between aliens and bullets"""
def check_bullet_alien_collisions(game_settings, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        stats.score += game_settings.alien_points
        sb.prepare_score()
    # Remove bullets and create new fleet
    if len(aliens) == 0:
        bullets.empty()
        game_settings.increase_speed()
        create_fleet(game_settings, screen, ship, aliens)
    """Defines what happens when all the bullets are fired"""
def fire_bullet(game_settings, screen, ship, bullets):
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)



""""Aliens section"""
def get_number_aliens_x(game_settings, alien_width):
    """Compute number of aliens in the row"""

    available_space_x = game_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(game_settings, ship_height, alien_height):
    """Define nuber of rows on screen"""
    available_space_y = game_settings.screen_height - 3 * alien_height - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(game_settings, screen, aliens, alien_number, row_number):
    # create alien and put it into a row
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(game_settings, screen, ship, aliens):
    """Create alines fleet"""

    # Create aliens and compute how much aliens can exists at the row
    alien = Alien(game_settings, screen)
    number_aliens_x = get_number_aliens_x(game_settings, alien.rect.width)
    number_rows = get_number_rows(game_settings, ship.rect.height, alien.rect.height)
    # create first row
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(game_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(game_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_settings, aliens)
            break

def change_fleet_direction(game_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1

def update_aliens(game_settings, stats, screen, ship, aliens, bullets):
    """Update aliens position"""
    check_fleet_edges(game_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(game_settings, stats, screen, ship, aliens, bullets)
    check_aliensbottom(game_settings, stats, screen, ship, aliens, bullets)
    # Check if aliens are at the bottom

# Restarts the game
def ship_hit(game_settings, stats, screen, ship, aliens, bullets):
    if stats.ships_left == 3:
        stats.ships_left = stats.ships_left - 1

        aliens.empty()
        bullets.empty()
        # Center ship

        ship.restartship()
        # pauses the game

        create_fleet(game_settings, screen, ship, aliens)
        sleep(2)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

"""Checks if the aliens have reached the bottom of the screen and if so restarts the game"""
def check_aliensbottom(game_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(game_settings, stats, screen, ship, aliens, bullets)
            break