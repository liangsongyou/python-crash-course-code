import pygame
from os import sys
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    """Detect and respond to different events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
def update_screen(ai_settings, screen, ship, bullets):
    """Update surfaces and  filp to the new screen."""
    # redraw the screen and draw surfaces
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # update to most recently visible screen
    pygame.display.flip()

def check_keydown_events(event,ai_settings, screen, ship, bullets):
    """Check the keydown event for any action."""
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    
def check_keyup_events(event, ship):
    """Check the keyup event for any action."""
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False         

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions
    bullets.update()
    # Get rid of old bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.right >= 1400:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet and it to the bullets group."""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)        
        bullets.add(new_bullet)
