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
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """Turns the score into a rendered image"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Score is displayed at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 16
        self.score_rect.top = 16

    def prep_high_score(self):
        """Turns the high score into a rendered image"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # High Score is displayed top center of screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turns the level into a rendered image"""
        self.level_image = self.font.render(("Level " + str(self.stats.level)), True, self.text_color, self.settings.bg_color)

        # Position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 8

    def display_score(self):
        """Draws the score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
