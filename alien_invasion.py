import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """ Overall class to manage game assets and behavior"""
    
    def __init__(self):
        """ Initialize the game, and create game resources """
        pygame.init()
            
        self.settings = Settings()                      # Instance Settings (module settings.py)        
        # self.screen = pygame.display.set_mode((self.settings.screenWidth, self.settings.screenHeight))  --> changed to full screen (lines 15, 16, 17)
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screenWidth = self.screen.get_rect().width    # Store width of the full screen
        self.settings.screenHeight = self.screen.get_rect().height  # Store height of the full screen
        pygame.display.set_caption(self.settings.setCaption)
        self.ship = Ship(self)                          # Instance Ship (module ship.py)
        self.bullets = pygame.sprite.Group()            # instance sprite group (like a list)
        self.aliens = pygame.sprite.Group()             # Instance a sprite group (like a list)
        
        self._createFleet()                             # Call to method for create a fleet of aliens
        
    def runGame(self):
        """ Start the main loop for the game """
        while True:                
            self._checkEvents()
            self.ship.updateMoving()
            self._updateBullets()
            self._updateScreen()
            
            
    def _checkEvents(self):        
        """ Respond to keypress and mouse events. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:  
                self._checkKeydownEvent(event)
                    
            elif event.type == pygame.KEYUP:
                self._checkKeyupEvent(event)    
        
    
    def _checkKeydownEvent(self, event):
        """ Respond to keydown event """
        if event.key == pygame.K_LEFT:
                self.ship.movingLeft = True                   
        elif event.key == pygame.K_RIGHT:
            self.ship.movingRight = True
        elif event.key == pygame.K_SPACE:
            self._fireBullet()              # todo--> REPASAR
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
            
    
    def _checkKeyupEvent(self, event):
        """ Respond to keyup event """
        if event.key == pygame.K_LEFT:
            self.ship.movingLeft = False
        elif event.key == pygame.K_RIGHT:
            self.ship.movingRight = False
   
    
    def _fireBullet(self):              # todo--> REPASAR
        
        if len(self.bullets) < self.settings.bulletAlowed:
            """ Create a bullet2 instance an add it to the bullets group. """
            bullet2 = Bullet(self)
            self.bullets.add(bullet2)
    
        
    def _updateBullets(self):
            # Update the bullets position.
        self.bullets.update()
            # Get ride of bullets that have disapareared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    
    def _createFleet(self):
        """ Create a fleet of aliens """                    
        alien = Alien(self)
        alienWidth = alien.rect.width
        availableSpaceX = self.settings.screenWidth - (2 * alienWidth)
        numberAlienX = availableSpaceX // (2 * alienWidth)
        
        for rowAliens in range(numberAlienX):
            self._createAlien(rowAliens)
    
    
    def _createAlien(self, rowAliens):
        """ # Make a alien """
        alien = Alien(self)
        alienWidth = alien.rect.width
        alien.x = alienWidth + 2 * alienWidth * rowAliens
        alien.rect.x = alien.x
        self.aliens.add(alien)
    
    
    def _updateScreen(self):
        """ Update the screen, and flip to the new screen. """
        self.screen.fill(self.settings.bgColor)     # background-color
        self.ship.blitme()                          # load ship image method
        
        for bullet in self.bullets.sprites():       # loop to list bullet sprites
            bullet.drawBullet()                 # todo --> REPASAR
        
        self.aliens.draw(self.screen)               # Call to draw method of sprites Group
        
            # Make the most recently draw screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.runGame()