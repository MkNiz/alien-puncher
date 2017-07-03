import pygame

from settings import Settings
from ship import Ship

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

    # Primary loop
    while True:
        gl.check_events(ship)
        ship.update()
        gl.update(game_settings, screen, ship)

run_game()
