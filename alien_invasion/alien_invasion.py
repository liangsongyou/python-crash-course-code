import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
import game_functions as gf

def run_game():
    """Initialize game and create screen objects."""
    # set the background color
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    stats = GameStats(ai_settings)
    # Make the ship
    ship = Ship(ai_settings, screen)
    # Make an alien group
    aliens = Group()
    # Make a group to store bullets
    bullets = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

# Start the main game loop
    while True:
        # wathch for keyboard and mouse events.        
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

    
if __name__ == '__main__':
    run_game()