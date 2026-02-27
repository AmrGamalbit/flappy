import pygame

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        super().__init__()
        self.image = pygame.image.load("assets/pipe.png")
        self.rect = self.image.get_rect()
        self.pipe_gap = 150

        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = (x, y - self.pipe_gap // 2)
        else:
            self.rect.topleft = (x, y + self.pipe_gap // 2)

    def update(self):
        self.rect.x -= 5
        if self.rect.x < -100:
            self.kill()
