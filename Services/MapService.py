import pygame
from typing import Tuple
from Utils.Game.Highlight import highlight

RGBA = Tuple[int, int, int, int]

class Tile(pygame.sprite.Sprite):
    def __init__(self, width: int, height: int, posX: int, posY: int, color: RGBA):
        super().__init__()
        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = [posX, posY]
        self.clicked = False
        self.allyPlanted = None
        self.lane = 0

class MapService:
    def __init__(self, screen):
        self.tileSize = (50, 50)
        self.mapPos = (0, 0)
        self.screen = screen
        self.tilesGroup = pygame.sprite.Group()
        self.tileGlow = True
        self.lanes = {}
        for i in range(0,10):
            self.lanes[i] = pygame.sprite.LayeredUpdates()

    def handleClick(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            for tile in self.tilesGroup:
                if tile.rect.collidepoint(mouse_pos):
                    tile.clicked = True
                    break
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            for tile in self.tilesGroup:
                if tile.clicked:
                    tile.clicked = False
                    break

    def createGrid(self, cols: int, rows: int, offset: int, color: RGBA):
        #self.tilesGroup.clear()
        for row in range(rows):
            for col in range(cols):
                mapPosX, mapPosY = self.mapPos
                tileSizeX, tileSizeY = self.tileSize
                tile_x = mapPosX + col * (tileSizeX + offset)
                tile_y = mapPosY + row * (tileSizeY + offset)
                
                tile = Tile(tileSizeX, tileSizeY, tile_x, tile_y, color)
                self.tilesGroup.add(tile)
                tile.lane = row
                
        return self.tilesGroup

    def update(self):            
        self.tilesGroup.draw(self.screen)
        #glow
        for tile in self.tilesGroup:
            mouse_pos = pygame.mouse.get_pos()
            # hover glow
            if tile.rect.collidepoint(mouse_pos) and self.tileGlow:
                highlight(tile.rect.size, tile.rect.topleft, self.screen, (150, 150, 150, 60))

            if tile.clicked:
                highlight(tile.rect.size, tile.rect.topleft, self.screen, (150, 150, 150, 80))

            if tile.allyPlanted and not tile.allyPlanted.alive:
                tile.allyPlanted = None


    def destroyGrid(self):
        #self.tilesGroup.clear()
        pass
