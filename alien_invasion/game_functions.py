import pygame
from os import sys
from time import sleep
from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, stats, play_button, ship, bullets):
    """Detect and respond to different events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('highscore','w') as file:
                file.write(stats.high_score)
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, stats, play_button, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, stats, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_play_button(ai_settings, stats, play_button, mouse_x, mouse_y):
    """Start a new game when player clicks the play button."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game initial settings
        ai_settings.initialize_dynamic_settings()
        start_game(stats)

def start_game(stats):
    # Hide the mouse cursor
    pygame.mouse.set_visible(False)
    stats.game_active = True

def update_screen(ai_settings, stats, screen, ship, aliens, bullets, play_button, sb):
    """Update surfaces and  filp to the new screen."""
    # redraw the screen and draw surfaces
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # draw the aliens group
    aliens.draw(screen)
    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Draw score inforamtion
    sb.show_score()
    # Draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()
    # update to most recently visible screen
    pygame.display.flip()

def check_keydown_events(event, stats, ai_settings, screen, ship, bullets):
    """Check the keydown event for any action."""
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        start_game(stats)
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    """Check the keyup event for any action."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_bullets(ai_settings, screen, ship, aliens, bullets, stats, sb):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions
    bullets.update()
    # Get rid of old bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets, stats, sb)

def check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets, stats, sb):
    #Check for any bullets that have hit aliens
    # If so, get rid of the bullet and the alien.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # Update the score
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # Destroy existing bullets and create new fleet
        bullets.empty()
        ai_settings.increas_speed()
        create_fleet(ai_settings, screen, ship, aliens)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet and it to the bullets group."""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
    """Calculate the number of aliens that fit in row."""
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows that fit on current screen."""
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""
    # Create an alien and find the number of aliens in a row
    # Spacing between aliens is equal to width of an alien.
    alien = Alien(ai_settings, screen)
    alien.x = alien.rect.width + (2 * alien.rect.width) * alien_number
    alien.y = alien.rect.height + (2 * alien.rect.height) * row_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Create the fleet of aliens."""
    alien = Alien(ai_settings,screen)
    alien.width = alien.rect.width
    alien.height = alien.rect.height
    number_aliens_x = get_number_aliens_x(ai_settings, alien.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.height)
    for row_number in range(number_rows):
        # Create the first row of aliens
        for alien_number in range(0,number_aliens_x):
            # Create an alien and place it in the row
            alien = Alien(ai_settings, screen)
            create_alien(ai_settings, screen,aliens, alien_number, row_number)

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Respond to ship being hit by aliens."""
    if stats.ships_left > 0:
        # Decrement ships left
        stats.ships_left -= 1
        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()
        # Create a new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # Pause
        sleep(0.5)
    else:
        pygmae.mouse.set_visible(True)
        stats.game_active = False

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Check whether the fleet has reached the bottom."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.top  >= screen_rect.bottom:
            # Treat this the same as if the ship got hit
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """Check if the fleet is an edge, and then update the positions of all aliens in fleet."""
    # Look for aliens hitting the bottom
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score >= int(stats.high_score):
        stats.high_score = stats.score
        with open('highscore','w') as file:
            file.write(str(stats.high_score))
        sb.prep_high_score()