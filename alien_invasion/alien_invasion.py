import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
    """Initialize game and create screen objects."""
    # set the background color
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Make the play button
    play_button = Button(ai_settings, screen, "Click to Play")
    # Create an instance to store game statistics and create a Scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
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
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets, stats, sb)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, stats, screen, ship, aliens, bullets, play_button, sb)


if __name__ == '__main__':
    run_game()
