import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ A class to represent a single alien in the fleet. """
    
    def __init__(self, aiGame):
        """ Initialized the alien and set the initing position. """
        super().__init__()
        self.screen = aiGame.screen
        
            # Load the image and set its rect attribute        
        self.image = pygame.image.load("./images/alien.png")
        self.rect = self.image.get_rect()
        
            # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
            # Store the alien´s exact horizontal position.
        self.x = float(self.rect.x)