from setting import Screen, Colors
import pygame
from pygame.locals import *
pygame.init()

# This is hilly theme


class ThemeLevelOne():
    def __init__(self):
        '''INITIALIZE VISUAL IMAGES'''
        # Theme Surface
        self.pos_x = 0
        self.pos_y = 0
        self.surface_width = 5000
        self.surface_height = 768
        self.speed = 7  # Transition speed

        self.surface = pygame.Surface(
            (self.surface_width, self.surface_height), pygame.SRCALPHA)
        pass

        # Land
        self.land_x = self.pos_x
        self.land_y = self.pos_y + 500
        self.land_width = self.surface_width
        self.land_height = self.surface_height - self.land_y
        pygame.draw.rect(self.surface, Colors.BROWN, (self.land_x,
                         self.land_y, self.land_width, self.land_height))
        pass

        # Sky
        self.sky_x = self.pos_x
        self.sky_y = self.pos_y
        self.sky_width = self.land_width
        self.sky_height = 768 - self.land_height
        pygame.draw.rect(self.surface, Colors.SKYBLUE, (self.sky_x,
                         self.sky_y, self.sky_width, self.sky_height))
        pass

        # Mountains
        def mountain(start, end, distance):
            for left_foot_x in range(start, end, distance):
                left_foot_y = self.land_y

                right_foot_x = left_foot_x + 400
                right_foot_y = left_foot_y

                peak_x = (left_foot_x + right_foot_x) // 2
                peak_y = left_foot_y - 300
                pygame.draw.polygon(self.surface, (78, 111, 142), ([left_foot_x, left_foot_y], [
                                    right_foot_x, right_foot_y], [peak_x, peak_y]))
            pass

        # Bushses
        def bush(start, end, distance):
            for bush_x in range(start, end, distance):
                for bush_y in range(450, 530, 120): #450, 530, 120 are start, end, distance vertically
                    bush_rad = 70
                    pygame.draw.circle(self.surface, Colors.GREEN, (bush_x, bush_y), bush_rad)
            pass

        # Clouds
        def cloud(start, end, distance):
            cloud_y = 100
            cloud_rad = 35

            for cloud_x in range(start, end, distance):
                cloud_y = 100
                cloud_rad = 35

                pygame.draw.circle(self.surface, Colors.WHITE,
                                (cloud_x, cloud_y), cloud_rad)
                pygame.draw.circle(self.surface, Colors.WHITE, (cloud_x - cloud_rad, cloud_y), cloud_rad * 3 // 4)
                pygame.draw.circle(self.surface, Colors.WHITE, (cloud_x + cloud_rad, cloud_y), cloud_rad * 3 // 4)
            pass
        


        # Drawing shapes
        mountain(self.pos_x, self.surface_width, 250)
        bush(self.pos_x, self.surface_width, 100)
        cloud(self.pos_x, self.surface_width, 300)
        pass

    def draw(self):

        Screen.blit(self.surface, (self.pos_x, self.pos_y))
        pass

    def update(self, player):
        # Moving background while main character move near border

        # DEBUGGING
        # print(player.theme_extend_left)
        key_pressed = pygame.key.get_pressed()
        if player.theme_extend_left and key_pressed[pygame.K_a] and player.pos_x > self.pos_x + 100:
            self.pos_x += self.speed
        if player.theme_extend_right and key_pressed[pygame.K_d] and player.pos_x + player.surface_width < self.pos_x + self.surface_width - 100:
            self.pos_x -= self.speed
        pass
