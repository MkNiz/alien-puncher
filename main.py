import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group

import game_logic as gl

def run_game():
    # Initialization of game and screen
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height)
    )
    pygame.display.set_caption("Alien Puncher")

    # Create the player ship
    ship = Ship(game_settings, screen)

    # Store bullets in a group
    bullets = Group()

    # Store aliens in a group
    aliens = Group()

    # Create a fleet of aliens
    gl.create_fleet(game_settings, screen, ship, aliens)

    # Primary loop
    while True:
        gl.check_events(game_settings, screen, ship, bullets)
        ship.update()
        gl.update_bullets(game_settings, screen, ship, aliens, bullets)
        gl.update_aliens(game_settings, ship, aliens)

        gl.update(game_settings, screen, ship, aliens, bullets)

run_game()
