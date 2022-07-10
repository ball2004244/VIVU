from setting import Screen, Colors
from theme.mechanism import object_move
import pygame
from pygame.locals import *
pygame.init()


class Orge():  # name of lv1 Boss
    def __init__(self):
        self.speed = 7
        self.pos_x = 500
        self.pos_y = 300
        # Appearance

        '''VARIABLE FOR MECHANISM'''
        self.moving_speed = 10
        pass

    def draw(self):
        def head():
            self.head_x = self.pos_x
            self.head_y = self.pos_y
            self.head_width = 70
            self.head_height = self.head_width

            self.head = pygame.Surface(
                (self.head_width, self.head_height), pygame.SRCALPHA)
            self.head.fill(Colors.SEA_FOAM_GREEN)
            self.head_rect = self.head.get_rect(center=(
                self.head_x + self.head_width // 2, self.head_y + self.head_height // 2))
            pass

        def ear():
            self.ear_width = self.head_width * 15 // 100
            self.ear_height = self.head_height * 45 // 100
            self.ear_x = self.head_x - self.ear_width
            self.ear_y = self.head_y + self.head_width // 5

            self.ear = pygame.Surface(
                (self.ear_width, self.ear_height), pygame.SRCALPHA)
            self.ear.fill(Colors.RED)
            self.lear_rect = self.ear.get_rect(
                topleft=(self.ear_x, self.ear_y))
            self.rear_rect = self.ear.get_rect(
                topleft=(self.ear_x + self.head_width + self.ear_width, self.ear_y))
            pass

        def neck():
            self.neck_x = self.head_x + self.head_width // 5
            self.neck_y = self.head_y + self.head_height
            self.neck_width = self.head_width * 3 // 5
            self.neck_height = self.head_height * 7 // 100

            self.neck = pygame.Surface(
                (self.neck_width, self.neck_height), pygame.SRCALPHA)
            self.neck.fill(Colors.SEA_FOAM_GREEN)
            self.neck_rect = self.neck.get_rect(center=(
                self.neck_x + self.neck_width // 2, self.neck_y + self.neck_height // 2))

            pass

        def mid_body():
            self.shoulder = self.head_width * 40 // 100
            self.mid_body_x = self.head_x - self.shoulder
            self.mid_body_y = self.neck_y + self.neck_height
            self.mid_body_width = self.head_width + 2 * self.shoulder
            self.mid_body_height = self.head_height * 140 // 100

            self.mid_body = pygame.Surface(
                (self.mid_body_width, self.mid_body_height), pygame.SRCALPHA)
            self.mid_body.fill(Colors.SEA_FOAM_GREEN)
            self.mid_body_rect = self.mid_body.get_rect(center=(
                self.mid_body_x + self.mid_body_width // 2, self.mid_body_y + self.mid_body_height // 2))
            pass

        def low_body():
            self.low_body_x = self.head_x - self.shoulder - self.shoulder // 2 
            self.low_body_y = self.mid_body_y + self.mid_body_height
            self.low_body_width = self.head_width + 2 * self.shoulder + self.shoulder
            self.low_body_height = self.mid_body_height * 105 // 100

            self.low_body = pygame.Surface(
                (self.low_body_width, self.low_body_height), pygame.SRCALPHA)
            self.low_body.fill(Colors.SEA_FOAM_GREEN)
            self.low_body_rect = self.low_body.get_rect(center=(
                self.low_body_x + self.low_body_width // 2, self.low_body_y + self.low_body_height // 2))
            pass

        def arm():
            self.arm_width = self.mid_body_width * 20 // 100
            self.arm_height = self.mid_body_height * 70 // 100
            self.arm_x = self.mid_body_x
            self.arm_y = self.mid_body_y

            self.arm = pygame.Surface(
                (self.arm_width, self.arm_height), pygame.SRCALPHA)
            self.arm.fill(Colors.RED)
            self.larm_rect = self.arm.get_rect(
                topright=(self.arm_x, self.arm_y))
            self.rarm_rect = self.arm.get_rect(
                topleft=(self.arm_x + self.mid_body_width, self.arm_y))
            pass

        def leg():
            self.leg_width = self.arm_width * 135 // 100
            self.leg_height = self.arm_height * 110 // 100
            self.leg_x = self.low_body_x + self.low_body_width // 2
            self.leg_y = self.low_body_y + self.low_body_height

            self.leg = pygame.Surface(
                (self.leg_width, self.leg_height), pygame.SRCALPHA)
            self.leg.fill(Colors.RED)
            self.lleg_rect = self.leg.get_rect(
                topright=(self.leg_x - self.low_body_width // 15, self.leg_y))
            self.rleg_rect = self.leg.get_rect(
                topleft=(self.leg_x + self.low_body_width // 15, self.leg_y))
            pass

        # Call back body parts
        head()
        ear()
        neck()
        mid_body()
        low_body()
        arm()
        leg()

        # Draw to Screen
        Screen.blit(self.head, self.head_rect)

        Screen.blit(self.ear, self.lear_rect)
        Screen.blit(self.ear, self.rear_rect)

        Screen.blit(self.neck, self.neck_rect)

        Screen.blit(self.mid_body, self.mid_body_rect)
        Screen.blit(self.low_body, self.low_body_rect)

        Screen.blit(self.arm, self.larm_rect)
        Screen.blit(self.arm, self.rarm_rect)

        Screen.blit(self.leg, self.lleg_rect)
        Screen.blit(self.leg, self.rleg_rect)
        pass

    def update(self, player, theme):
        object_move(player, theme, self)
        pass
