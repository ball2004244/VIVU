import pygame, sys
from main_character import Player
from setting import Screen, Colors
from pygame.locals import *
from theme import ThemeLevelOne
pygame.init()

player = Player()
themelevelone = ThemeLevelOne()

class TownBackground():
    def __init__(self):
        self.pos = [0, 240, 480, 720]
        self.quantity = 6
        self.a = 1024/2 - 150
# town screen
        self.pos_x = 0
        self.pos_y = 0
        self.townScreen = pygame.Surface((1024 * 10, 768),SRCALPHA)
# land
        self.land_x = 0
        self.land_y = 500
        self.land_width = 1024
        self.land_height = 268

        pass
# Sky
        self.sky_x = 0
        self.sky_y = 0
        self.sky_width = self.land_width
        self.sky_height = 768 - self.land_height


# normal building
    # house 1
        self.house1Width = 120
        self.house1Height = 100
        self.house_x1 = 0
        self.house_y1 = self.land_y - 100
    # house 2
        self.house2Width = 120
        self.house2Height = 100
        self.house_x2 = 240
        self.house_y2 = self.land_y - 100
    # house 3
        self.house3Width = 120
        self.house3Height = 100
        self.house_x3 = 120
        self.house_y3 = self.land_y - 100
    # house 4
        self.house4Width = 120
        self.house4Height = 100
        self.house_x4 = 360
        self.house_y4 = self.land_y - 100
# special building
    # school
        self.schoolWidth = 600
        self.schoolHeight = 115
        self.school_x = 480
        self.school_y = self.land_y - 115

    def draw(self):
        Screen.blit(self.townScreen, (self.pos_x, self.pos_y))
        self.townScreen.fill(Colors.WHITE)
# land
        pygame.draw.rect(self.townScreen, Colors.BROWN,
                         (self.land_x,self.land_y, self.land_width, self.land_height))
# sky
        pygame.draw.rect(self.townScreen, Colors.SKYBLUE,
                         (self.sky_x,self.sky_y, self.sky_width, self.sky_height))
# normal buildings
        for i in range(self.quantity):
            self.house_x1 = 1080 * i
            self.house_x2 = 240 + 1080 * i
            self.house_x3 = 120 + 1080 * i
            self.house_x4 = 360 + 1080 * i

    # house 1
            pygame.draw.rect(self.townScreen, Colors.GOLD,
                                [self.house_x1, self.house_y1, self.house1Width, self.house1Height])
            pygame.draw.polygon(self.townScreen, Colors.REDDISH_BROWN,
                                ([self.house_x1, self.house_y1],
                                 [self.house_x1 + 20, self.house_y1 - 30],
                                 [self.house_x1 + self.house1Width - 20, self.house_y1 - 30],
                                 [self.house_x1 + self.house1Width, self.house_y1]))
            pygame.draw.rect(self.townScreen, Colors.SEA_FOAM_GREEN,
                            [self.house_x1 + self.house1Width / 2 - 20, self.house_y1 + self.house1Height - 50,
                            40, 50])
            pygame.draw.rect(self.townScreen, Colors.BABY_BLUE,
                            [self.house_x1 + 10, self.house_y1 + self.house1Height - 55, 20, 20])
            pygame.draw.rect(self.townScreen, Colors.BABY_BLUE,
                            [self.house_x1 + self.house1Width - 30, self.house_y1 + self.house1Height - 55, 20, 20])

    # house 2
            pygame.draw.polygon(self.townScreen, Colors.LIGHT_YELLOW,
                                ([self.house_x2, self.house_y2 - 30],
                                 [self.house_x2 + self.house2Width, self.house_y2 + 20],
                                 [self.house_x2 + self.house2Width, self.house_y2 + self.house2Height - 0.5],
                                 [self.house_x2, self.house_y2 + self.house2Height- 0.5]))
            pygame.draw.line(self.townScreen, Colors.BROWN,
                            [self.house_x2, self.house_y2 - 30],
                            [self.house_x2 + self.house2Width, self.house_y2 + 20], 10)
            pygame.draw.rect(self.townScreen, Colors.PLUM,
                             [self.house_x2 + self.house2Width / 2 + 5, self.house_y2 + self.house2Height - 50,
                              40, 50])
            pygame.draw.rect(self.townScreen, Colors.BRIGHT_BLUE,
                             [self.house_x2 + 10, self.house_y2 + self.house2Height - 55, 20, 20])

    # house 3
            pygame.draw.rect(self.townScreen, Colors.DARK_YELLOW,
                             [self.house_x3, self.house_y3, self.house3Width, self.house3Height])
            pygame.draw.line(self.townScreen, Colors.BRICK,
                             [self.house_x3, self.house_y3],
                             [self.house_x3 + self.house3Width, self.house_y3],10)
            pygame.draw.rect(self.townScreen, Colors.BLUISH_PURPLE,
                             [self.house_x3 + self.house3Width / 2 + 5, self.house_y3 + self.house3Height - 30,
                              40, 30])
            pygame.draw.circle(self.townScreen, Colors.BLUISH_PURPLE,
                               (self.house_x3 + self.house3Width / 2 + 25, self.house_y3 + self.house3Height - 30), 20)
            pygame.draw.rect(self.townScreen, Colors.SKYBLUE,
                             [self.house_x3 + 10, self.house_y3 + self.house3Height - 55, 10, 20])
            pygame.draw.rect(self.townScreen, Colors.SKYBLUE,
                             [self.house_x3 + 40, self.house_y3 + self.house3Height - 55, 10, 20])

    # House 4
            pygame.draw.rect(self.townScreen, Colors.SAND,
                             [self.house_x4, self.house_y4, self.house4Width, self.house4Height])

            pygame.draw.rect(self.townScreen, Colors.GRASSGREEN,
                             [self.house_x4 + 10, self.house_y4 + self.house4Height - 30,
                              40, 30])
            pygame.draw.circle(self.townScreen, Colors.GRASSGREEN,
                               (self.house_x4 + 5 + 25, self.house_y4 + self.house4Height - 30), 20)
            pygame.draw.rect(self.townScreen, Colors.CYAN,
                             [self.house_x4 + self.house4Width / 2 + 5, self.house_y4 + self.house4Height - 55, 10, 20])
            pygame.draw.rect(self.townScreen, Colors.CYAN,
                             [self.house_x4 + self.house4Width / 2 + 35, self.house_y4 + self.house4Height - 55, 10, 20])

            pygame.draw.rect(self.townScreen, Colors.SAND,
                             [self.house_x4, self.house_y4 - self.house4Height - 2.5, self.house4Width, self.house4Height])
            pygame.draw.rect(self.townScreen, Colors.CYAN,
                             [self.house_x4 + self.house4Width / 2 + 15, self.house_y4 - 65, 10, 20])
            pygame.draw.rect(self.townScreen, Colors.CYAN,
                             [self.house_x4 + self.house4Width / 2 + 35, self.house_y4 - 65, 10, 20])
            pygame.draw.rect(self.townScreen, Colors.CYAN,
                             [self.house_x4 + self.house4Width / 2 - 25, self.house_y4 - 65, 10, 20])
            pygame.draw.rect(self.townScreen, Colors.CYAN,
                             [self.house_x4 + self.house4Width / 2 - 45, self.house_y4 - 65, 10, 20])

            pygame.draw.line(self.townScreen, Colors.LIGHTBROWN,
                             [self.house_x4 - 0.5, self.house_y4],
                             [self.house_x4 + self.house3Width , self.house_y4], 10)
            pygame.draw.polygon(self.townScreen, Colors.BROWN,
                            ([self.house_x4 - 5, self.house_y4 - self.house4Height],
                             [self.house_x4 + self.house4Width + 5, self.house_y4 - self.house4Height],
                             [self.house_x4 + self.house4Width - 5, self.house_y4 - self.house4Height - 20],
                             [self.house_x4 + 5, self.house_y4 - self.house4Height - 20]))
