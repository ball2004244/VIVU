# Import modules
from theme import DefaultTheme
from characters import Player
from setting import fps_clock, update_screen, Screen, colors
import pygame
import sys
from pygame.locals import *
pygame.init()


# Initialize variable for Main function
player = Player()
default_theme = DefaultTheme()
# Main function
while True:
    # quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    Screen.fill(colors.WHITE)

    # draw
    default_theme.draw()
    player.draw()


    # update
    fps_clock()
    update_screen()
