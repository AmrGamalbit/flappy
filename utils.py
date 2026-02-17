import pygame

def load_scaled(path, size:tuple):
    return pygame.transform.scale(path, size)
