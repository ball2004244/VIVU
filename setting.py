import pygame
from pygame.locals import *
pygame.init()

class Colors():
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    YELLOW = (186, 200, 0)
    BLUE = (0, 0, 255)
    BROWN = (83, 53, 10)
    SKYBLUE = (154,203,255)
    LIGHTBROWN = (124, 96, 62)

class FontType():
    FONT1 = pygame.font.SysFont('Dotum', 50)
    FONT2 = pygame.font.SysFont('Cambria', 30)
    FONT3 = pygame.font.SysFont('Garamond', 20)

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
    pygame.display.update()





