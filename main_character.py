from setting import Screen, Colors, FontType
import pygame
from pygame.locals import *
pygame.init()


class Player():
    def __init__(self):
        # Surface
        '''Delete SRCALPHA to see hitbox in black Colors'''
        self.surface_height = 60
        self.surface_width = self.surface_height + 30
        self.surface = pygame.Surface(
            (self.surface_width, self.surface_height), SRCALPHA)

        '''CUSTOMIZE PLAYER'S APPEARANCE'''
        # Legs
        self.leg_width = 14
        self.leg_height = self.leg_width
        # left leg
        self.left_leg_x = self.surface_width // 2 - 20
        self.left_leg_y = self.surface_height - self.leg_height
        pygame.draw.rect(self.surface, Colors.BLACK, (self.left_leg_x,
                                                      self.left_leg_y, self.leg_width, self.leg_height))

        # right leg
        self.right_leg_x = self.left_leg_x + 5
        self.right_leg_y = self.left_leg_y
        pygame.draw.rect(self.surface, Colors.BLACK, (self.right_leg_x + 20,
                         self.right_leg_y, self.leg_width, self.leg_height))

        # Body
        self.body_x = self.right_leg_x + self.leg_width
        self.body_y = self.left_leg_y - 19
        self.body_rad = 25
        pygame.draw.circle(self.surface, Colors.RED,
                           (self.body_x, self.body_y), self.body_rad)

        # Eyes
        self.eye_x = self.body_x + 10
        self.eye_y = self.body_y - 1
        self.eye_rad = 10
        self.eye_rad_inner = self.eye_rad - 6
        pygame.draw.circle(self.surface, Colors.WHITE,
                           (self.eye_x - 22, self.eye_y), self.eye_rad)
        pygame.draw.circle(self.surface, Colors.WHITE,
                           (self.eye_x, self.eye_y), self.eye_rad)
        pygame.draw.circle(self.surface, Colors.BLACK,
                           (self.eye_x - 22, self.eye_y), self.eye_rad_inner)
        pygame.draw.circle(self.surface, Colors.BLACK, (self.eye_x,
                           self.eye_y), self.eye_rad_inner)

        # Arms
        self.arm_rad = 7
        # left arm
        self.left_arm_x = self.body_x - self.body_rad - self.arm_rad
        self.left_arm_y = self.body_y + 2

        pygame.draw.circle(self.surface, Colors.BLACK,
                           (self.left_arm_x, self.left_arm_y), self.arm_rad)

        # right arm
        self.right_arm_x = self.body_x + self.body_rad + self.arm_rad
        self.right_arm_y = self.body_y + 2

        pygame.draw.circle(self.surface, Colors.BLACK,
                           (self.right_arm_x, self.right_arm_y), self.arm_rad)

        '''VARIABLE FOR MECHANISM'''
        # Walking
        self.init_speed = 3
        self.speed = self.init_speed
        self.run_speed = self.init_speed + 2

        # Jumping
        self.jump = False
        self.jump_speed = 5

        self.jump_step = 0
        self.jump_limit = 150

        # Falling
        self.fall = False
        self.fall_speed = 7

        # Attacking
        self.init_damage = 5
        self.damage = self.init_damage
        self.give_damage_left = False
        self.give_damage_right = False

        # Extend them
        self.theme_extend_left = False
        self.theme_extend_right = False

        # Surface's position
        self.pos_x = 1024 / 2 - 150
        self.pos_y = 500 - self.surface_height
        pass

    def draw(self):
        Screen.blit(self.surface, (self.pos_x, self.pos_y))
        pass

    def update(self):
        '''MOVING IN 4 DIRECTIONS'''
        key_pressed = pygame.key.get_pressed()
        # Moving Left
        if key_pressed[pygame.K_a]:
            self.pos_x -= self.speed

        # Moving Right
        if key_pressed[pygame.K_d]:
            self.pos_x += self.speed

        # Moving background while character moving near border
        if self.pos_x < 100:
            self.theme_extend_left = True
        else:
            self.theme_extend_left = False

        if self.pos_x > 924:
            self.theme_extend_right = True
        else:
            self.them_extend_right = False

        # Jumping & Falling
            # get key
        if key_pressed[pygame.K_w] and self.jump == False and self.fall == False:
            self.jump = True

            # stand still -> jump
        if self.jump == True and self.fall == False and self.jump_step < self.jump_limit:
            self.pos_y -= self.jump_speed
            self.jump_step += self.jump_speed

            # jump -> fall
        if self.jump_step >= self.jump_limit:
            self.jump = False
            self.fall = True

        if self.jump == False and self.fall == True and self.jump_step > 0:
            self.pos_y += self.fall_speed
            self.jump_step -= self.fall_speed

            # fall -> stand still
        if self.jump_step <= 0:
            self.fall = False

        # Running
        if key_pressed[pygame.K_LCTRL]:
            self.speed = self.run_speed
        else:
            self.speed = self.init_speed

        # Attacking
        # get mouse pos
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()

                if mouseX < self.body_x + self.body_rad:
                    self.give_damage_left = True
                else:
                    self.give_damage_right = True
            else:
                self.give_damage_left = False
                self.give_damage_right = False
        # Unfinished

    pass


