import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Control the aliens appearing on the screen."""
    
    def __init__(self, ai_settings, screen):
        """Initialize the alien object to default position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # load the alien image and it's rectangle
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # start each new alien at the top of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height 

        self.x = float(self.rect.x)

    def blitme(self):
        """Display the alien on screen."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return true if alien is at the edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right."""
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x