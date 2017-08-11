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
        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 18
        self.bullet_color = 200, 0, 0
        self.bullets_allowed = 3
        # Alien settings
        self.fleet_drop_speed = 10
        # How quickly the ship speeds up
        self.speedup_scale = 1.1
        # How quikcly the alien points values Increase
        self.score_scale = 1.5
        # Score for an shooting an alien
        self.alien_points = 10
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 5
        self.alien_speed_factor = 1
        # fleet direction of -1 represents left and 1 rerepresetns right
        self.fleet_direction = 1

    def increas_speed(self):
        """Increase speed of all elements by speedup_scale. and alsoo score"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
