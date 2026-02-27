import pygame

class RestartButton(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/restart.png")
        self.rect = self.image.get_rect(center=(x, y))
