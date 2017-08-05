import pygame

from rocket import Rocket
from settings import Settings
import game_functions as gf



def main():
    """The main function to run the game."""
    pygame.init()
    screen = pygame.display.set_mode((1376,740))
    pygame.display.set_caption("Rockets")
    ro_settings = Settings()
    rocket = Rocket(ro_settings, screen)

    while True:
        gf.check_events(rocket)
        rocket.update()        
        gf.update_screen(ro_settings,screen, rocket)

main()

