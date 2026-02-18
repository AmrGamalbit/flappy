import pygame

class Pipe(pygame.sprite.Sprite):
    def __init__(self, y, position):
        super().__init__()
        self.pipe_image = pygame.image.load("assets/game_objects/pipe-green.png").convert_alpha()

        if position == "top":
            self.image = pygame.transform.flip(self.pipe_image, False, True)
            self.rect = self.image.get_rect(midtop=(700, y))
        else:
            self.image = self.pipe_image
            self.rect = self.image.get_rect(midtop=(700, y))

        self.scroll_speed = 10

    def scroll(self):
        self.rect.x -= self.scroll_speed

    def update(self):
        self.scroll()

        if self.rect.x <= -100:
            self.kill()
