import pygame
from setting import Screen, Colors
from pygame.locals import *

pygame.init()



class ThemeLevelZero():
    def __init__(self):
        self.quantity = 6

        self.theme_speed = -7
        # Town screen
        self.pos_x = 0
        self.pos_y = 0
        self.surface_width = 1024 * 6
        self.surface_height = 768
        self.surface = pygame.Surface((self.surface_width, self.surface_height), pygame.SRCALPHA)

        # Land
        self.land_x = self.pos_x
        self.land_y = 500
        self.land_width = self.surface_width
        self.land_height = self.surface_height - self.land_y
        pygame.draw.rect(self.surface, Colors.BROWN,
                         (self.land_x, self.land_y, self.land_width, self.land_height))

        # Sky
        self.sky_x = 0
        self.sky_y = 0
        self.sky_width = self.land_width
        self.sky_height = 768 - self.land_height
        pygame.draw.rect(self.surface, Colors.SKYBLUE,
                         (self.sky_x, self.sky_y, self.sky_width, self.sky_height))


        '''NORMAL BUILDINGS'''
        def house_1(x):
            self.house1Width = 120
            self.house1Height = 100
            self.house_x1 = x
            self.house_y1 = self.land_y - 100

            pygame.draw.rect(self.surface, Colors.GOLD,
                            [self.house_x1, self.house_y1, self.house1Width, self.house1Height])
            pygame.draw.polygon(self.surface, Colors.REDDISH_BROWN,
                                ([self.house_x1, self.house_y1],
                                [self.house_x1 + 20, self.house_y1 - 30],
                                [self.house_x1 + self.house1Width -
                                20, self.house_y1 - 30],
                                [self.house_x1 + self.house1Width, self.house_y1]))
            pygame.draw.rect(self.surface, Colors.SEA_FOAM_GREEN,
                            [self.house_x1 + self.house1Width // 2 - 20, self.house_y1 + self.house1Height - 50,
                            40, 50])
            pygame.draw.rect(self.surface, Colors.BABY_BLUE,
                            [self.house_x1 + 10, self.house_y1 + self.house1Height - 55, 20, 20])
            pygame.draw.rect(self.surface, Colors.BABY_BLUE,
                            [self.house_x1 + self.house1Width - 30, self.house_y1 + self.house1Height - 55, 20, 20])
        
        def house_2(x):
            self.house2Width = 120
            self.house2Height = 100
            self.house_x2 = x
            self.house_y2 = self.land_y - 100

            pygame.draw.polygon(self.surface, Colors.LIGHT_YELLOW,
                                    ([self.house_x2, self.house_y2 - 30],
                                    [self.house_x2 + self.house2Width,
                                        self.house_y2 + 20],
                                    [self.house_x2 + self.house2Width,
                                        self.house_y2 + self.house2Height - 0.5],
                                    [self.house_x2, self.house_y2 + self.house2Height - 0.5]))
            pygame.draw.line(self.surface, Colors.BROWN,
                                [self.house_x2, self.house_y2 - 30],
                                [self.house_x2 + self.house2Width, self.house_y2 + 20], 10)
            pygame.draw.rect(self.surface, Colors.PLUM,
                                [self.house_x2 + self.house2Width // 2 + 5, self.house_y2 + self.house2Height - 50,
                                40, 50])
            pygame.draw.rect(self.surface, Colors.BRIGHT_BLUE,
                                [self.house_x2 + 10, self.house_y2 + self.house2Height - 55, 20, 20])
    
        def house_3(x):
            self.house3Width = 120
            self.house3Height = 100
            self.house_x3 = x
            self.house_y3 = self.land_y - 100

            pygame.draw.rect(self.surface, Colors.DARK_YELLOW,
                                [self.house_x3, self.house_y3, self.house3Width, self.house3Height])
            pygame.draw.line(self.surface, Colors.BRICK,
                                [self.house_x3, self.house_y3],
                                [self.house_x3 + self.house3Width, self.house_y3], 10)
            pygame.draw.rect(self.surface, Colors.BLUISH_PURPLE,
                                [self.house_x3 + self.house3Width // 2 + 5, self.house_y3 + self.house3Height - 30,
                                40, 30])
            pygame.draw.circle(self.surface, Colors.BLUISH_PURPLE,
                                (self.house_x3 + self.house3Width // 2 + 25, self.house_y3 + self.house3Height - 30), 20)
            pygame.draw.rect(self.surface, Colors.SKYBLUE,
                                [self.house_x3 + 10, self.house_y3 + self.house3Height - 55, 10, 20])
            pygame.draw.rect(self.surface, Colors.SKYBLUE,
                                [self.house_x3 + 40, self.house_y3 + self.house3Height - 55, 10, 20])
    
        def house_4(x):
            self.house4Width = 120
            self.house4Height = 100
            self.house_x4 = x
            self.house_y4 = self.land_y - 100

            pygame.draw.rect(self.surface, Colors.SAND,
                                [self.house_x4, self.house_y4, self.house4Width, self.house4Height])

            pygame.draw.rect(self.surface, Colors.GRASSGREEN,
                                [self.house_x4 + 10, self.house_y4 + self.house4Height - 30,
                                40, 30])
            pygame.draw.circle(self.surface, Colors.GRASSGREEN,
                                (self.house_x4 + 5 + 25, self.house_y4 + self.house4Height - 30), 20)
            pygame.draw.rect(self.surface, Colors.CYAN,
                                [self.house_x4 + self.house4Width // 2 + 5, self.house_y4 + self.house4Height - 55, 10, 20])
            pygame.draw.rect(self.surface, Colors.CYAN,
                                [self.house_x4 + self.house4Width // 2 + 35, self.house_y4 + self.house4Height - 55, 10, 20])

            pygame.draw.rect(self.surface, Colors.SAND,
                                [self.house_x4, self.house_y4 - self.house4Height - 2.5, self.house4Width, self.house4Height])
            pygame.draw.rect(self.surface, Colors.CYAN,
                                [self.house_x4 + self.house4Width // 2 + 15, self.house_y4 - 65, 10, 20])
            pygame.draw.rect(self.surface, Colors.CYAN,
                                [self.house_x4 + self.house4Width // 2 + 35, self.house_y4 - 65, 10, 20])
            pygame.draw.rect(self.surface, Colors.CYAN,
                                [self.house_x4 + self.house4Width // 2 - 25, self.house_y4 - 65, 10, 20])
            pygame.draw.rect(self.surface, Colors.CYAN,
                                [self.house_x4 + self.house4Width // 2 - 45, self.house_y4 - 65, 10, 20])

            pygame.draw.line(self.surface, Colors.LIGHTBROWN,
                                [self.house_x4 - 0.5, self.house_y4],
                                [self.house_x4 + self.house3Width, self.house_y4], 10)
            pygame.draw.polygon(self.surface, Colors.BROWN,
                                    ([self.house_x4 - 5, 
                                        self.house_y4 - self.house4Height],
                                    [self.house_x4 + self.house4Width + 5,
                                        self.house_y4 - self.house4Height],
                                    [self.house_x4 + self.house4Width - 5,
                                        self.house_y4 - self.house4Height - 20],
                                    [self.house_x4 + 5, 
                                        self.house_y4 - self.house4Height - 20]))

        '''SPECIAL BUILDINGS'''
        def church():
            self.churchWidth = 600
            self.churchHeight = 90
            self.church_x = 1560
            self.church_y = self.land_y - self.churchHeight

                # left building
            pygame.draw.rect(self.surface, Colors.MUSTARD,
                            [self.church_x, self.church_y - 20, self.churchWidth//4, self.churchHeight + 20])
            pygame.draw.rect(self.surface, Colors.BLACK,
                            [self.church_x + self.churchWidth // 8 - 2, self.church_y - 105, 5, 35])
            pygame.draw.rect(self.surface, Colors.BLACK,
                            [self.church_x + self.churchWidth // 8 - 10, self.church_y - 95, 20, 5])
            pygame.draw.polygon(self.surface, Colors.MIDNIGHT_BLUE,
                                ([self.church_x, self.church_y - 20],
                                [self.church_x + self.churchWidth //
                                    4, self.church_y - 20],
                                [self.church_x + self.churchWidth//8, self.church_y - 75]))
            pygame.draw.rect(self.surface, Colors.CERULEAN,
                            [self.church_x + self.churchWidth // 8 - 45, self.church_y + self.churchHeight - 65,
                            self.churchWidth // 20, self.churchHeight - 75])
            pygame.draw.circle(self.surface, Colors.CERULEAN,
                            [self.church_x + self.churchWidth // 8 - 30,
                                self.church_y + self.churchHeight - 65],
                            self.churchWidth // 40)
            pygame.draw.rect(self.surface, Colors.CERULEAN,
                            [self.church_x + self.churchWidth // 8 + 10, self.church_y + self.churchHeight - 65,
                            self.churchWidth // 20, self.churchHeight - 75])
            pygame.draw.circle(self.surface, Colors.CERULEAN,
                            [self.church_x + self.churchWidth // 8 + 25,
                                self.church_y + self.churchHeight - 65],
                            self.churchWidth // 40)
                # right building
            pygame.draw.rect(self.surface, Colors.MUSTARD,
                            [self.church_x + self.churchWidth // 2 + 150, self.church_y - 20, self.churchWidth // 4,
                            self.churchHeight + 20])
            pygame.draw.rect(self.surface, Colors.BLACK,
                            [self.church_x + self.churchWidth // 2 + 150 + self.churchWidth // 8 - 2, self.church_y - 105,
                            5, 35])
            pygame.draw.rect(self.surface, Colors.BLACK,
                            [self.church_x + self.churchWidth // 2 + 150 + self.churchWidth // 8 - 10, self.church_y - 95,
                            20, 5])
            pygame.draw.polygon(self.surface, Colors.MIDNIGHT_BLUE,
                                ([self.church_x + self.churchWidth // 2 + 150, self.church_y - 20],
                                [self.church_x + self.churchWidth // 2 + 150 +
                                    self.churchWidth // 4, self.church_y - 20],
                                [self.church_x + self.churchWidth // 2 + 150 + self.churchWidth // 8, self.church_y - 75]))
            pygame.draw.rect(self.surface, Colors.CERULEAN,
                            [self.church_x + self.churchWidth // 2 + 150 + self.churchWidth // 8 - 45, self.church_y + self.churchHeight - 65,
                            self.churchWidth // 20, self.churchHeight - 75])
            pygame.draw.circle(self.surface, Colors.CERULEAN,
                            [self.church_x + self.churchWidth // 2 + 150 + self.churchWidth //
                                8 - 30, self.church_y + self.churchHeight - 65],
                            self.churchWidth // 40)
            pygame.draw.rect(self.surface, Colors.CERULEAN,
                            [self.church_x + self.churchWidth // 2 + 150 + self.churchWidth // 8 + 10, self.church_y + self.churchHeight - 65,
                            self.churchWidth // 20, self.churchHeight - 75])
            pygame.draw.circle(self.surface, Colors.CERULEAN,
                            [self.church_x + self.churchWidth // 2 + 150 + self.churchWidth //
                                8 + 25, self.church_y + self.churchHeight - 65],
                            self.churchWidth // 40)
                # mid building
                # bot
            pygame.draw.polygon(self.surface, Colors.YELLOW,
                                ([self.church_x + self.churchWidth // 2 - 175, self.church_y],
                                [self.church_x + self.churchWidth // 2 - 175,
                                    self.church_y + self.churchHeight - 0.5],
                                [self.church_x + self.churchWidth // 2 + 175,
                                    self.church_y + self.churchHeight - 0.5],
                                [self.church_x + self.churchWidth //
                                    2 + 175, self.church_y],
                                [self.church_x + self.churchWidth // 2, self.church_y - self.church_y // 6]))
            pygame.draw.line(self.surface, Colors.MIDNIGHT_BLUE,
                            [self.church_x + self.churchWidth //
                                2 - 175, self. church_y],
                            [self.church_x + self.churchWidth//2, self. church_y - self. church_y//6], 10)
            pygame.draw.line(self.surface, Colors.MIDNIGHT_BLUE,
                            [self.church_x + self.churchWidth //
                                2 + 175, self.church_y],
                            [self.church_x + self.churchWidth//2, self. church_y - self. church_y//6], 10)
                # entrance and exit
            pygame.draw.rect(self.surface, Colors.CERULEAN,
                            [self.church_x + self.churchWidth // 2 - 100, self.church_y + self.churchHeight - 55,
                            self.churchWidth // 12, self.churchHeight - 35])
            pygame.draw.circle(self.surface, Colors.CERULEAN,
                            [self.church_x + self.churchWidth // 2 - 75,
                                self.church_y + self.churchHeight - 55],
                            self.churchWidth // 24)
            pygame.draw.rect(self.surface, Colors.CERULEAN,
                            [self.church_x + self.churchWidth // 2 - 25, self.church_y + self.churchHeight - 55,
                            self.churchWidth // 12, self.churchHeight - 35])
            pygame.draw.circle(self.surface, Colors.CERULEAN,
                            [self.church_x + self.churchWidth // 2,
                                self.church_y + self.churchHeight - 55],
                            self.churchWidth // 24)
            pygame.draw.rect(self.surface, Colors.CERULEAN,
                            [self.church_x + self.churchWidth // 2 + 50, self.church_y + self.churchHeight - 55,
                            self.churchWidth // 12, self.churchHeight - 35])
            pygame.draw.circle(self.surface, Colors.CERULEAN,
                            [self.church_x + self.churchWidth // 2 + 75,
                                self.church_y + self.churchHeight - 55],
                            self.churchWidth // 24)
                # top
            pygame.draw.polygon(self.surface, Colors.YELLOW,
                                ([self.church_x + self.churchWidth // 2 - 75, self.church_y - self.churchHeight * 2 + 30],
                                [self.church_x + self.churchWidth //
                                    2 - 75, self.church_y],
                                [self.church_x + self.churchWidth //
                                    2 + 75, self.church_y],
                                [self.church_x + self.churchWidth // 2 + 75,
                                    self.church_y - self.churchHeight * 2 + 30],
                                [self.church_x + self.churchWidth // 2, self.church_y - self.churchHeight * 2.5 + 15]))
            pygame.draw.line(self.surface, Colors.MIDNIGHT_BLUE,
                            [self.church_x + self.churchWidth // 2 - 75,
                                self.church_y - self.churchHeight * 2 + 30],
                            [self.church_x + self.churchWidth // 2, self.church_y - self.churchHeight * 2.5 + 15], 10)
            pygame.draw.line(self.surface, Colors.MIDNIGHT_BLUE,
                            [self.church_x + self.churchWidth // 2 + 75,
                                self.church_y - self.churchHeight * 2 + 30],
                            [self.church_x + self.churchWidth // 2, self.church_y - self.churchHeight * 2.5 + 15], 10)
            pygame.draw.line(self.surface, Colors.MIDNIGHT_BLUE,
                            [self.church_x + self.churchWidth //
                                2 - 75, self.church_y - 40],
                            [self.church_x + self.churchWidth // 2 + 75, self.church_y - 40], 10)
                # Holy Cross
            pygame.draw.rect(self.surface, Colors.BLACK,
                            [self.church_x + self.churchWidth // 2 - 5, self.church_y - self.churchHeight - 95, 10, 60])
            pygame.draw.rect(self.surface, Colors.BLACK,
                            [self.church_x + self.churchWidth // 2 - 20, self.church_y - self.churchHeight - 80, 40, 10])

        def school():
            self.schoolWidth = 600
            self.schoolHeight = 115
            self.school_x = 480 + 2 * 1080
            self.school_y = self.land_y - self.schoolHeight

            pygame.draw.rect(self.surface, Colors.BRICKRED,
                            [self.school_x, self.school_y, self.schoolWidth, self.schoolHeight])

            pygame.draw.polygon(self.surface, Colors.SEA_FOAM_GREEN,
                                ([self.school_x + self.schoolWidth//2 - 90, self.school_y - self.schoolHeight-20],
                                [self.school_x + self.schoolWidth//2 + 90,
                                    self.school_y - self.schoolHeight-20],
                                [self.school_x + self.schoolWidth//2, self.school_y - self.schoolHeight - 55-30]))

            pygame.draw.rect(self.surface, Colors.BRICKRED,
                            [self.school_x + self.schoolWidth//2 - 75, self.school_y - self.schoolHeight-20,
                            self.schoolWidth//4, self.schoolHeight*2])
            pygame.draw.polygon(self.surface, Colors.SEA_FOAM_GREEN,
                                ([self.school_x, self.school_y],
                                [self.school_x + self.schoolWidth, self.school_y],
                                [self.school_x + self.schoolWidth -
                                    10, self.school_y - 30],
                                [self.school_x + 15, self.school_y - 30]))
                # door
            pygame.draw.circle(self.surface, Colors.BLUEGREY,
                            [self.school_x + self.schoolWidth // 2,
                                self.school_y + self.schoolHeight - 50],
                            self.schoolWidth//20)
            pygame.draw.rect(self.surface, Colors.BLUEGREY,
                            [self.school_x + self.schoolWidth // 2 - 30, self.school_y + self.schoolHeight - 50,
                            self.schoolWidth // 10, self.schoolHeight - 65])
                # clock
            pygame.draw.circle(self.surface, Colors.AQUAMARINE,
                            [self.school_x + self.schoolWidth //
                                2, self.school_y - 90],
                            self.schoolWidth // 20 + 5)
            pygame.draw.line(self.surface, Colors.BLACK,
                            [self.school_x + self.schoolWidth // 2, self.school_y - 90],
                            [self.school_x + self.schoolWidth // 2, self.school_y - 90 - self.schoolWidth//20], 4)
            pygame.draw.line(self.surface, Colors.BLACK,
                            [self.school_x + self.schoolWidth // 2, self.school_y - 90],
                            [self.school_x + self.schoolWidth // 2 + self.schoolWidth//20 - 10, self.school_y - 90], 4)
            pygame.draw.circle(self.surface, Colors.BLACK,
                            [self.school_x + self.schoolWidth //
                                2 + 1 // 2, self.school_y - 90],
                            self.schoolWidth // 20 - 55 // 2)

                # windows
            pygame.draw.rect(self.surface, Colors.AQUAMARINE,
                            [self.school_x + 30, self.school_y + 50, self.schoolWidth//15, self.schoolHeight-85])
            pygame.draw.rect(self.surface, Colors.AQUAMARINE,
                            [self.school_x + 110, self.school_y + 50, self.schoolWidth // 15, self.schoolHeight - 85])
            pygame.draw.rect(self.surface, Colors.AQUAMARINE,
                            [self.school_x + 190, self.school_y + 50, self.schoolWidth // 15, self.schoolHeight - 85])
            pygame.draw.rect(self.surface, Colors.AQUAMARINE,
                            [self.school_x + self.schoolWidth - 70, self.school_y + 50,
                            self.schoolWidth // 15, self.schoolHeight - 85])
            pygame.draw.rect(self.surface, Colors.AQUAMARINE,
                            [self.school_x + self.schoolWidth - 150, self.school_y + 50,
                            self.schoolWidth // 15, self.schoolHeight - 85])
            pygame.draw.rect(self.surface, Colors.AQUAMARINE,
                            [self.school_x + self.schoolWidth - 230, self.school_y + 50,
                            self.schoolWidth // 15, self.schoolHeight - 85])

        def supermarket():
            self.supermarketWidth = 600
            self.supermarketHeight = 110
            self.supermarket_x = 480 + 3*1080
            self.supermarket_y = self.land_y - self.supermarketHeight

            pygame.draw.rect(self.surface, Colors.TEAL,
                            [self.supermarket_x, self.supermarket_y - self.supermarketHeight,
                            self.supermarketWidth, self.supermarketHeight * 2])
            pygame.draw.line(self.surface, Colors.BURNT_ORANGE,
                            [self.supermarket_x, self.supermarket_y],
                            [self.supermarket_x + self.supermarketWidth, self.supermarket_y], 10)
                # doors
            pygame.draw.rect(self.surface, Colors.BRIGHT_BLUE,
                            [self.supermarket_x + self.supermarketWidth//2 - 40, self.supermarket_y + 45,
                            self.supermarketWidth * 2 // 15, self.supermarketHeight - 45])
            pygame.draw.rect(self.surface, Colors.BRIGHT_BLUE,
                            [self.supermarket_x + self.supermarketWidth // 2 - 40 - 80 - 15, self.supermarket_y + 45,
                            self.supermarketWidth * 2 // 15, self.supermarketHeight - 45])
            pygame.draw.rect(self.surface, Colors.BRIGHT_BLUE,
                            [self.supermarket_x + self.supermarketWidth // 2 + 40 + 15, self.supermarket_y + 45,
                            self.supermarketWidth * 2 // 15, self.supermarketHeight - 45])
            pygame.draw.polygon(self.surface, Colors.DARK_YELLOW,
                                ([self.supermarket_x + self.supermarketWidth // 2 + 40 + 80 + 15 + 15, self.supermarket_y + 45],
                                [self.supermarket_x + self.supermarketWidth //
                                    2 + 40 + 80 + 15, self.supermarket_y + 15],
                                [self.supermarket_x + self.supermarketWidth //
                                    2 - 40 - 80 - 15, self.supermarket_y + 15],
                                [self.supermarket_x + self.supermarketWidth // 2 - 40 - 80 - 15 - 15, self.supermarket_y + 45]))
                # windows
            pygame.draw.rect(self.surface, Colors.BRIGHT_BLUE,
                            [self.supermarket_x + 56, self.supermarket_y - self.supermarketHeight + 15,
                            80, 80])
            pygame.draw.rect(self.surface, Colors.BRIGHT_BLUE,
                            [self.supermarket_x + 192, self.supermarket_y - self.supermarketHeight + 15,
                            80, 80])
            pygame.draw.rect(self.surface, Colors.BRIGHT_BLUE,
                            [self.supermarket_x + 328, self.supermarket_y - self.supermarketHeight + 15,
                            80, 80])
            pygame.draw.rect(self.surface, Colors.BRIGHT_BLUE,
                            [self.supermarket_x + 464, self.supermarket_y - self.supermarketHeight + 15,
                            80, 80])

            pygame.draw.polygon(self.surface, Colors.BURNT_ORANGE,
                                ([self.supermarket_x, self.supermarket_y - self.supermarketHeight],
                                [self.supermarket_x, self.supermarket_y -
                                    self.supermarketHeight - 20],
                                [self.supermarket_x + self.supermarketWidth//2 - 135,
                                    self.supermarket_y - self.supermarketHeight - 20],
                                [self.supermarket_x + self.supermarketWidth//2 - 135,
                                    self.supermarket_y - self.supermarketHeight - 50],
                                [self.supermarket_x + self.supermarketWidth//2 + 135,
                                    self.supermarket_y - self.supermarketHeight - 50],
                                [self.supermarket_x + self.supermarketWidth//2 + 135,
                                    self.supermarket_y - self.supermarketHeight - 20],
                                [self.supermarket_x + self.supermarketWidth,
                                    self.supermarket_y - self.supermarketHeight - 20],
                                [self.supermarket_x + self.supermarketWidth, self.supermarket_y - self.supermarketHeight]))

        def hospital():
            self.hospitalWidth = 600
            self.hospitalHeight = 200
            self.hospital_x = 480
            self.hospital_y = self.land_y - self.hospitalHeight

            pygame.draw.rect(self.surface, Colors.WHITE,
                            [self.hospital_x, self.hospital_y - self.hospitalHeight//2,
                            self.hospitalWidth, self.hospitalHeight + self.hospitalHeight//2])

            for j in range(self.hospital_y - 80 + 20, self.hospital_y + 101, 80):
                for i in range(self.hospital_x + 20, self.hospital_x + 300 - 100, 50):
                    pygame.draw.rect(self.surface, Colors.BLUE,
                                    [i, j, 30, 60])

                for i in range(self.hospital_x + 300 + 100, self.hospital_x + self.hospitalWidth - 21, 50):
                    pygame.draw.rect(self.surface, Colors.BLUE,
                                    [i, j, 30, 60])

            pygame.draw.rect(self.surface, Colors.CYAN,
                            [self.hospital_x + self.hospitalWidth//2 - 40, self.hospital_y + self.hospitalHeight // 2,
                            self.hospitalWidth//10 + 20, self.hospitalHeight // 2])
            pygame.draw.rect(self.surface, Colors.RED,
                            [self.hospital_x + self.hospitalWidth // 2 - 10, self.hospital_y - self.hospitalHeight // 2 + 20,
                            self.hospitalWidth // 30, self.hospitalHeight // 2.5])
            pygame.draw.rect(self.surface, Colors.RED,
                            [self.hospital_x + self.hospitalWidth // 2 - 40,
                            self.hospital_y - self.hospitalHeight // 4,
                            self.hospitalWidth // 7.5, self.hospitalHeight // 10])
        


        '''DRAW HOUSES'''
        for i in range(self.quantity):
            house_1(1080 * i)
            house_2(360 + 1080 * i)
            house_3(120 + 1080 * i)
            house_4(240 + 1080 * i)
            pass

        church()
        school()
        supermarket()
        hospital()
        pass

    def draw(self):
        Screen.blit(self.surface, (self.pos_x, self.pos_y))
        # ...

    def update(self, player):
        key_pressed = pygame.key.get_pressed()
        if player.theme_extend_left and key_pressed[pygame.K_a] and player.pos_x > self.pos_x + 100:
            self.pos_x -= self.theme_speed
        if player.theme_extend_right and key_pressed[pygame.K_d] and player.pos_x + player.surface_width < self.pos_x + self.surface_width - 100:
            self.pos_x += self.theme_speed
# unfinished
