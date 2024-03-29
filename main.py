# Import modules
from weapon.stick import StickLevelOne
from theme.theme_1_hill import ThemeLevelOne
from theme.theme_0_town import ThemeLevelZero
from theme.mechanism import Map
from shop import ShopThemeOne
from main_character import Player, StatusBar, Inventory
from setting import fps_clock, update_screen, Screen, Colors
from enemy.creep import CreepLevelOne
from boss.boss_lv1 import Orge
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
inventory = Inventory()
minimap = Map()
lobby = ThemeLevelZero()

# Main function
while True:
    # draw
    Screen.fill(Colors.WHITE)

    lobby.draw()
    #theme_lv1.draw()
    player.draw()
    status_bar.draw()
    #creep_lv1.draw()
    shop_lv1.draw(player, stick_lv1)
    inventory.draw(player, stick_lv1, status_bar)
    minimap.draw(lobby)


    # update
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # shutil.rmtree use to delete folders
            shutil.rmtree('__pycache__')
            shutil.rmtree('theme/__pycache__')
            shutil.rmtree('enemy/__pycache__')
            shutil.rmtree('weapon/__pycache__')
            shutil.rmtree('boss/__pycache__')

            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                shop_lv1.toggle()  
            elif event.key == pygame.K_i:
                inventory.toggle()
            elif event.key == pygame.K_m:
                minimap.toggle()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            shop_lv1.trading(player, stick_lv1)

    lobby.update(player)
    #theme_lv1.update(player, theme_lv1)
    player.update(status_bar)
    #creep_lv1.update()
    status_bar.update()
    shop_lv1.update()
    inventory.update()



    fps_clock()
    update_screen()
