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

    def spawnAlly(self, name: str, pos: pygame.Vector2, lane):
        newAlly = Allies[name](
            screen=self.screen,
            position=pos,
            bulletGroup=self.bulletGroup,
            lane=lane
        )
        self.allyGroup.add(newAlly)
        return newAlly

    def handleClick(self, event, tilesGroup):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            
            for tile in tilesGroup:
                if tile.rect.collidepoint(mouse_pos) and tile.allyPlanted == "nil":
                    tile.allyPlanted = self.spawnAlly("PeaShooter", tile.rect.center, tile.lane)
                    tile.Taken = True
    
    def update(self):
        self.bulletGroup.update()
        self.allyGroup.draw(self.screen)
        self.allyGroup.update()

        # for sprite in self.allyGroup:
        #     pygame.draw.rect(self.screen, (255, 0, 0), sprite.hitbox, 2)