# special building
    # school
        pygame.draw.rect(self.townScreen, Colors.BRICKRED,
                        [self.school_x, self.school_y, self.schoolWidth, self.schoolHeight])

        pygame.draw.polygon(self.townScreen, Colors.SEA_FOAM_GREEN,
                            ([self.school_x + self.schoolWidth/2 - 90, self.school_y - self.schoolHeight-20],
                             [self.school_x + self.schoolWidth/2 + 90, self.school_y - self.schoolHeight-20],
                             [self.school_x + self.schoolWidth/2 , self.school_y - self.schoolHeight - 55-30]))

        pygame.draw.rect(self.townScreen, Colors.BRICKRED,
                         [self.school_x + self.schoolWidth/2 - 75, self.school_y - self.schoolHeight-20,
                          self.schoolWidth/4, self.schoolHeight*2 ])
        pygame.draw.polygon(self.townScreen, Colors.SEA_FOAM_GREEN,
                            ([self.school_x, self.school_y],
                             [self.school_x + self.schoolWidth, self.school_y],
                             [self.school_x + self.schoolWidth - 10, self.school_y - 30],
                             [self.school_x + 15, self.school_y - 30]))
        pygame.draw.circle(self.townScreen, Colors.BLUEGREY,
                         [self.school_x + self.schoolWidth / 2, self.school_y + self.schoolHeight - 50],
                           self.schoolWidth/20)
        pygame.draw.rect(self.townScreen, Colors.BLUEGREY,
                         [self.school_x + self.schoolWidth/2 - 30, self.school_y + self.schoolHeight - 50,
                          self.schoolWidth/10, self.schoolHeight - 65])

        pygame.draw.rect(self.townScreen, Colors.AQUAMARINE,
                         [self.school_x + 30, self.school_y + 50, self.schoolWidth/15, self.schoolHeight-85])
        pygame.draw.rect(self.townScreen, Colors.AQUAMARINE,
                         [self.school_x + 110, self.school_y + 50, self.schoolWidth / 15, self.schoolHeight - 85])
        pygame.draw.rect(self.townScreen, Colors.AQUAMARINE,
                         [self.school_x + 190, self.school_y + 50, self.schoolWidth / 15, self.schoolHeight - 85])
        pygame.draw.rect(self.townScreen, Colors.AQUAMARINE,
                         [self.school_x + self.schoolWidth - 70, self.school_y + 50,
                          self.schoolWidth / 15, self.schoolHeight - 85])
        pygame.draw.rect(self.townScreen, Colors.AQUAMARINE,
                         [self.school_x + self.schoolWidth - 150, self.school_y + 50,
                          self.schoolWidth / 15, self.schoolHeight - 85])
        pygame.draw.rect(self.townScreen, Colors.AQUAMARINE,
                         [self.school_x + self.schoolWidth - 230, self.school_y + 50,
                          self.schoolWidth / 15, self.schoolHeight - 85])

    def update(self):

        if self.a < 0:
            self.a = 0
        if self.a + 90 > 1024:
            self.a = 1024 - 90
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_a]:
            self.a -= player.speed
        if key_pressed[pygame.K_d]:
            self.a += player.speed

        if self.a < 100 and key_pressed[pygame.K_a] and self.pos_x != 0:
            self.pos_x += themelevelone.speed
        if self.a > 926 and key_pressed[pygame.K_d]:
            self.pos_x -= themelevelone.speed

#unfinished
