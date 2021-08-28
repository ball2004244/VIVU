from setting import Screen, Colors
import pygame
from pygame.locals import *
pygame.init()

# This is hilly theme


class ThemeLevelOne():
    def __init__(self):
        '''INITIALIZE VISUAL IMAGES'''
        # Theme Surface
        self.surface = pygame.Surface((1366, 768), pygame.SRCALPHA)
        self.pos_x = 0
        self.pos_y = 0
        self.speed = 7  # Transition speed

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

        for self.bush_x in range(-100, 1124, 100):
            for self.bush_y in range(450, 530, 120):
                self.bush_rad = 70
                pygame.draw.circle(self.surface, Colors.GREEN,
                                   (self.bush_x, self.bush_y), self.bush_rad)

        # Clouds
            self.cloud_x = 900
            self.cloud_y = 100
            self.cloud_rad = 35
            pygame.draw.circle(self.surface, Colors.WHITE,
                               (self.cloud_x, self.cloud_y), self.cloud_rad)
            pygame.draw.circle(self.surface, Colors.WHITE, (self.cloud_x -
                               self.cloud_rad, self.cloud_y), self.cloud_rad * 3 // 4)
            pygame.draw.circle(self.surface, Colors.WHITE, (self.cloud_x +
                               self.cloud_rad, self.cloud_y), self.cloud_rad * 3 // 4)

    def draw(self):

        Screen.blit(self.surface, (self.pos_x, self.pos_y))
        pass

    def update(self, player):
        # Moving background while main character move near border

        # DEBUGGING
        # print(player.theme_extend_left)
        key_pressed = pygame.key.get_pressed()
        if player.theme_extend_left and key_pressed[pygame.K_a]:
            self.pos_x += self.speed
        if player.theme_extend_right and key_pressed[pygame.K_d]:
            self.pos_x -= self.speed
        pass
