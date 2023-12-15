import pygame
import sys

class Rocket:
    
    def __init__(self):
        
        pygame.init()
        
        self.screen = pygame.display.set_mode((500, 400))        
        pygame.display.set_caption("rocket_exercise")
        
        self.screenRect = self.screen.get_rect()    # se obtiene rectángulo de la pantalla
        
        self.image = pygame.image.load("./images/smile.bmp")  # se carga imagen
        self.rect = self.image.get_rect()   # se obtiene rectángulo en el que se encuentra la imagen
        
        self.rect.midbottom = self.screenRect.midbottom # se posiciona imagen igualando rectángulo del screen con el de la imagen
        
        self.derecha = False
    
    def updateMovRight(self):
        if self.derecha and self.rect.right < self.screenRect.right:
            self.rect.x += 1
                
    def runRocket(self):
        while True:
            self.screen.fill((0, 191, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()                
                elif event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_RIGHT:
                        self.derecha = True
                        
                    elif event.key == pygame.K_LEFT:
                        self.rect.x -= 1
                    elif event.key == pygame.K_UP:
                        self.rect.y -= 1
                    elif event.key == pygame.K_DOWN:
                        self.rect.y += 1
                    elif event.key == pygame.K_ESCAPE:
                        sys.exit()
                
                elif event.type == pygame.K_UP:
                    if event.key == pygame.K_RIGHT:
                        self.derecha = False
                
            
            self.updateMovRight()        
            self.screen.blit(self.image, self.rect)            
            
            
            pygame.display.flip()
            

if __name__ == '__main__':
    rocket = Rocket()
    rocket.runRocket()