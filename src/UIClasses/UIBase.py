import pygame


class UIBase():
    def __init__(self, Pos, Size, ImagePath, AnchorPoint=(0.5,0.5), zIndex=1):
        self.PosX, self.PosY = Pos
        self.SizeX, self.SizeY = Size
        self.AnchorX, self.AnchorY = AnchorPoint
        self.Image = pygame.image.load(ImagePath)
        self.zIndex = zIndex
        self.events = {
            "MouseEnter": [],
            "MouseLeave": [],
            "MouseButton1Up": [],
            "MouseButton1Down": [],
        }

    def refresh(self, Width, Height):
        scaledImg = pygame.transform.scale(self.Image, (Width*self.SizeX, Height*self.SizeY))
        scaledPos = (Width*(self.PosX - self.AnchorX*self.SizeX), Height*(self.PosY- self.AnchorY*self.SizeY))

        return scaledImg, scaledPos
    
    def IsMouseIn(self, MousePositon):
        MouseX, MouseY = MousePositon

        print(MouseX, MouseY)

        pass