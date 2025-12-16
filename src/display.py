import pygame

class display():
    def __init__(self):
        self._dipslay = pygame.display.set_mode((500,500), pygame.RESIZABLE)

    def refresh(self, UIElements):
        self._dipslay.fill((0,0,0))

        DisplaySizeX, DisplaySizeY = self._dipslay.get_size()

        for elem in UIElements:
            Img, Pos = elem.refresh(DisplaySizeX, DisplaySizeY)
            self._dipslay.blit(Img, Pos)

    def get_size(self):
        return self._dipslay.get_size()