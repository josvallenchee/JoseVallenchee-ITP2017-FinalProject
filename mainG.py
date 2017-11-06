# Credits : www.raywenderlich.com/24252/beginning-game-programming-for-teens-with-python
#           Python.Crash.Course - Alien Invasion
#           Jude Martinez & Minaldi Louis

#importing pygame in order to activate it
import pygame

# importing all other classes
from settings import Setting
from pygame.sprite import Group
from rabbit import Bunny
from stats import GameStats
from healthbar import Health
from text import Button
from scoreboard import Scoreboard
import move as gf



# making a function to run the game
def run_game():
    # calling pygame
    pygame.init()
    setting = Setting()

    # putting the background
    screen = pygame.display.set_mode([setting.width,setting.height])
    background = pygame.transform.scale(pygame.image.load_basic('grass.bmp'),(setting.width,setting.height))
    backgroundrect = background.get_rect()
    screen.blit(background, backgroundrect)

    # loading the background music and setting a caption
    rabbit = Bunny(screen, setting)
    pygame.display.set_caption("Mouse Infestation")
    pygame.mixer.music.load('moonlight.wav')
    pygame.mixer.music.play(-1,0.0)
    pygame.mixer.music.set_volume(0.25)

    # calling the classes
    play_button = Button(setting, screen, "Play")
    Health_bar = Health(screen)

    stats = GameStats(setting)
    sb = Scoreboard(setting, screen, stats)
    bullets = Group()
    mice = Group()
    castles = Group()

    gf.create_castle(screen,setting,80,castles)

    # making a loop for the game
    while True:

        # checking the program
        gf.check_event(setting, screen, stats, play_button, sb, rabbit, mice, bullets)

        # placing the healthbar
        if stats.game_active == False:
            Health_bar.reset_health_bar()

        # summoning the mice(enemies)
        if stats.game_active:
            for mouse in mice:
                if mouse.rect.x < mouse.image.get_rect().centerx:
                    gf.create_fleet(setting, screen, mice)
                    break

            # updating the screen in order for the program to run
            rabbit.update()
            gf.update_bullet(setting,screen, stats, sb, rabbit, bullets, mice)
            gf.update_mouse(setting, Health_bar, screen, rabbit, mice, bullets,castles,stats)
        gf.update_screen(background,backgroundrect,screen,setting, sb, rabbit, stats, bullets, mice, play_button,castles,Health_bar)


run_game()