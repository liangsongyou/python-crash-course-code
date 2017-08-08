class GameStats():
    """Track statistics for alien invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0
        with open('highscore','r') as file:
            self.high_score = file.read()

    def reset_stats(self):
        """Initialize statistics that can change during the game play."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
