import pygame
from pygame.locals import K_UP

from utils import load_scaled_2x


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_scaled_2x("assets/game_objects/yellowbird-midflap.png")
        self.rect = self.image.get_rect(center=(100, 400))
        self.velocity = 0
        self.gravity = 0.5
        self.space_pressed = False
        self.bird_frames = {
            "up": load_scaled_2x("assets/game_objects/yellowbird-upflap.png"),
            "mid": load_scaled_2x("assets/game_objects/yellowbird-midflap.png"),
            "down": load_scaled_2x("assets/game_objects/yellowbird-downflap.png"),
        }

    def get_bird_frame(self):
        if self.velocity < 0:
            self.image = self.bird_frames["up"]
            self.ract = self.image.get_rect()
        elif self.velocity > 0:
            self.image = self.bird_frames["down"]
            self.ract = self.image.get_rect()
        else:
            self.image = self.bird_frames["mid"]
            self.ract = self.image.get_rect()

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

        self.get_bird_frame()
        self.handle_bounds(self.rect, screen_rect)
