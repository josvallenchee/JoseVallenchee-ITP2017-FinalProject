import pygame
from pygame.sprite import Sprite

# the class of the enemy(mouse)
class Enemy (Sprite):
    # the function of the enemy
    def __init__(self, setting, screen):
        super(Enemy, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.setting = setting

        # putting the mouse image
        self.image = pygame.image.load_basic("badguy.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.screen_rect.width

        self.x = float(self.rect.x)

    # to blit the enemy's image
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    # updating the position and the speed of the enemy
    def update(self):
        self.x -= self.setting.mouse_speed
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True