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

        # Ready the score image
        self.prep_score()

    def prep_score(self):
        """Turns the score into a rendered image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Score is displayed at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 16
        self.score_rect.top = 16

    def display_score(self):
        """Draws the score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
