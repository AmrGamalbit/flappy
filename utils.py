import pygame

def load_scaled(path, size:tuple):
    return pygame.transform.scale(path, size)

def load_scaled_2x(path:str):
    image_surface = pygame.image.load(path).convert_alpha()
    image_surface = pygame.transform.scale_by(image_surface, 2)
    return image_surface
