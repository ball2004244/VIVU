from setting import Screen, colors
import pygame
from pygame.locals import *
pygame.init()


class Player():
    def __init__(self):
        # Surface
        '''Delete SRCALPHA to see hitbox in black color'''
        self.surface = pygame.Surface((150, 150), SRCALPHA)

        # Body
        self.body_x = 100
        self.body_y = 100
        self.body_rad = 25
        pygame.draw.circle(self.surface, colors.RED,
                           (self.body_x, self.body_y), self.body_rad)

        # Legs
        self.leg_x = self.body_x + 4
        self.leg_y = self.body_y + 14
        self.leg_width = 13
        self.leg_height = self.leg_width
        pygame.draw.rect(self.surface, colors.BLACK, (self.leg_x,
                         self.leg_y, self.leg_width, self.leg_height))
        pygame.draw.rect(self.surface, colors.BLACK, (self.leg_x - 20,
                         self.leg_y, self.leg_width, self.leg_height))

        # Eyes
        self.eye_x = self.body_x + 10
        self.eye_y = self.body_y - 1
        self.eye_rad = 10
        self.eye_rad_inner = self.eye_rad - 6
        pygame.draw.circle(self.surface, colors.WHITE,
                           (self.eye_x - 22, self.eye_y), self.eye_rad)
        pygame.draw.circle(self.surface, colors.WHITE,
                           (self.eye_x, self.eye_y), self.eye_rad)
        pygame.draw.circle(self.surface, colors.BLACK,
                           (self.eye_x - 22, self.eye_y), self.eye_rad_inner)
        pygame.draw.circle(self.surface, colors.BLACK, (self.eye_x,
                           self.eye_y), self.eye_rad_inner)

        # Arms
        '''
        self.arm_x = self.body_x - 5
        self.arm_y = self.body_y + 2
        self.arm_rad = 7
        pygame.draw.circle(self.surface, BLACK, (self.arm_x, self.arm_y), self.arm_rad)
        pygame.draw.circle(self.surface, BLACK, (self.arm_x + 25, self.arm_y), self.arm_rad)
        '''
        pass

    def draw(self):
        self.pos_x = 1024 / 2 - 150
        self.pos_y = 768 / 2 - 150
        Screen.blit(self.surface, (self.pos_x, self.pos_y))
        pass

    def update(self):
        pass
