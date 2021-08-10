from setting import Screen
import pygame
from setting import colors
from pygame.locals import *
pygame.init()


class DefaultTheme():
    def __init__(self):
        # Container of this theme
        self.surface = pygame.Surface((1366, 768), SRCALPHA)

        # Land
        self.land_x = 0
        self.land_y = 500
        self.land_width = 1024
        self.land_height = 268
        pygame.draw.rect(self.surface, colors.BROWN, (self.land_x,
                         self.land_y, self.land_width, self.land_height))
        pass

        # Sky
        self.sky_x = 0
        self.sky_y = 0
        self.sky_width = self.land_width
        self.sky_height = 768 - self.land_height
        pygame.draw.rect(self.surface, colors.SKYBLUE, (self.sky_x,
                         self.sky_y, self.sky_width, self.sky_height))

    def draw(self):
        self.pos_x = 0
        self.pos_y = 0
        Screen.blit(self.surface, (self.pos_x, self.pos_y))
        pass

    def update(self):
        pass