class StatusBar():
    def __init__(self):
        '''INITIALIZE VISUAL HP/MP BARS'''
        # surface
        self.surface_width = 260
        self.surface_height = self.surface_width / 2 - 20
        self.surface = pygame.Surface(
            (self.surface_width, self.surface_height))
        self.surface.fill(Colors.LIGHTBROWN)

        # frame
        self.frame_x = 10
        self.frame_y = 5
        self.frame_width = self.surface_width - 20
        self.frame_height = self.surface_height - 10
        pygame.draw.rect(self.surface, Colors.WHITE, (self.frame_x,
                         self.frame_y, self.frame_width, self.frame_height))

        # hp bar
        self.hp_x = self.frame_x + 45
        self.hp_y = self.frame_y + 10
        self.hp_width = 70
        self.hp_height = 28
        pygame.draw.rect(self.surface, Colors.RED, (self.hp_x,
                         self.hp_y, self.hp_width, self.hp_height))

        # mp bar
        self.mp_x = self.hp_x
        self.mp_y = self.hp_y + 40
        self.mp_width = 70
        self.mp_height = self.hp_height
        pygame.draw.rect(self.surface, Colors.BLUE, (self.mp_x,
                         self.mp_y, self.mp_width, self.mp_height))

        '''VARIABLE FOR MECHANISM'''
        # HP/MP
        self.max_hp = self.hp_width
        self.hp_amount = self.max_hp
        self.get_damage = False

        self.max_mp = self.mp_width
        self.mp_amount = self.max_mp
        self.use_mana = False

        self.die = False

        # Surface's position
        self.pos_x = 10
        self.pos_y = 10

        pass

    def draw(self):
        # visualize images
        Screen.blit(self.surface, (self.pos_x, self.pos_y))

        # print hp text
        Screen.blit(pygame.font.Font.render(
            FontType.FONT3, 'HP: ', True, Colors.LIGHTBROWN), (self.hp_x - 25, self.hp_y + self.hp_height / 2 - 3))
        Screen.blit(pygame.font.Font.render(
            FontType.FONT3, str(self.hp_amount) + '/' + str(self.max_hp), True, Colors.WHITE), (self.hp_x + 10, self.hp_y + self.hp_height / 2 - 3))

        # print mp text

        Screen.blit(pygame.font.Font.render(
            FontType.FONT3, 'MP: ', True, Colors.LIGHTBROWN), (self.mp_x - 25, self.mp_y + self.mp_height / 2 - 3))
        Screen.blit(pygame.font.Font.render(
            FontType.FONT3, str(self.mp_amount) + '/' + str(self.max_mp), True, Colors.WHITE), (self.mp_x + 10, self.mp_y + self.mp_height / 2 - 3))
        pass

    def update(self):
        '''CONSUMING HP/MP'''
        if self.get_damage == True and self.hp_width > 0:
            self.hp_width -= 1
        else:
            self.die = True

        if self.use_mana == True and self.mp_width > 0:
            self.mp_width -= 1

        # Unfinished
        pass
