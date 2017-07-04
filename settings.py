class Settings():
    """Class that stores settings for the game"""

    def __init__(self):
        """Initialize game settings"""
        # Screen
        self.screen_width  = 640
        self.screen_height = 480
        self.bg_color      = (40, 0, 0)

        # Ship
        self.ship_speed_factor = 1.5

        # Bullet
        self.bullet_speed_factor = 4.5
        self.bullet_width        = 4
        self.bullet_height       = 18
        self.bullet_color        = 60, 60, 60
