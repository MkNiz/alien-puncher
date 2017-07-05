import pygame

from settings import Settings
from ship import Ship
from alien import Alien
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

    # Create an alien
    alien = Alien(game_settings, screen)

    # Primary loop
    while True:
        gl.check_events(game_settings, screen, ship, bullets)
        ship.update()
        gl.update_bullets(bullets)

        gl.update(game_settings, screen, ship, alien, bullets)

run_game()
