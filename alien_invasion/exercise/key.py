from os import sys
import pygame

def main():
    """Main loop of the window."""
    pygame.init()
    scr_size = (1386,700)
    screen = pygame.display.set_mode(scr_size)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print('{}'.format(event.key))
        pygame.display.flip()

main()