import pygame
import sys
# from Game_Character import Draw
import Game_Character as gc

# 12-1. Blue Sky (window pygame)
# ---------------
class BlueSky:
    def __init__(self):
        pygame.init
        
        self.screen = pygame.display.set_mode((800, 600))
        self.screen.fill((0, 191, 255))
        pygame.display.set_caption("Blue Sky Exercise")
        
        self.draw2 = gc.Draw(self)
    
    def runWindow(self):
        while True:
            self.checkEvent()
            pygame.display.flip()
            self.draw2.blitme()
    
    def checkEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit
        

test = BlueSky()
test.runWindow()