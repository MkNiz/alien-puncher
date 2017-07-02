import sys
import pygame

from settings import Settings

def run_game():
    # Initialization of game and screen
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height)
    )
    pygame.display.set_caption("Alien Puncher")
    # Primary loop
    while True:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Set a custom background color
        screen.fill(game_settings.bg_color)
        # Set display to make the most recently drawn screen visible
        pygame.display.flip()

run_game()
