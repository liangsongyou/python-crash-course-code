from os import sys
import pygame

def check_events(ship):
    """Detect and respond to different events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
def update_screen(ai_settings, screen, ship):
    """Update surfaces and  filp to the new screen."""
    # redraw the screen and draw surfaces
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # update to most recently visible screen
    pygame.display.flip()

def check_keydown_events(event, ship):
    """Check the keydown event for any action."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
def check_keyup_events(event, ship):
    """Check the keyup event for any action."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False    
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
