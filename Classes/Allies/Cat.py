import pygame

class Cat(pygame.sprite.Sprite):
    def __init__(self, pictureLink):
        super().__init__()
        self.image = pygame.image.load(pictureLink)
        self.rect = self.image.get_rect()
    def update(self):
        pass
        # glow_surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        # glow_surface.fill((255, 255, 255, 60))
        # self.screen.blit(glow_surface, self.rect.topleft)