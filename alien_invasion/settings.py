class Settings():
    """A class to store all settings for alien invasioon."""


    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1376
        self.screen_height = 700
        self.bg_color = (230,230,230)
        # Ship settings
        self.ship_limit = 3        
        self.ship_speed_factor = 1.5
        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = 200, 0, 0
        self.bullets_allowed = 3
        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet direction of -1 represents left and 1 rerepresetns right
        self.fleet_direction = 1