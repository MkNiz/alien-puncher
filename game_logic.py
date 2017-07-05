import sys
import pygame
from bullet import Bullet

def check_events(settings, screen, ship, bullets):
    """Responds to pygame events i.e. key presses"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            keyup_events(event, settings, screen, ship, bullets)

def keydown_events(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # Ship starts moving to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Ship starts moving to the left
        ship.moving_left  = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group
        fire_bullet(settings, screen, ship, bullets)

def keyup_events(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # Ship stops moving to the right
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # Ship stops moving to the left
        ship.moving_left  = False

def fire_bullet(settings, screen, ship, bullets):
    """Fire a bullet if there are less than the max bullets on screen"""
    if len(bullets) < settings.max_bullets:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)
        settings.flip_bullet_side()

def update(game_settings, screen, ship, bullets):
    """Updates the screen with current data"""
    # Set a custom background color
    screen.fill(game_settings.bg_color)

    # Redraw all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Draw the player's ship at its current position
    ship.blitme()

    # Flip the screen
    pygame.display.flip()

def update_bullets(bullets):
    """Update bullet positions and existence"""
    # Update position of bullets
    bullets.update()

    # Remove bullets that pass the top of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
