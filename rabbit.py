import pygame

# the class of the main character
class Bunny():
    # the function of the character
    def __init__(self, screen, setting):
        self.screen = screen
        self.moving_up = False
        self.moving_down = False
        self.setting = setting

        # putting the character's image
        self.imageBig = pygame.image.load_basic("dude2.bmp")
        self.image = pygame.transform.scale(self.imageBig,(80,80))

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # locating the character's coordination
        self.rect.centery = self.screen_rect.centery
        self.center = float(self.screen_rect.centery)
        self.rect.centery = self.center

    def center_rabbit(self):
        self.centery = self.screen_rect.centery

    # the function to blit the character
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    # updating the moving and the speed of the character
    def update(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center -= self.setting.rabbit_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.setting.rabbit_speed

        self.rect.y = self.center


