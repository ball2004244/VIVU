# Import modules
from theme_0_town import ThemeLevelZero
from main_character import Player, StatusBar, Map
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

# Main function
while True:
    # draw
    Screen.fill(Colors.WHITE)

    lobby.draw()
    player.draw()
    minimap.draw(lobby)


    # update
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # shutil.rmtree use to delete folders
            shutil.rmtree('__pycache__')
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                minimap.toggle()
            

    lobby.update(player)
    player.update(status_bar)
    fps_clock()
    update_screen()
