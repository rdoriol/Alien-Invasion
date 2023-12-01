import pygame

class Ship:
    """ A class to manage the ship """
    
    def __init__(self, aiGame):
        """ Initialize the ship and set its starting position"""
        self.screen = aiGame.screen
        self.screenRect = aiGame.screen.get_rect()
        
            # Load the image and get its rect
        self.image = pygame.image.load("images\ship.bmp")
        self.rect = self.image.get_rect()
        
            # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screenRect.midbottom
    
    def blitme(self):
        """ Draw the ship at the current location."""
        self.screen.blit(self.image, self.rect)