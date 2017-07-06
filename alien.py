import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class that represents an alien"""

    def __init__(self, settings, screen):
        """Initialize the alien, and set its starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings

        # Load the alien image and set a rect from it
        self.image = pygame.image.load('assets/alien.png')
        self.rect = self.image.get_rect()

        # Each alien starts at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store position as float
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True when alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Updates the alien's position over time"""
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Draw the alien at its position"""
        self.screen.blit(self.image, self.rect)
