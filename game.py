import sys
import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Example game")

    while True():
        for event in pygame.event.get():
            if event.type == pygame.quit()
                sys.exit()