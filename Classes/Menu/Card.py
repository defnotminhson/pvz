import pygame, Global
from Classes import Database
from Utils.Game.Highlight import highlight
from Classes.Menu.Components.TextLabel import TextLabel

class Card(pygame.sprite.Sprite):
    def __init__(self, position, order: int):
        super().__init__()
        self.position = position
        self.size = pygame.Vector2(150,140)
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)
        self.baseImage = pygame.transform.scale(
            pygame.image.load("Assets/Menu/Card.png").convert_alpha(),
            self.size
        )
        self.rect = self.image.get_rect()
        self.rect.center = position

        self.hitbox = pygame.Rect(0, 0, self.size.x - 50, self.size.y - 30)
        self.hitbox.center = position
        self.price = None
        self.allyName = None
        self.order = order
        self.clicked = False

        self.previewImage = pygame.Surface(self.size, pygame.SRCALPHA)
        self.textColor = (0, 0, 0)
        self.priceText = TextLabel(
            str(self.price), 
            self.position + pygame.Vector2(0,35), 
            18, 
            self.textColor, 
            "Assets/Fonts/Rimouski.OTF", 
            True
            )
        

    def updateInfo(self):
        if self.order > -1 and self.order < len(Global.currentAlly):
            name = Global.currentAlly[self.order]
            self.allyName = name
            self.price = Database.data[name]["price"]
            self.previewImage = pygame.Surface(self.size, pygame.SRCALPHA)
            self.previewImage = pygame.transform.scale(
                pygame.image.load(Database.data[name]["preview"]).convert_alpha()
                , self.size - pygame.Vector2(70,55)
            )
            self.previewRect = self.previewImage.get_rect()
            self.priceText.setText(str(self.price))

    def handleClick(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()

            if self.hitbox.collidepoint(mouse_pos):
                self.clicked = True
                if Global.inGameSun >= Database.data[self.allyName]["price"]:
                    Global.inGameCurrentSelected = self.allyName

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.clicked = False
                
    def update(self):
        self.image = self.baseImage.copy()
        self.image.blit(self.previewImage, (35,20))
        Global.screen.blit(self.priceText.image, self.priceText.rect)

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
            
            