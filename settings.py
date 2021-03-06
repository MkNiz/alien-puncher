class Settings():
    """Class that stores settings for the game"""

    def __init__(self):
        """Initialize game settings"""
        # Screen
        self.screen_width  = 640
        self.screen_height = 480
        self.bg_color      = (100, 40, 40)

        # Ship
        self.ship_limit = 3

        # Bullet
        self.max_bullets = 2

        # Alien
        self.fleet_drop_speed = 16

        # The speed at which the game becomes faster
        self.speed_mod = 1.2
        # The modifier for point values increasing each wave
        self.score_mod = 1.5

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        """Initializes/resets settings that change over the course of the game"""
        self.ship_speed_factor = 2.75
        self.bullet_speed_factor = 8.5
        self.bullet_side = "left"
        self.alien_speed_factor = 1
        # Fleet direction; 1 = right, -1 = left
        self.fleet_direction = 1
        # Point values
        self.alien_points = 50

    def speed_up_fleets(self):
        """Increase the speed of alien fleets, and their score value"""
        self.alien_speed_factor *= self.speed_mod
        self.alien_points = int(self.alien_points * self.score_mod)

    def flip_bullet_side(self):
        """Flips the bullet side between right and left"""
        if self.bullet_side == "left":
            self.bullet_side = "right"
        else:
            self.bullet_side = "left"
