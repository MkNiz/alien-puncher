import sys
import pygame

def check_events(ship):
    """Responds to pygame events i.e. key presses"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Ship starts moving to the right
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                # Ship starts moving to the left
                ship.moving_left  = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                # Ship stops moving to the right
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                # Ship stops moving to the left
                ship.moving_left  = False

def update(game_settings, screen, ship):
    """Updates the screen with current data"""
    # Set a custom background color
    screen.fill(game_settings.bg_color)

    # Draw the player's ship at its current position
    ship.blitme()

    # Flip the screen
    pygame.display.flip()
