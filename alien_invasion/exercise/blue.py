from os import sys
import pygame
from character import Character

def main():
    """The main function to be run on start."""
    pygame.init()
    screen = pygame.display.set_mode((900,500))
    pygame.display.set_caption("Character")
    ch = Character(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((83,29,67))
        ch.blit_character()
        pygame.display.flip()

main()