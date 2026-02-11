import pygame, Global
from Classes.Allies.Cat import Cat
from Classes.Allies.PeaShooter import PeaShooter

Allies = {
    "Cat": Cat,
    "PeaShooter": PeaShooter,
}

class AllyService:
    def __init__(self, screen):
        self.allyGroup = pygame.sprite.Group()
        self.bulletGroup = pygame.sprite.Group()
        self.screen = screen

    def spawnAlly(self, name: str, posX: int, posY: int):
        newAlly = Allies[name](
            screen=self.screen,
            position=pygame.Vector2(posX, posY),
            bulletGroup=self.bulletGroup,
        )
        self.allyGroup.add(newAlly)

    def handleClick(self, event, tilesGroup):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            
            for tile in tilesGroup:
                if tile.rect.collidepoint(mouse_pos) and not tile.Taken:
                    self.spawnAlly("PeaShooter", tile.rect.centerx, tile.rect.centery)
                    tile.Taken = True
    
    def update(self):
        self.bulletGroup.update()
        self.allyGroup.draw(self.screen)
        self.allyGroup.update()