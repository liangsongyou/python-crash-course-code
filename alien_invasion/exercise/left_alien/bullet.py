import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Describe and manage the bullet to be shot by the ship."""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = screen
        # Create a bullet rect at 0,0 and set it's position to ship's position
        self.rect = pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centery = ship.img_rect.centery
        self.rect.left = ship.img_rect.right
        # Store the bullet's position as decimal value
        self.x = float(self.rect.x)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor    

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet
        self.x += self.speed_factor
        # update the rect position
        self.rect.x = self.x
        

    def draw_bullet(self):
        """Draw the bullet on screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
        