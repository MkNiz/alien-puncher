import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class that fires bullets from the ship"""

    def __init__(self, settings, screen, ship):
        """Create a bullet object at the ship's position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Load bullet image and rect
        self.image = pygame.image.load('assets/fist.png')
        if settings.bullet_side == "right":
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()

        # Send bullet rect to the ship
        if settings.bullet_side == "left":
            self.rect.centerx = ship.rect.left
        else:
            self.rect.centerx = ship.rect.right
        self.rect.top = ship.rect.top

        # Store the bullet's y-position as a float
        self.y = float(self.rect.y)

        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        """The bullet will move to the top of the screen"""
        # Update the bullet position
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draws the bullet to the screen"""
        self.screen.blit(self.image, self.rect)
