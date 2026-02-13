import pygame
from Classes.Enemies.Test import Test
from Classes.Enemies.Police import Police

Enemies = {
    "Test": Test,
    "Police": Police
}

class EnemyService:
    def __init__(self, screen):
        self.enemyGroup = pygame.sprite.Group()
        self.screen = screen
        self.lanes = {
            0: pygame.sprite.Group(),
            1: pygame.sprite.Group(),
            2: pygame.sprite.Group(),
            3: pygame.sprite.Group(),
            4: pygame.sprite.Group(),
            5: pygame.sprite.Group(),
            6: pygame.sprite.Group(),
            7: pygame.sprite.Group(),
            8: pygame.sprite.Group(),
            9: pygame.sprite.Group(),
        }

    def spawnEnemy(self, name: str, pos: pygame.Vector2, lane: int):
        newEnemy = Enemies[name](
            screen=self.screen,
            position=pos,
            lane=lane,
        )
        self.enemyGroup.add(newEnemy)
        self.lanes[lane].add(newEnemy)

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