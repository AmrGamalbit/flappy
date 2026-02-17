import pygame
from pygame.locals import K_UP


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            "assets/game_objects/yellowbird-midflap.png"
        ).convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 2)
        self.rect = self.image.get_rect(center=(100, 400))
        self.velocity = 0
        self.gravity = 0.5
        self.space_pressed = False

    def flap(self):
        self.velocity = -8

    def handle_bounds(self, player_rect, screen_rect):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_rect.bottom:
            self.game_over()


    def game_over(self):
        self.kill()

    def update(self, screen_rect):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.space_pressed:
            self.flap()
            self.space_pressed = True
        elif not keys[pygame.K_SPACE]:
            self.space_pressed = False

        self.velocity += self.gravity
        self.rect.y += self.velocity

        self.handle_bounds(self.rect ,screen_rect)
