import pygame

class Ship:
    """ A class to manage the ship """
    
    def __init__(self, aiGame):
        """ Initialize the ship and set its starting position"""
        self.screen = aiGame.screen
        self.screenRect = aiGame.screen.get_rect()
        
        self.shipSettings = aiGame.settings
        
            # Load the image and get its rect
        self.image = pygame.image.load("images\ship2.bmp")
        self.rect = self.image.get_rect()
        
            # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screenRect.midbottom
        
            # Store a decimal value for the ship´s horizontal position.
        self.x = float(self.rect.x)
        
            # Movements flags
        self.movingRight = False
        self.movingLeft = False
            
    def updateMoving(self):
        """ Update the ship´s position based on the movement flag """
        if self.movingRight and self.rect.right < self.screenRect.right:
            self.x += self.shipSettings.shipSpeed
        if self.movingLeft and self.rect.left > 0:
            self.x -= self.shipSettings.shipSpeed
            
            # Update rect object from self.x
        self.rect.x = self.x
            
    def blitme(self):
        """ Draw the ship at the current location."""
        self.screen.blit(self.image, self.rect)