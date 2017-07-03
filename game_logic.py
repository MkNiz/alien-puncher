import sys
import pygame

def check_events():
    """Responds to pygame events i.e. key presses"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update(game_settings, screen, ship):
    """Updates the screen with current data"""
    # Set a custom background color
    screen.fill(game_settings.bg_color)

    # Draw the player's ship at its current position
    ship.blitme()

    # Flip the screen
    pygame.display.flip()
