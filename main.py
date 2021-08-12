# Import modules
from theme import ThemeLevelOne
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


# Main function
while True:
    # quit
    for event in pygame.event.get():
        if event.type == QUIT:
            # shutil.rmtree use to delete folders
            shutil.rmtree('__pycache__')
            shutil.rmtree('enemy/__pycache__')

            pygame.quit()
            sys.exit()

    Screen.fill(Colors.WHITE)

    # draw
    theme_lv1.draw()
    player.draw()
    status_bar.draw()
    creep_lv1.draw()

    # update
    player.update()
    theme_lv1.update()
    creep_lv1.update()

    fps_clock()
    update_screen()
