import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A class to manage bullets fired from the ship """
    
    def __init__(self, aiGame):
        """ Create a bullet object at the ship´s current position """
        super().__init__()
        self.screen = aiGame.screen
        self.settings = aiGame.settings
        self.color = self.settings.bulletColor
        ## self.screenRect = aiGame.screen.get_rect()
        
            # Create a bullet rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bulletWidth, self.settings.bulletHeight)
        self.rect.midtop = aiGame.ship.rect.midtop
        
            # Store the bullet´s position as a decimal value
        self.y = float(self.rect.y)
        
    def update(self):
        """ Move the bullet up the screen """
            # Update the decimal position of the bullet.
        self.y -= self.settings.bulletSpeed
            # Update the rect position
        self.rect.y = self.y
        
    def drawBullet(self):
        """ Draw the bullet to the screen """
        pygame.draw.rect(self.screen, self.color, self.rect)