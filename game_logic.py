import sys
import pygame
from bullet import Bullet
from alien import Alien

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
    """Events run when keys are pressed"""
    if event.key == pygame.K_RIGHT:
        # Ship starts moving to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Ship starts moving to the left
        ship.moving_left  = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group
        fire_bullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def keyup_events(event, settings, screen, ship, bullets):
    """Events run when keys are released"""
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

def update(game_settings, screen, ship, aliens, bullets):
    """Updates the screen with current data"""
    # Set a custom background color
    screen.fill(game_settings.bg_color)

    # Redraw all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Draw the player's ship at its current position
    ship.blitme()

    # Draw aliens at their current position
    aliens.draw(screen)

    # Flip the screen
    pygame.display.flip()

def update_bullets(settings, screen, ship, aliens, bullets):
    """Update bullet positions and existence"""
    # Update position of bullets
    bullets.update()

    # Remove bullets that pass the top of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Check if bullets have hit aliens
    bullet_collision(settings, screen, ship, aliens, bullets)

def bullet_collision(settings, screen, ship, aliens, bullets):
    """Handle collision between bullets and aliens"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # Bring in a new fleet if the current one is destroyed
    if len(aliens) == 0:
        # Destroy lingering bullets, create new fleet
        bullets.empty()
        create_fleet(settings, screen, ship, aliens)

def update_aliens(settings, stats, ship, aliens, bullets):
    """Updates the positions of all aliens in the given group"""
    check_fleet_edges(settings, aliens)
    aliens.update()

    # Check for alien/ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        print("Ship has been Struck")

def get_num_aliens_x(settings, alien_width):
    """Returns the number of aliens that should be in a horizontal row"""
    space_for_x = settings.screen_width - (2 * alien_width)
    num_aliens_x = int(space_for_x / (2 * alien_width))
    return num_aliens_x

def get_num_rows(settings, ship_height, alien_height):
    """Returns the number of rows of aliens the screen will fit"""
    available_space_y = (settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(settings, screen, aliens, alien_num, row_num):
    """Creates an alien and adds it to a row"""
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + (2 * alien_width * alien_num)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + (2 * alien.rect.height * row_num)
    aliens.add(alien)

def create_fleet(settings, screen, ship, aliens):
    """Create a fleet of aliens"""
    alien = Alien(settings, screen)
    # Determine number of aliens in row based on width against screen size
    alien_width = alien.rect.width
    num_aliens_x = get_num_aliens_x(settings, alien_width)
    num_rows = get_num_rows(settings, ship.rect.height, alien.rect.height)

    # Create the first row of aliens
    for row_num in range(num_rows):
        for alien_num in range(num_aliens_x):
            create_alien(settings, screen, aliens, alien_num, row_num)

def check_fleet_edges(settings, aliens):
    """Respond when an alien reaches the edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break

def change_fleet_direction(settings, aliens):
    """Lower the fleet and change their direction"""
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1
