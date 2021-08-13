from setting import Screen, Colors
from main_character import Player
import pygame
from pygame.locals import *
pygame.init()

# This is hilly theme


class ThemeLevelOne():
    def __init__(self):
        '''INITIALIZE VISUAL IMAGES'''
        # Container of this theme
        self.surface = pygame.Surface((1366, 768), SRCALPHA)

        # Land
        self.land_x = 0
        self.land_y = 500
        self.land_width = 1024
        self.land_height = 268
        pygame.draw.rect(self.surface, Colors.BROWN, (self.land_x,
                         self.land_y, self.land_width, self.land_height))
        pass

        # Sky
        self.sky_x = 0
        self.sky_y = 0
        self.sky_width = self.land_width
        self.sky_height = 768 - self.land_height
        pygame.draw.rect(self.surface, Colors.SKYBLUE, (self.sky_x,
                         self.sky_y, self.sky_width, self.sky_height))

        # Mountains

        for self.left_foot_x in range(-100, 1124, 250):
            self.left_foot_y = self.land_y

            self.right_foot_x = self.left_foot_x + 400
            self.right_foot_y = self.left_foot_y

            self.peak_x = (self.left_foot_x + self.right_foot_x) / 2
            self.peak_y = self.left_foot_y - 300
            pygame.draw.polygon(self.surface, (78, 111, 142), ([self.left_foot_x, self.left_foot_y], [
                self.right_foot_x, self.right_foot_y], [self.peak_x, self.peak_y]))

        # Bushses

        for self.bush_x in range(-100, 1124, 80):
            for self.bush_y in range(390, 500, 30):
                self.bush_rad = 45
                pygame.draw.circle(self.surface, Colors.GREEN,
                                (self.bush_x, self.bush_y), self.bush_rad)

        '''INITIALIZE VARIABLES FOR MECHANISM'''
        #Transition 
        self.speed = 20

        #Surface's position
        self.pos_x = 0
        self.pos_y = 0

    def draw(self):

        Screen.blit(self.surface, (self.pos_x, self.pos_y))
        pass

    def update(self):
        #Moving background while main character move near border
        player = Player()

        #left
        if player.theme_extend_left == True:
            self.pos_x -= self.speed
        if player.theme_extend_right == True:
            self.pos_x += self.speed
        pass
