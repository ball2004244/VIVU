from setting import Screen, Colors, FontType
import pygame
from pygame.locals import *
pygame.init()


class Player():
    def __init__(self):
        # Game Surface: The surface with S = 1024 * 768
        self.game_surface_height = 768
        self.game_surface_width = 1024
        self.game_surface_x = 0
        self.game_surface_y = 0
        self.game_surface = pygame.Surface(
            (self.game_surface_width, self.game_surface_height), pygame.SRCALPHA)

        self.theme_extend_left = False
        self.theme_extend_right = False

        # Player Surface
        '''Delete SRCALPHA to see hitbox in black Colors'''
        self.surface_height = 60
        self.surface_width = self.surface_height + 30
        self.pos_x = 1024 / 2 - 150
        self.pos_y = 500 - self.surface_height

        self.surface = pygame.Surface(
            (self.surface_width, self.surface_height), pygame.SRCALPHA)

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

        # Money
        self.money = 1000

        pass

    def draw(self):
        Screen.blit(self.surface, (self.pos_x, self.pos_y))
        Screen.blit(self.game_surface,
                    (self.game_surface_x, self.game_surface_y))
        pass

    def update(self, status):
        def movement():
            #print(status.die)
            if not status.die:
                '''MOVING IN 4 DIRECTIONS'''
                key_pressed = pygame.key.get_pressed()
                # Moving Left
                if key_pressed[pygame.K_a] and not self.theme_extend_left:
                    self.pos_x -= self.speed

                # Moving Right
                if key_pressed[pygame.K_d] and not self.theme_extend_right:
                    self.pos_x += self.speed

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

                # Moving background while character moving near border
                # CHECK LEFT BORDER
                if self.pos_x < self.game_surface_x + 100:
                    self.theme_extend_left = True
                else:
                    self.theme_extend_left = False

                # CHECK RIGHT BORDER
                if self.pos_x + self.surface_width > self.game_surface_x + self.game_surface_width - 100:
                    self.theme_extend_right = True
                else:
                    self.theme_extend_right = False
                
                # DEBUGGING
                '''print(str(self.pos_x) + ' ' + str(self.theme_extend_left) +
                    ' ' + str(self.theme_extend_right))'''
        movement()
        pass


class StatusBar():
    def __init__(self):
        '''INITIALIZE VISUAL HP/MP BARS'''
        # surface
        self.surface_width = 260
        self.surface_height = self.surface_width / 2 - 20
        self.pos_x = 10
        self.pos_y = 10
        self.surface = pygame.Surface(
            (self.surface_width, self.surface_height))
        self.surface.fill(Colors.LIGHTBROWN)

        # frame
        self.frame_x = 10
        self.frame_y = 5
        self.frame_width = self.surface_width - 20
        self.frame_height = self.surface_height - 10

        # hp bar (hp range: 50 -> 190)
        self.hp_x = self.frame_x + 45
        self.hp_y = self.frame_y + 10
        self.max_hp = 190
        self.hp_height = 28
        self.current_hp = self.max_hp
        self.get_damage = False
        self.die = False

        # mp bar (mp range: 50 -> 190)
        self.mp_x = self.hp_x
        self.mp_y = self.hp_y + 40
        self.max_mp = 50
        self.current_mp = self.max_mp
        self.mp_height = self.hp_height
        self.use_mana = False
        self.out_of_mana = False

        pass

    def draw(self):
        # visualize images
        Screen.blit(self.surface, (self.pos_x, self.pos_y))

        # draw frame of status bar
        pygame.draw.rect(self.surface, Colors.WHITE, (self.frame_x,
                         self.frame_y, self.frame_width, self.frame_height))

        # print hp text
        Screen.blit(pygame.font.Font.render(
            FontType.FONT3, 'HP: ', True, Colors.LIGHTBROWN), (self.hp_x - 25, self.hp_y + self.hp_height / 2 - 3))
        Screen.blit(pygame.font.Font.render(
            FontType.FONT3, str(self.current_hp) + '/' + str(self.max_hp), True, Colors.WHITE), (self.hp_x + 12, self.hp_y + self.hp_height / 2 - 3))

        # draw hp bar
        pygame.draw.rect(self.surface, Colors.BLACK, (self.hp_x,
                         self.hp_y, self.max_hp, self.hp_height))
        pygame.draw.rect(self.surface, Colors.RED, (self.hp_x,
                         self.hp_y, self.current_hp, self.hp_height))

        # print mp text
        Screen.blit(pygame.font.Font.render(
            FontType.FONT3, 'MP: ', True, Colors.LIGHTBROWN), (self.mp_x - 25, self.mp_y + self.mp_height / 2 - 3))
        Screen.blit(pygame.font.Font.render(
            FontType.FONT3, str(self.current_mp) + '/' + str(self.max_mp), True, Colors.WHITE), (self.mp_x + 12, self.mp_y + self.mp_height / 2 - 3))

        # draw mp bar
        pygame.draw.rect(self.surface, Colors.BLACK, (self.mp_x,
                         self.mp_y, self.max_mp, self.mp_height))
        pygame.draw.rect(self.surface, Colors.BLUE, (self.mp_x,
                         self.mp_y, self.current_mp, self.mp_height))

        pass

    def update(self):
        '''CONSUMING HP/MP'''
        # Self-damage button
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_e]:
            self.get_damage = True
        else:
            self.get_damage = False

        # Use-mana button
        if key_pressed[pygame.K_r]:
            self.use_mana = True
        else:
            self.use_mana = False

        if self.get_damage:
            self.current_hp -= 1
            if self.current_hp <= 0:
                self.die = True
                self.current_hp = 0

        if self.use_mana == True:
            self.current_mp -= 1
            if self.current_mp <= 0:
                self.out_of_mana = True
                self.current_mp = 0

        if self.die:
            pass
        # DEBUG
        #print(self.current_hp, ' ', self.current_mp)
        # Unfinished
        pass


class Inventory():
    def __init__(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass
