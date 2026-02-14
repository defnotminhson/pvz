import pygame

def highlight(size, position, screen, color):
    glow_surface = pygame.Surface(size, pygame.SRCALPHA)
    glow_surface.fill(color)
    screen.blit(glow_surface, position)