import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class that fires bullets from the ship"""

    def __init__(self, settings, screen, ship):
        """Create a bullet object at the ship's position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Initialize bullet rect at 0,0 before repositioning at ship
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's y-position as a float
        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        """The bullet will move to the top of the screen"""
        # Update the bullet position
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draws the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
