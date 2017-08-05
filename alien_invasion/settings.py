class Settings():
    """A class to store all settings for alien invasioon."""


    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1376
        self.screen_height = 700
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 100, 0, 0
        self.bullets_allowed = 3