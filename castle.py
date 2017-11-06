import pygame
from pygame.sprite import Sprite

# the class of the castle
class Castle(Sprite):
    # the function of the castle
    def __init__(self,screen,setting):
        super(Castle, self).__init__()
        self.screen = screen
        self.setting = setting

        # putting the castle image
        self.image = pygame.image.load_basic('castle.bmp')

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()