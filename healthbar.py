import pygame

# the class of the health
class Health():
    # function of the c;ass
    def __init__(self,screen):
        self.screen = screen
        # determining the healthbar location, size and color
        self.screen_rect = self.screen.get_rect()
        self.width = self.screen_rect.width/100
        self.height = self.screen_rect.height

        self.rect = pygame.Rect(0,0, self.width,self.height)
        self.rect.center = self.screen_rect.center
        self.rect.left = self.screen_rect.left
        self.color = (0,255,222)

    # changing the healthbar's color when it is decreased
    def min_health_bar(self):
        if self.height > 0:
            self.height -= self.screen_rect.height/10
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.rect.center = self.screen_rect.center
            self.rect.left = self.screen_rect.left
            if self.height < self.screen_rect.height/2:
                self.color = (255,0,0)
            else:
                self.color = (0,255,222)

    # resetting the healthbar when healthbar = 0
    def reset_health_bar(self):
        self.height = self.screen_rect.height

    def get_health_bar(self):
        return self.height

    # drawing the healthbar
    def draw_health_bar(self):
        pygame.draw.rect(self.screen,self.color, self.rect)