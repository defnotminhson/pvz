import pygame
from Classes.Allies.Cat import Cat

Allies = {
    "Cat": Cat,
}

class AllyService:
    def __init__(self, screen):
        self.allyGroup = pygame.sprite.Group()
        self.bulletGroup = pygame.sprite.Group()
        self.screen = screen

    def spawnAlly(self, name: str, posX: int, posY: int):
        newAlly = Allies[name](
            screen=self.screen,
            position=[posX, posY],
            bulletGroup=self.bulletGroup,
        )
        self.allyGroup.add(newAlly)

    def handleClick(self, event, tilesGroup):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            
            for tile in tilesGroup:
                if tile.rect.collidepoint(mouse_pos):
                    self.spawnAlly("Cat", tile.rect.centerx, tile.rect.centery)
    
    def update(self, dt: float):
        self.bulletGroup.update(dt)
        self.allyGroup.draw(self.screen)
        self.allyGroup.update(dt)