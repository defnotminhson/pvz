import pygame
from typing import Tuple

RGBA = Tuple[int, int, int, int]

class MapService:
    def __init__(self,screen):
        self.tileSizeX = 50
        self.tileSizeY = 50
        self.map_x = 0
        self.map_y = 0
        self.screen = screen
        self.tiles = []

    def setPosition(self, x: int, y: int):
        self.map_x = x
        self.map_y = y
    
    def setSize(self, x: int, y: int):
        self.tileSizeX = x
        self.tileSizeY = y

    def createGrid(self, cols: int, rows: int, offset: int, color: RGBA):
        self.tiles.clear()

        for row in range(rows):
            for col in range(cols):
                tile_x = self.map_x + col * (self.tileSizeX + offset)
                tile_y = self.map_y + row * (self.tileSizeY + offset)

                rect = pygame.Rect(
                    tile_x,
                    tile_y,
                    self.tileSizeX,
                    self.tileSizeY
                )

                tile_surface = pygame.Surface(
                    (self.tileSizeX, self.tileSizeY),
                    pygame.SRCALPHA
                )
                tile_surface.fill(color)  # RGBA (alpha = 120)

                self.tiles.append({
                    "rect": rect,
                    "surface": tile_surface
                })

                
        return self.tiles

    def drawGrid(self):
        for tile in self.tiles:
            self.screen.blit(tile["surface"], tile["rect"].topleft)
            rect = tile["rect"]
            if rect.collidepoint(pygame.mouse.get_pos()):
                    glow_surface = pygame.Surface(rect.size, pygame.SRCALPHA)
                    glow_surface.fill((255, 255, 255, 60))  # white glow, low alpha
                    self.screen.blit(glow_surface, rect.topleft)


    def destroy(self):
        self.tiles.clear()
