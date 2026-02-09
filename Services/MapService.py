import pygame
from typing import Tuple

RGBA = Tuple[int, int, int, int]

class Tile(pygame.sprite.Sprite):
    def __init__(self, width: int, height: int, posX: int, posY: int, color: RGBA):
        super().__init__()
        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = [posX, posY]
        self.clicked = False

class MapService:
    def __init__(self,screen):
        self.tileSizeX = 50
        self.tileSizeY = 50
        self.mapPosX = 0
        self.mapPosY = 0
        self.screen = screen
        self.tilesGroup = pygame.sprite.Group()
        self.tileGlow = True

    def handleClick(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            for tile in self.tilesGroup:
                if tile.rect.collidepoint(mouse_pos):
                    tile.clicked = True
                    break
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_pos = event.pos
            for tile in self.tilesGroup:
                if tile.rect.collidepoint(mouse_pos):
                    tile.clicked = False
                    break

    def createGrid(self, cols: int, rows: int, offset: int, color: RGBA):
        #self.tilesGroup.clear()
        for row in range(rows):
            for col in range(cols):
                tile_x = self.mapPosX + col * (self.tileSizeX + offset)
                tile_y = self.mapPosY + row * (self.tileSizeY + offset)
                
                tile = Tile(self.tileSizeX, self.tileSizeY, tile_x, tile_y, color)
                self.tilesGroup.add(tile)
                
        return self.tilesGroup

    def drawGrid(self):            
        self.tilesGroup.draw(self.screen)
        #glow
        for tile in self.tilesGroup:
            mouse_pos = pygame.mouse.get_pos()
            # hover glow
            if tile.rect.collidepoint(mouse_pos) and self.tileGlow:
                glow_surface = pygame.Surface(tile.rect.size, pygame.SRCALPHA)
                glow_surface.fill((255, 255, 255, 60))
                self.screen.blit(glow_surface, tile.rect.topleft)

            if tile.clicked:
                click_overlay = pygame.Surface(tile.rect.size, pygame.SRCALPHA)
                click_overlay.fill((0, 255, 0, 80))
                self.screen.blit(click_overlay, tile.rect.topleft)


    def destroyGrid(self):
        #self.tilesGroup.clear()
        pass
