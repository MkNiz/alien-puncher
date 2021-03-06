class GameStats():
    """Maintains statistics for the game"""

    def __init__(self, settings):
        """Initialize"""
        self.settings = settings
        self.reset_stats()

        self.high_score = 0

        # Game starts in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Sets statistics to default values"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
