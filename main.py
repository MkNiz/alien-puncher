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

    # Primary loop
    while True:
        gl.check_events(game_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        # Remove bullets when they hit the top of the screen
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
                
        gl.update(game_settings, screen, ship, bullets)

run_game()
