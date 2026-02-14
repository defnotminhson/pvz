import pygame, Global
from Utils.Core.Loader import loadModule

class AllyService:
    def __init__(self, screen):
        self.allyGroup = pygame.sprite.LayeredUpdates()
        self.bulletGroup = pygame.sprite.Group()
        self.screen = screen

    def spawnAlly(self, name: str, pos: pygame.Vector2, lane):
        newAlly = loadModule(f"Classes/Allies/{name}.py")(
            screen=self.screen,
            position=pos,
            lane=lane
        )
        self.allyGroup.add(newAlly, layer=newAlly.lane)
        return newAlly

    def handleClick(self, event, tilesGroup):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            
            for tile in tilesGroup:
                if tile.rect.collidepoint(mouse_pos) and tile.allyPlanted == "nil":
                    tile.allyPlanted = self.spawnAlly("SunFlower", tile.rect.center, tile.lane)
                    tile.Taken = True
    
    def update(self):
        self.bulletGroup.update()
        self.allyGroup.draw(self.screen)
        self.allyGroup.update()

        # for sprite in self.allyGroup:
        #     pygame.draw.rect(self.screen, (255, 0, 0), sprite.hitbox, 2)