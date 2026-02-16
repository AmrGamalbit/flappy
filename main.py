import pygame
from pygame.locals import *
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("FlapPy")
clock = pygame.time.Clock()

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/game_objects/yellowbird-midflap.png")
        self.image = pygame.transform.scale(self.image, (100, 300))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 400)

bird = pygame.sprite.GroupSingle()
bird.add(Bird())
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    bird.draw(screen)
    pygame.display.update()
    clock.tick(60)
