import pygame
import math
from pygame.locals import *
from setting import Colors, Screen, FontType
pygame.init()


class CreepLevelOne():
    def __init__(self):
        # Surface
        self.surface_height = 250
        self.surface_width = self.surface_height
        self.surface = pygame.Surface(
            (self.surface_width, self.surface_height), SRCALPHA)

        '''CUSTOMIZE APPEARANCE'''
        def appearance():
            # Body
            self.body_x = self.surface_width // 2
            self.body_y = self.surface_height // 2
            self.body_rad = 15
            pygame.draw.circle(self.surface, Colors.BLACK,
                               (self.body_x, self.body_y), self.body_rad)

            # Eye
            self.eye_x = self.body_x
            self.eye_y = self.body_y
            self.eye_rad = self.body_rad // 2

            self.inner_eye_x = self.eye_x
            self.inner_eye_y = self.eye_y
            self.inner_eye_rad = self.eye_rad // 4

            pygame.draw.circle(self.surface, Colors.WHITE,
                               (self.eye_x, self.eye_y), self.eye_rad)
            pygame.draw.circle(self.surface, Colors.BLACK,
                               (self.inner_eye_x, self.inner_eye_y), self.inner_eye_rad)

            def spike():
                # Spike
                # up spike
                self.spike_left_foot_x = self.body_x - self.body_rad
                self.spike_right_foot_x = self.spike_left_foot_x + self.body_rad * 2
                self.spike_foot_y = self.body_y - self.body_rad

                self.spike_peak_x = (self.spike_left_foot_x +
                                    self.spike_right_foot_x) / 2
                self.spike_peak_y = self.spike_foot_y - 3 * self.body_rad

                pygame.draw.polygon(self.surface, Colors.BLACK, ([self.spike_left_foot_x, self.spike_foot_y], [
                                    self.spike_right_foot_x, self.spike_foot_y], [self.spike_peak_x, self.spike_peak_y]))

                # down spike
                self.spike_2_left_foot_x = self.spike_left_foot_x
                self.spike_2_right_foot_x = self.spike_right_foot_x
                self.spike_2_foot_y = self.spike_foot_y + 2 * self.body_rad

                self.spike_2_peak_x = self.spike_peak_x
                self.spike_2_peak_y = self.spike_2_foot_y + 3 * self.body_rad

                pygame.draw.polygon(self.surface, Colors.BLACK, ([self.spike_2_left_foot_x, self.spike_2_foot_y], [
                                    self.spike_2_right_foot_x, self.spike_2_foot_y], [self.spike_2_peak_x, self.spike_2_peak_y]))

                # left spike 
                self.spike_3_foot_x = self.body_x - self.body_rad
                self.spike_3_up_foot_y = self.body_y - self.body_rad
                self.spike_3_down_foot_y = self.spike_3_up_foot_y + 2 * self.body_rad

                self.spike_3_peak_x = self.spike_3_foot_x - 3 * self.body_rad
                self.spike_3_peak_y = (self.spike_3_up_foot_y + self.spike_3_down_foot_y) / 2

                pygame.draw.polygon(self.surface, Colors.BLACK, ([self.spike_3_foot_x, self.spike_3_up_foot_y], [
                                    self.spike_3_foot_x, self.spike_3_down_foot_y], [self.spike_3_peak_x, self.spike_3_peak_y]))

                # right spike
                self.spike_4_foot_x = self.spike_3_foot_x + 2 * self.body_rad
                self.spike_4_up_foot_y = self.spike_3_up_foot_y
                self.spike_4_down_foot_y = self.spike_3_down_foot_y
                
                self.spike_4_peak_x = self.spike_4_foot_x + 3 * self.body_rad
                self.spike_4_peak_y = self.spike_3_peak_y

                pygame.draw.polygon(self.surface, Colors.BLACK, ([self.spike_4_foot_x, self.spike_4_up_foot_y], [
                                    self.spike_4_foot_x, self.spike_4_down_foot_y], [self.spike_4_peak_x, self.spike_4_peak_y]))       
        
            #draw spike
            spike()
                
        #running functions above
        appearance()

        '''VARIABLE FOR MECHANISM'''
        # Surface's position
        self.pos_x = 500
        self.pos_y = 100
        self.surface_rect = (self.pos_x, self.pos_y)

        # Rotation
        self.angle = 0
        self.rotated_surface = pygame.transform.rotozoom(
            self.surface, self.angle, 1)
        self.rotated_surface_rect = self.rotated_surface.get_rect(
            center=(500, 100))
        pass

    def draw(self):
        Screen.blit(self.rotated_surface, self.rotated_surface_rect)
        '''For Debugging
        Screen.blit(pygame.font.Font.render(
            FontType.FONT3, str(self.spike_left_foot_x), True, Colors.BLACK), (300, 230))
        '''
        pass

    def update(self):
        def rotate():
            self.rotated_surface = pygame.transform.rotozoom(
                self.surface, self.angle, 1)
            self.rotated_surface_rect = self.rotated_surface.get_rect(
                center=(500, 100))
            return (self.rotated_surface, self.rotated_surface_rect)

        self.angle -= 5
        self.rotated_surface, self.rotated_surface_rect = rotate()
        pass
