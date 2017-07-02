import sys
import pygame

def run_game():
    # Initialization of game and screen
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Alien Puncher")
    # Primary loop
    while True:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Set a custom background color
        screen.fill((255, 0, 0))
        # Set display to make the most recently drawn screen visible
        pygame.display.flip()

run_game()
