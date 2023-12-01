import sys
import pygame
from settings import Settings

class AlienInvasion:
    """ Overall class to manage game assets and behavior"""
    
    def __init__(self):
        """ Initialize the game, and create game resources """
        pygame.init()
            # Instance Settings (module settings.py)
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screenWidth, self.settings.screenHeight))
        pygame.display.set_caption(self.settings.setCaption)
        
    def runGame(self):
        """ Start the main loop for the game """
        while True:
                # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit
            
                # Redraw the screen during each pass though the loop
            self.screen.fill(self.settings.bgColor)
                # Make the most recently draw screen visible
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.runGame()