import pygame
from star import *

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Solar System")

star = Star("Gold")

run = True

while run:
    screen.fill((0, 0, 0))
    pygame.draw.circle(
        screen,
        pygame.Color(star.color),
        (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
        50 * star.mass,
    )
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
