import pygame
from pygame.sprite import Sprite

# the class of the bullet
class Bullet(Sprite):
    # the funtion of the bullet
    def __init__(self, setting, rabbit, screen):
        super(Bullet, self).__init__()
        self.screen = screen

        # calling the settings of the bullet
        self.rect = pygame.Rect(0, 0, setting.bullet_width, setting.bullet_height)
        # determining the position of the bullet
        self.rect.x = rabbit.rect.centerx
        self.rect.y = rabbit.rect.centery

        # calling the color and speed of the bullet
        self.x = float(self.rect.x)
        self.color = setting.bullet_color
        self.speed = setting.bullet_speed

    # updating the speed and location of the bullet
    def update(self):
        self.x += self.speed
        self.rect.x = self.x

    #drawing the bullet
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)