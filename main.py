import sys

import pygame
from pygame.locals import *

from bird import Bird
from utils import load_scaled

pygame.init()
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption("FlapPy")
clock = pygame.time.Clock()

SKY_SURFACE = load_scaled(
    pygame.image.load("assets/game_objects/background-day.png").convert(), (600, 650)
)
sky_rect = SKY_SURFACE.get_rect()
BASE_SURFACE = load_scaled(
    pygame.image.load("assets/game_objects/base.png").convert(), (600, 150)
)

bird = pygame.sprite.GroupSingle()
bird.add(Bird())
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(SKY_SURFACE, (0, 0))
    screen.blit(BASE_SURFACE, (0, 650))
    bird.draw(screen)
    bird.update(sky_rect)
    pygame.display.update()
    clock.tick(60)
