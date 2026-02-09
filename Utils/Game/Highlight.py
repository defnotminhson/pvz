import pygame

def highlight(rect, screen, color):
    glow_surface = pygame.Surface(rect.size, pygame.SRCALPHA)
    glow_surface.fill(color)
    screen.blit(glow_surface, rect.topleft)