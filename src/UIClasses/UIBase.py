import pygame


class UIBase():
    def __init__(self, Pos, Size, ImagePath, AnchorPoint):
        self.PosX, self.PosY = Pos
        self.SizeX, self.SizeY = Size
        self.AnchorX, self.AnchorY = AnchorPoint or (0,0)
        self.Image = pygame.image.load(ImagePath)

    def refresh(self, Width, Height):
        scaledImg = pygame.transform.scale(self.Image, (Width*self.SizeX, Height*self.SizeY))
        scaledPos = (Width*self.PosX, Height*self.PosY)

        return scaledImg, scaledPos