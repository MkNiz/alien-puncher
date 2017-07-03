import pygame

class Ship():
    """Main character ship of the game"""

    def __init__(self, screen):
        """Initialize the ship; set its start position"""
        self.screen = screen

        # Load the ship's image and get its bounding box
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # New ships start at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draws the ship at its current location"""
        self.screen.blit(self.image, self.rect)
