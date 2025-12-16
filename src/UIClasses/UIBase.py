import pygame


class UIBase:
    def __init__(self, Pos, Size, ImagePath, AnchorPoint=(0.5,0.5), zIndex=1):
        self.PosX, self.PosY = Pos
        self.SizeX, self.SizeY = Size
        self.AnchorX, self.AnchorY = AnchorPoint
        self.Image = pygame.image.load(ImagePath)
        self.zIndex = zIndex
        self.events = {
            "MouseEnter": [],
            "MouseLeave": [],
            #"MouseButton1Up": [],
            #"MouseButton1Down": [],
        }

    def refresh(self, Width, Height):
        scaledImg = pygame.transform.scale(self.Image, (Width*self.SizeX, Height*self.SizeY))
        scaledPos = (Width*(self.PosX - self.AnchorX*self.SizeX), Height*(self.PosY- self.AnchorY*self.SizeY))

        return scaledImg, scaledPos
    
    def IsMouseIn(self, MousePositon):
        MouseX, MouseY = MousePositon

        print(MouseX, MouseY)
    def _FireEvent(self, EventName):
        CBlist = self.events[EventName]

        if not CBlist:
            print("Failed to find Callback List for Event Name:"+EventName)
            return
        
        for cb in CBlist:
            cb()

    def _ConnectEvent(self, EventName, CB):
        CBlist = self.events[EventName]

        if not CBlist:
            print("Failed to find Callback List for Event Name:"+EventName)
            return
        
        CBlist.append(CB)

    def FireMouseEnter(self):
        self._FireEvent("MouseEnter")

    def FireMouseLeave(self):
        self._FireEvent("MouseLeave")

    #def FireMouseButton1Up(self):
    #    self._FireEvent("MouseButton1Up")

    #def FireMouseButton1Down(self):
    #    self._FireEvent("MouseButton1Down")

    #Connections

    def ConnectMouseEnter(self, CB):
        self._ConnectEvent("MouseEnter", CB)

    def ConnectMouseLeave(self, CB):
        self._ConnectEvent("MouseLeave", CB)
   
    #def ConnectMouseButton1Up(self, CB):
    #    self._ConnectEvent("MouseButton1Up", CB)

    #def ConnectMouseButton1Down(self, CB):
    #    self._ConnectEvent("MouseButton1Down", CB)



        
        