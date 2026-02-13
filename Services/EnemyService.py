import pygame, Global
from Classes.Enemies.Test import Test
from Classes.Enemies.Police import Police

Enemies = {
    "Test": Test,
    "Police": Police
}

class EnemyService:
    def __init__(self, screen):
        self.enemyGroup = pygame.sprite.LayeredUpdates()
        self.screen = screen

    def spawnEnemy(self, name: str, pos: pygame.Vector2, lane: int):
        newEnemy = Enemies[name](
            screen=self.screen,
            position=pos,
            lane=lane,
        )
        self.enemyGroup.add(newEnemy, layer=newEnemy.lane)
        Global.mapService.lanes[lane].add(newEnemy, layer=newEnemy.lane)

    def handleClick(self, event, tilesGroup):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            mouse_pos = event.pos
            
            for tile in tilesGroup:
                if tile.rect.collidepoint(mouse_pos):
                    self.spawnEnemy("Police", tile.rect.center, tile.lane)
    
    def update(self):
        self.enemyGroup.draw(self.screen)
        self.enemyGroup.update()

        # for sprite in self.enemyGroup:
        #     pygame.draw.rect(self.screen, (255, 0, 0), sprite.hitbox, 2)