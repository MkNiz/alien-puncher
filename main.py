import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
    # Initialization of game and screen
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height)
    )
    pygame.display.set_caption("Alien Puncher")

    # Create the player ship
    ship = Ship(screen)

    # Primary loop
    while True:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Set a custom background color
        screen.fill(game_settings.bg_color)

        # Draw the player's ship at its current position
        ship.blitme()

        # Set display to make the most recently drawn screen visible
        pygame.display.flip()

run_game()
