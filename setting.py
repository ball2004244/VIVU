import pygame
from pygame.locals import *
pygame.init()

# Colors
class colors():
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    YELLOW = (186, 200, 0)
    BLUE = (0, 0, 255)
    BROWN = (100, 70, 36)
    SKYBLUE = (154,203,255)

# Screen
ScreenWidth = 1024
ScreenHeight = 768
Screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption('VIVU')

def fps_clock():
    FPS = 120
    clock = pygame.time.Clock()
    clock.tick(FPS)

def update_screen():
    pygame.display.flip()


