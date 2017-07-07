class GameStats():
    """Maintains statistics for the game"""

    def __init__(self, settings):
        """Initialize"""
        self.settings = settings
        self.reset_stats()

        # Game starts in active state
        self.game_active = True

    def reset_stats(self):
        """Sets statistics to default values"""
        self.ships_left = self.settings.ship_limit
