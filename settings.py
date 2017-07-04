class Settings():
    """Class that stores settings for the game"""

    def __init__(self):
        """Initialize game settings"""
        # Screen
        self.screen_width  = 640
        self.screen_height = 480
        self.bg_color      = (40, 0, 0)

        # Ship
        self.ship_speed_factor = 2.75

        # Bullet
        self.bullet_speed_factor = 8.5
        self.bullet_side         = "left"
        self.max_bullets         = 2

    def flip_bullet_side(self):
        """Flips the bullet side between right and left"""
        if self.bullet_side == "left":
            self.bullet_side = "right"
        else:
            self.bullet_side = "left"
