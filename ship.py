import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Main character ship of the game"""

    def __init__(self, settings, screen):
        """Initialize the ship; set its start position"""
        super(Ship, self).__init__()
        self.screen = screen
        self.settings = settings

        # Load the ship's image and get its bounding box
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # New ships start at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Ship's center is stored as a float
        self.center = float(self.rect.centerx)

        # Whether the ship is moving in a given horizontal direction
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on a movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor
        # Rect object is updated through self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draws the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Centers the ship on the screen"""
        self.center = self.screen_rect.centerx
