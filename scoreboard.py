import pygame.font

class Scoreboard():
    """Displays score information"""

    def __init__(self, settings, screen, stats):
        """Initialize attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.settings = settings
        self.stats = stats

        # Font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
