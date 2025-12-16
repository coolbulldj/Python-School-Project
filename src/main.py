import pygame
from display import display as displayObj
from UIClasses.UIBase import UIBase as UIBaseObj
from UIClasses.Button import Button as UIButtonObj
Display = displayObj()

TestFrame = UIBaseObj((0,0), (0.5, 0.5), r"src\Assets\UIAssets\WhiteSquare.png")
Button = UIButtonObj((0.25, 0.6), (0.25,0.25), r"src\Assets\UIAssets\WhiteSquare.png")


UIElements: list[UIBaseObj] = []

UIElements.append(TestFrame)
UIElements.append(Button)

MAXFPS = 60

running = True

def GetScaledMousePos():
    click_x, click_y = pygame.mouse.get_pos()
    display_x, display_y = Display.get_size()
    scaled_x, scaled_y = click_x/display_x, click_y/display_y

    return (scaled_x, scaled_y)

while running:
    ScaledMousePos = GetScaledMousePos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for UIElem in UIElements:
                if UIElem.IsA("Button") & UIElem.IsMouseIn(ScaledMousePos):
                    print("Detected Click")
            #print(event.type)
    #Detect Mouse Movements around UI frames
    for UIElem in UIElements:
        if UIElem.IsMouseIn(ScaledMousePos):
            if not UIElem.MouseIn:
                UIElem.MouseIn = True
                UIElem.FireMouseEnter()
            else:
                if UIElem.MouseIn:
                    UIElem.MouseIn = False
                    UIElem.FireMouseLeave()

    Display.refresh(UIElements)

    pygame.display.flip()

print("QUIT")