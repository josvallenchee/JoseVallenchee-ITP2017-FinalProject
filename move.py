#the import of other classes, the system and ramdom
import sys
from enemy import Enemy
import pygame
from time import sleep
from bullet import Bullet
from castle import Castle
import random

# the function for the main character to move up and down
def check_keydown(event, rabbit, setting, screen, bullets):
    if event.key == pygame.K_w:
        rabbit.moving_up = True
    elif event.key == pygame.K_s:
        rabbit.moving_down = True
    if event.key == pygame.K_q:
        sys.exit()
    # spawning bullets by pressing spacebar
    elif event.key == pygame.K_SPACE:
       fire_bullet(rabbit, setting, screen, bullets)

def fire_bullet(rabbit, setting, screen, bullets):
    if len(bullets) < setting.bullets_allowed:
        new_bullet = Bullet(setting, rabbit, screen)
        bullets.add(new_bullet)

def update_bullet(setting, screen, stats, sb, rabbit, bullets, mice):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_mouse_collisions(setting, screen, stats, sb, rabbit, mice, bullets)

# making the collisions  between the bullet and mouse(enemy)
def check_bullet_mouse_collisions(setting, screen, stats, sb, rabbit, mice, bullets):
    collision = pygame.sprite.groupcollide(bullets, mice, True, True)

    if collision:
        for mice in collision.values():
            # inserting the score each collisions made between bullet and mouse
            stats.score += setting.mouse_points * len(mice)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(mice) == 0:
        bullets.empty()
        setting.increase_speed()
        create_fleet(setting, screen, mice)

# updating the mouse
def update_mouse(setting, healthbar, screen, rabbit, mice, bullets, castles,stats):
    mice.update()
    check_mice_bottom(setting, healthbar, screen, rabbit, mice, bullets,stats)

    if pygame.sprite.groupcollide(castles, mice, False, False):
        rabbit_hit(setting, healthbar, screen, rabbit, mice, bullets,stats)

# checking the moving of the main character
def check_keyup(event, rabbit):
    if event.key == pygame.K_w:
        rabbit.moving_up = False
    elif event.key == pygame.K_s:
        rabbit.moving_down = False

def check_event(setting, screen, stats, play_button, sb, rabbit, mice, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, rabbit, setting, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup(event, rabbit)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(setting, screen, stats, play_button, sb, rabbit, mice, bullets, mouse_x, mouse_y)

# checking the play button and the resetting of the score
def check_play_button(setting,screen, stats, play_button, sb, rabbit, mice, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        setting.initialize_dynamic_settings()

        pygame.mouse.set_visible(False)

        stats.reset_stats()
        sb.prep_score()
        sb.show_score()

        stats.game_active = True

        mice.empty()
        bullets.empty()
        rabbit.center_rabbit()

# updating the screen with the background and the castle
def update_screen(background,backgroundrect,screen, setting, sb, rabbit, stats, bullets, mice, play_button,castle,Healthbar):

    screen.fill(setting.color)
    screen.blit(background, backgroundrect)
    Healthbar.draw_health_bar()
    castle.draw(screen)

    rabbit.blitme()
    mice.draw(screen)
    for bullet in bullets:
        bullet.draw_bullet()

    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()

# creating the random fleet of the mouse
def create_fleet(setting,screen,mice):
    mouse = Enemy(setting,screen)
    screen_rect = screen.get_rect()
    mice_lo_height = random.randint(0,screen_rect.bottom)
    mouse.rect.x = screen_rect.width
    mouse.rect.y = mice_lo_height
    mouse.add(mice)

# creating the function when the healthbar goes 0
def rabbit_hit(setting, healthbar, screen, rabbit, mice, bullets,stats):
    if healthbar.get_health_bar() > 0:
        healthbar.min_health_bar()
        mice.empty()
        bullets.empty()
        create_fleet(setting, screen, mice)
        rabbit.center_rabbit()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_mice_bottom(setting, healthbar, screen, rabbit, mice, bullets,stats):
    screen_rect = screen.get_rect()
    for mouse in mice.sprites():
        if mouse.rect.bottom > screen_rect.bottom:
            rabbit_hit(setting, healthbar, screen, rabbit, mice, bullets,stats)
            break

# checking the high score
def check_high_score(stats, sb):
    if stats.score>stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

# creating the bunch of castles and their size
def create_castle(screen,settings,location,castles):
    for i in range(6):
        castle = Castle(screen,settings)
        castle.rect.x = location
        castle.rect.y = castle.rect.height*i
        castles.add(castle)