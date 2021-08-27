# Import modules
from weapon.stick import StickLevelOne
from theme_1_hill import ThemeLevelOne
from shop import ShopThemeOne
from main_character import Player, StatusBar
from setting import fps_clock, update_screen, Screen, Colors
from enemy.creep import CreepLevelOne
import pygame
import sys
import shutil
from pygame.locals import *
pygame.init()


# Initialize variable for Main function
player = Player()
theme_lv1 = ThemeLevelOne()
status_bar = StatusBar()
creep_lv1 = CreepLevelOne()
stick_lv1 = StickLevelOne()
shop_lv1 = ShopThemeOne()

# Main function
while True:
    # draw
    Screen.fill(Colors.WHITE)

    theme_lv1.draw()
    player.draw()
    status_bar.draw()
    creep_lv1.draw()
    shop_lv1.draw(player, stick_lv1)

    # update
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # shutil.rmtree use to delete folders
            shutil.rmtree('__pycache__')
            shutil.rmtree('enemy/__pycache__')
            shutil.rmtree('weapon/__pycache__')

            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            shop_lv1.toggle()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            shop_lv1.trading(player, stick_lv1)

    theme_lv1.update(player)
    player.update(status_bar)
    creep_lv1.update()
    status_bar.update()
    shop_lv1.update()

    fps_clock()
    update_screen()
