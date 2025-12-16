from .UIBase import UIBase


class Button(UIBase):
    def __init__(self, Pos, Size, ImagePath, AnchorPoint=(0.5, 0.5), zIndex=1):
        super().__init__(Pos, Size, ImagePath, AnchorPoint, zIndex)
        self.events = {
            "MouseEnter": [],
            "MouseLeave": [],
            "MouseButton1Up": [],
            "MouseButton1Down": [],
        }

    def FireMouseButton1Up(self):
        super()._FireEvent("MouseButton1Up")

    def FireMouseButton1Down(self):
        super()._FireEvent("MouseButton1Down")

    def ConnectMouseButton1Up(self, CB):
        super()._ConnectEvent("MouseButton1Up", CB)

    def ConnectMouseButton1Down(self, CB):
        super()._ConnectEvent("MouseButton1Down", CB)