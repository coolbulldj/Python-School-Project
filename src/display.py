import pygame

class display():
    def __init__(self):
        self._dipslay = pygame.display.set_mode((500,500))
        self.elements = {}

    def refresh(self):
        self._dipslay.fill((0,0,0))

        DisplaySizeX, DisplaySizeY = self._dipslay.get_size()

        for elem in self.elements:
            Img, Pos = elem.refresh(DisplaySizeX, DisplaySizeY)
            self._dipslay.blit(Img, Pos)

    def add_element(self, elem):
        self.elements.add