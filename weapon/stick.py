import pygame
from pygame.locals import *
from setting import Colors, Screen
from main_character import Player
pygame.init()


class StickLevelOne():
    def __init__(self):
        # Surface
        self.surface_width = 14
        self.surface_height = self.surface_width * 8
        self.surface = pygame.Surface(
            (self.surface_width, self.surface_height), pygame.SRCALPHA)

        # surface position
        self.pos_x = 300
        self.pos_y = 50

        def appearance():
            # stick body
            self.x = 0
            self.y = 0
            self.width = self.surface_width
            self.height = self.surface_height
            pygame.draw.rect(self.surface, Colors.BLACK,
                             (self.x, self.y, self.width, self.height))

            # stick head
            self.head_width = self.width
            self.head_height = self.height // 10

            self.head_x = self.x
            self.head_up_y = self.y
            self.head_down_y = self.head_height * 9 + 1

            pygame.draw.rect(self.surface, Colors.WHITE,
                             (self.head_x, self.head_up_y, self.head_width, self.head_height))

            pygame.draw.rect(self.surface, Colors.WHITE,
                             (self.head_x, self.head_down_y, self.head_width, self.head_height))

            pass

        # execute functions
        appearance()

        '''VARIABLE FOR MECHANISM'''
        self.hit_enemy = False
        self.damage = 5
        self.buy_price = 30 #dollar
        self.sell_price = 5 #dollar
        pass

    def draw(self):
        Screen.blit(self.surface, (self.pos_x, self.pos_y))
        pass

    def update(self):
        def give_damage():
            if self.hit_enemy:

                #enemy.health -= self.damage
                self.hit_enemy = False
            else:
                get_mouse_click()

        def get_mouse_click():
            if Player.give_damage_left or Player.give_damage_right:
                return True
            return False

        def hit_enemy():
            ''' if get_mouse_click():
                #Check self.x, y overlap enemy.x, y
                if (self.x >= enemy.x) and (self.x + self.width <= enemy.x + enemy.width) and (self.y >= enemy.y) and (self.y + self.height <= enemy.y + enemy.height):
                    return True
            return False
            '''
            #UNFINISHED
        pass
