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

    def update(self):
        """Updates the alien's position over time"""
        self.x += self.settings.alien_speed_factor
        self.rect.x = self.x

    def blitme(self):
        """Draw the alien at its position"""
        self.screen.blit(self.image, self.rect)
