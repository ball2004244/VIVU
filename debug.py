# Import modules
from boss.boss_lv1 import Orge
from theme.theme_0_town import ThemeLevelZero
from theme.mechanism import Map
from main_character import Player, StatusBar
from setting import fps_clock, update_screen, Screen, Colors
import pygame
import sys
import shutil
from pygame.locals import *
pygame.init()


# Initialize variable for Main function
player = Player()
status_bar = StatusBar()
minimap = Map()
lobby = ThemeLevelZero()
boss_1 = Orge()
# Main function
while True:
    # draw
    Screen.fill(Colors.WHITE)

    lobby.draw()
    minimap.draw(lobby)
    boss_1.draw()
    player.draw()


    # update
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # shutil.rmtree use to delete folders
            shutil.rmtree('__pycache__')
            shutil.rmtree('boss/__pycache__')
            shutil.rmtree('theme/__pycache__')

            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                minimap.toggle()
            

    lobby.update(player)
    player.update(status_bar)
    boss_1.update(player, lobby)

    fps_clock()
    update_screen()
