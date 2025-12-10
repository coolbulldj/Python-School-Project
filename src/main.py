import pygame
from display import display as displayObj
from UIClasses.UIBase import UIBase as UIBaseObj
Display = displayObj()
TestFrame = UIBaseObj((0,0), (0.5, 0.5), "src\Assets\UIAssets\WhiteSquare.png")
Display.add_element(TestFrame)



a = {"a", "b", 1} 

a.add()

print(a)

MAXFPS = 60

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            pass
            #print(event.type)
    Display.refresh()

    pygame.display.flip()

print("QUIT")