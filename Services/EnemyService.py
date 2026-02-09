import pygame
from Classes.Enemies.Test import Test

Enemies = {
    "Test": Test,
}

class EnemyService:
    def __init__(self, screen):
        self.enemyGroup = pygame.sprite.Group()
        self.screen = screen

    def spawnEnemy(self, name: str, posX: int, posY: int):
        newEnemy = Enemies[name](
            screen=self.screen,
            position=[posX, posY],
        )
        self.enemyGroup.add(newEnemy)

    def handleClick(self, event, tilesGroup):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            mouse_pos = event.pos
            
            for tile in tilesGroup:
                if tile.rect.collidepoint(mouse_pos):
                    self.spawnEnemy("Test", tile.rect.centerx, tile.rect.centery)
    
    def drawEnemy(self, dt: float):
        self.enemyGroup.draw(self.screen)
        self.enemyGroup.update(dt)