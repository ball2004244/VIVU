from setting import Colors, Screen
import pygame
from pygame.locals import *
pygame.init()

# make object move while theme extend
# this is applicaple for theme if entity = theme.
def object_move(player, theme, entity): 
    key_pressed = pygame.key.get_pressed()
    if player.theme_extend_left and key_pressed[pygame.K_a] and player.pos_x > theme.pos_x + 100:
        entity.pos_x += theme.speed
    if player.theme_extend_right and key_pressed[pygame.K_d] and player.pos_x + player.surface_width < theme.pos_x + theme.surface_width - 100:
        entity.pos_x -= theme.speed

class Map():
    def __init__(self):
        self.opening = False
        pass

    def draw(self, theme):
        # Draw Surface
        ratio = 5 / 100
        self.width = int(theme.surface_width * ratio)
        self.height = int(theme.surface_height * ratio)
        self.pos_x = 1024 - self.width - 10
        self.pos_y = 10
        self.surface = pygame.transform.scale(
            theme.surface, (self.width, self.height))

        # Draw Frame
        self.frame_dense = 5
        self.frame_x = self.pos_x - self.frame_dense
        self.frame_y = self.pos_y - self.frame_dense
        self.frame_width = self.width + 2 * self.frame_dense
        self.frame_height = self.height + 2 * self.frame_dense
        self.frame = pygame.Surface((self.frame_width, self.frame_height), pygame.SRCALPHA)
        self.frame.fill(Colors.LIGHTBROWN)

        if self.opening:
            Screen.blit(self.frame, (self.frame_x, self.frame_y))
            Screen.blit(self.surface, (self.pos_x, self.pos_y))
        pass
    
    def toggle(self):
        self.opening = not self.opening
        pass
    
    def update(self):
        pass
    pass