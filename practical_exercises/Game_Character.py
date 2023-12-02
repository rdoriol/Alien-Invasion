import pygame

# 12-2. Game Character

class Draw:
    def __init__(self, blueS):
            # Se obtiene configuración de pantalla y posición de la clase BlueSky
        self.screen = blueS.screen
        self.screenRect = blueS.screen.get_rect()
        
            # Se carga imagen y posición deseada
        self.image = pygame.image.load("./images/smile.bmp")
        self.rect = self.image.get_rect()   # atributo con posición inicial de la imagen
        
            # Se inicia imagen con la posición deseada
        self.rect.center = self.screenRect.center
        
         # pruebas propias
        # self.rect.x = 100
        # self.rect.y = 100        
        # self.screenRect.x = self.rect.x
        # self.screenRect.y = self.rect.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)