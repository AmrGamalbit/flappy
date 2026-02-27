import random
import sys

import pygame

from bird import Bird
from pipe import Pipe
from button import RestartButton

pygame.init()

SCREEN_HEIGHT = 936
SCREEN_WIDTH = 864
FPS = 60

ground_scroll = 0
scroll_speed = 5
pipe_frequency = 1500
pipe_spawn = pygame.USEREVENT + 1
pygame.time.set_timer(pipe_spawn, pipe_frequency)
game_over = False
score = 0
previous_score = 0
bird_pass = False

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("FlapPy")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 36)

bg = pygame.image.load("assets/bg.png")
ground = pygame.image.load("assets/ground.png")

flappy_bird = Bird(100, SCREEN_HEIGHT // 2)

bird_group = pygame.sprite.GroupSingle()
pipe_group = pygame.sprite.Group()

bird_group.add(flappy_bird)
button = RestartButton(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
button_group = pygame.sprite.GroupSingle()
button_group.add(button)

def draw_score():
    score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(SCREEN_WIDTH // 2, 100))
    screen.blit(score_surface, score_rect)

def reset_game():
    pipe_group.empty()
    flappy_bird.rect.x = 100
    flappy_bird.rect.y = SCREEN_HEIGHT // 2
    flappy_bird.flying = False
    score = 0
    return score

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and not flappy_bird.flying
            and not game_over
        ):
            bird_group.sprite.flying = True
        if event.type == pipe_spawn and not game_over and flappy_bird.flying:
            pipe_height = random.randint(-100, 100)
            btm_pipe = Pipe(SCREEN_WIDTH, int(SCREEN_HEIGHT // 2 + pipe_height), -1)
            top_pipe = Pipe(SCREEN_WIDTH, int(SCREEN_HEIGHT // 2 + pipe_height), 1)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)

    screen.blit(bg, (0, 0))
    screen.blit(ground, (ground_scroll, 768))

    if (
        pygame.sprite.groupcollide(pipe_group, bird_group, False, False)
        or flappy_bird.rect.top < 0
    ):
        game_over = True

    if flappy_bird.rect.bottom > 768:
        game_over = True
        flappy_bird.flying = False
    pipe_group.draw(screen)
    if not game_over:
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0
        pipe_group.update()
        bird_group.draw(screen)
        bird_group.update()

    if len(pipe_group) > 1:
        if (
            bird_group.sprite.rect.left > pipe_group.sprites()[0].rect.left
            and bird_group.sprite.rect.right < pipe_group.sprites()[0].rect.right
            and not bird_pass
        ):
            bird_pass = True
        if (
            bird_group.sprite.rect.left > pipe_group.sprites()[0].rect.right
            and bird_pass
        ):
            previous_score = score
            score += 1
            bird_pass = False
    if game_over:
        button_group.draw(screen)
        pos = pygame.mouse.get_pos()
        if button_group.sprite.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                game_over = False
                score = reset_game()
    draw_score()
    pygame.display.update()
    clock.tick(FPS)
