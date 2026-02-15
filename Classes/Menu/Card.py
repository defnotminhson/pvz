import pygame, Global
from Classes import Database
from Utils.Game.Highlight import highlight

class Card(pygame.sprite.Sprite):
    def drawText(self):
        self.priceText = self.font.render(str(self.price), True, self.textColor)
        self.textRect = self.priceText.get_rect()
        self.textRect.midbottom = (self.size.x / 2, self.size.y - 20)

    def __init__(self, position, size: pygame.Vector2, order: int):
        super().__init__()
        self.position = position
        self.size = size
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.baseImage = pygame.transform.scale(
            pygame.image.load("Assets/Menu/Card.png").convert_alpha(),
            self.size
        )
        self.rect = self.image.get_rect()
        self.rect.center = position

        self.hitbox = pygame.Rect(0, 0, size.x - 50, size.y - 30)
        self.hitbox.center = position
        self.price = None
        self.allyName = None
        self.order = order
        self.clicked = False

        self.previewImage = pygame.Surface(self.size, pygame.SRCALPHA)
        self.font = pygame.font.Font(None, 24)
        self.textColor = (0, 0, 0)
        Card.drawText(self)
        

    def updateInfo(self):
        if self.order > -1 and self.order < len(Global.currentAlly):
            name = Global.currentAlly[self.order]
            self.allyName = name
            self.price = Database.data[name]["price"]
            self.previewImage = pygame.Surface(self.size, pygame.SRCALPHA)
            self.previewImage = pygame.transform.scale(
                pygame.image.load(Database.data[name]["preview"]).convert_alpha()
                , self.size - pygame.Vector2(30,30)
            )
            self.previewRect = self.previewImage.get_rect()
            Card.drawText(self)

    def handleClick(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()

            if self.hitbox.collidepoint(mouse_pos):
                self.clicked = True
                if Global.inGameSun >= Database.data[self.allyName]["price"]:
                    print("switched")
                    Global.inGameCurrentSelected = self.allyName

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.clicked = False
                
    def update(self):
        self.image = self.baseImage.copy()
        self.image.blit(self.previewImage, (15,10))
        self.image.blit(self.priceText, self.textRect)

        mouse_pos = pygame.mouse.get_pos()
        # hover glow
        if self.hitbox.collidepoint(mouse_pos):
            highlight(
                self.size - pygame.Vector2(50,20), 
                self.rect.topleft + pygame.Vector2(25,10), 
                Global.screen, 
                (0,0,0, 50)
            )

        if self.clicked:
            highlight(
                self.size - pygame.Vector2(50,20), 
                self.rect.topleft + pygame.Vector2(25,10), 
                Global.screen, 
                (0,0,0, 15)
            )
            
            