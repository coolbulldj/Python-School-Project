import pygame
from display import display as displayObj
from UIClasses.UIBase import UIBase as UIBaseObj
Display = displayObj()
TestFrame = UIBaseObj((0,0), (0.5, 0.5), r"src\Assets\UIAssets\WhiteSquare.png")

UIElements = []

MAXFPS = 60

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_x, click_y = pygame.mouse.get_pos()
            display_x, display_y = Display.get_size()
            scaled_x, scaled_y = click_x/display_x, click_y/display_y
            
        else:
            pass
            #print(event.type)
    Display.refresh()

    pygame.display.flip()

print("QUIT")