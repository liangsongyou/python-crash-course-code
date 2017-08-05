import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from ship import Ship

def run_game():
    """Initialize game and create screen objects."""
    # set the background color
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets
    bullets = Group()

# Start the main game loop
    while True:
        # wathch for keyboard and mouse events.        
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

    
if __name__ == '__main__':
    run_game()