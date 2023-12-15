class Settings():
    """ A class to store all settings for Alien Invasion """
    def __init__(self):
        """ Initialize the game´s settings """
            # Screen settings
        self.screenWidth = 1200
        self.screenHeight = 700
        # self.bgColor = (230, 230, 230)
        self.bgColor = (19, 19, 19)
        self.setCaption = "Alien Invasion"
        
            # Ship settings
        self.shipSpeed = 1.5
        
            # Bullet settings
        self.bulletWidth = 3
        self.bulletHeight = 15
        self.bulletSpeed = 1.0
        self.bulletColor = (60, 60, 60)