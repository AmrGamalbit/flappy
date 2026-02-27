import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = []
        for num in range(1, 4):
            img = pygame.image.load(f"assets/bird{num}.png")
            self.images.append(img)
        self.index = 0
        self.counter = 0
        self.vel = 0
        self.clicked = False
        self.flying = False
        self.image = pygame.image.load("assets/bird1.png")
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        if self.flying:
            self.vel += 0.5
            if self.vel == 8:
                self.vel = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)

        if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
            self.clicked = True
            self.vel = -10
        if pygame.mouse.get_pressed()[0] == 0 and self.clicked:
            self.clicked = False

        self.counter += 1
        flap_cooldown = 5
        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
