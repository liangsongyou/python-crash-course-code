import pygame

class Rocket():
    """Represent the rocket object."""

    def __init__(self, ro_settings, screen):
        """Initialize the ship and set it's starting position."""
        self.screen = screen
        self.ro_settings = ro_settings
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False
        # load the ship image and get its rectangle.
        self.image = pygame.image.load('./ship.bmp')
        self.img_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new ship at the bottom center of the screen
        self.img_rect.centery = self.screen_rect.centery
        self.img_rect.centerx = self.screen_rect.centerx
        # store a decimal value for the ship's center
        self.centerx = float(self.img_rect.centerx)
        self.centery = float(self.img_rect.centery)

    def blitme(self):
        """Draw the ship at it's current location."""
        self.screen.blit(self.image,self.img_rect)

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.img_rect.right < self.screen_rect.right:
            self.centerx += self.ro_settings.rocket_speed_factor
        if self.moving_left and self.img_rect.left > 0:
            self.centerx-= self.ro_settings.rocket_speed_factor
        if self.moving_up and self.img_rect.top > 0:
            self.centery -= self.ro_settings.rocket_speed_factor
        if self.moving_down and self.img_rect.bottom < self.screen_rect.bottom:
            self.centery += self.ro_settings.rocket_speed_factor
        # update img_rect from self.center
        self.img_rect.centery = self.centery        
        self.img_rect.centerx = self.centerx