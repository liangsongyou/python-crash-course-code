import pygame

class Character():
    """The character to be displayed."""

    def __init__(self, screen):
        """Initialize the character's default postion which is middle."""
        # for local reference
        self.screen = screen
        # load the character's image
        self.image = pygame.image.load('ship.bmp')
        self.img_rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # set the middle position of screen rectangle
        self.img_rect.centerx = self.screen_rect.centerx
        self.img_rect.centery = self.screen_rect.centery

    def blit_character(self):
        """Draw the character on screen."""
        self.screen.blit(self.image, self.img_rect)
        