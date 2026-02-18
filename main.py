import sys
import random

import pygame

from bird import Bird
from pipe import Pipe

from utils import load_scaled

def create_pipe_pair():
    gap = random.randint(100, 180)
    random_height = random.randint(-90, 0)
    top_pipe = Pipe(random_height, "top")
    bottom_pipe = Pipe(random_height + gap + 320, "bottom")

    return bottom_pipe, top_pipe

pygame.init()
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption("FlapPy")
clock = pygame.time.Clock()
SPAWN_WALL = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_WALL, 1000)

SKY_SURFACE = load_scaled(
    pygame.image.load("assets/game_objects/background-day.png").convert(), (600, 650)
)
sky_rect = SKY_SURFACE.get_rect()
BASE_SURFACE = load_scaled(
    pygame.image.load("assets/game_objects/base.png").convert(), (600, 150)
)

bird = pygame.sprite.GroupSingle()
bird.add(Bird())

pipes = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SPAWN_WALL:
            x_top, x_bottom = 700, 700
            y_top = random.randint(500, 650)
            pipes.add(create_pipe_pair())

    screen.blit(SKY_SURFACE, (0, 0) )
    pipes.draw(screen)
    pipes.update()
    bird.draw(screen)
    bird.update(sky_rect)
    screen.blit(BASE_SURFACE, (0, 650))
    pygame.display.update()
    clock.tick(60)
