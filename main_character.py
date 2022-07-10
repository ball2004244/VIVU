from setting import Screen, Colors, FontType
import pygame
from pygame.locals import *
pygame.init()


class Player():
    def __init__(self):
        # Game Surface: The surface with S = 1024 * 768
        # This surface served for mechanism (moving,...)
        self.game_surface_height = 768
        self.game_surface_width = 1024
        self.game_surface_x = 0
        self.game_surface_y = 0
        self.game_surface = pygame.Surface(
            (self.game_surface_width, self.game_surface_height), pygame.SRCALPHA)

        self.theme_extend_left = False
        self.theme_extend_right = False

        # Player Surface
        # This surface is square shaped surrounding player's body
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

        # Attribute
        self.name = 'NAME'
        self.money = 1000
        pass

    def draw(self):
        Screen.blit(self.surface, (self.pos_x, self.pos_y))
        Screen.blit(self.game_surface,
                    (self.game_surface_x, self.game_surface_y))
        pass

    def update(self, status):
        def movement():
            # print(status.die)
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
                pass
        movement()
        pass

    pass


class StatusBar():
    def __init__(self):
        '''INITIALIZE VISUAL HP/MP/EXP BARS'''
        # surface
        self.surface_width = 270
        self.surface_height = self.surface_width // 2 - 20
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

        # level and exp
        self.exp_x = self.frame_x + 45
        self.exp_y = self.frame_y + self.frame_height - 8 - 20
        self.exp_height = 23

        self.init_lv = 1
        self.current_lv = self.init_lv + 0
        self.max_lv = 100

        self.current_exp = 1
        self.init_max_exp = 50
        self.full_exp = self.init_max_exp * self.current_lv

        # hp bar (hp range: 50 -> 190)
        self.hp_x = self.frame_x + 45
        self.hp_y = self.frame_y + 8
        self.hp_height = 23

        self.init_hp = 50  # hp at lv 1
        self.max_hp = 200  # hp at lv max

        self.hp_rate = (self.max_hp - self.init_hp) / \
            (self.max_lv - 1)  # chang in hp when level up
        self.full_hp = self.init_hp + \
            round((self.current_lv - 1) * self.hp_rate)  # hp when full
        self.current_hp = self.full_hp  # hp if take damages

        self.get_damage = False
        self.die = False

        # mp bar (mp range: 50 -> 190)
        self.mp_x = self.hp_x
        self.mp_y = self.hp_y + 34
        self.mp_height = self.hp_height

        self.init_mp = 50  # mp at lv 1
        self.max_mp = 200  # mp at lv max

        self.mp_rate = (self.max_mp - self.init_mp) / \
            (self.max_lv - 1)  # change in mp when level up
        self.full_mp = self.init_mp + \
            round((self.current_lv - 1) * self.mp_rate)  # mp when do nothing
        self.current_mp = self.full_mp  # mp if used
        self.use_mana = False
        self.out_of_mana = False

        '''INITIALIZE OTHER ATTRIBUTES'''
        pass

    def draw(self):
        # visualize images
        Screen.blit(self.surface, (self.pos_x, self.pos_y))

        # draw frame of status bar
        pygame.draw.rect(self.surface, Colors.WHITE, (self.frame_x,
                         self.frame_y, self.frame_width, self.frame_height))

        # print hp text
        Screen.blit(pygame.font.Font.render(
            FontType.FONT3, 'HP: ', True, Colors.RED), (self.hp_x - 25, self.hp_y + self.hp_height / 2 - 3))
        Screen.blit(pygame.font.Font.render(
            FontType.FONT3, str(self.current_hp) + '/' + str(self.full_hp), True, Colors.WHITE), (self.hp_x + 12, self.hp_y + self.hp_height / 2 - 3))

        # draw hp bar
        pygame.draw.rect(self.surface, Colors.BLACK, (self.hp_x,
                         self.hp_y, self.full_hp, self.hp_height))
        pygame.draw.rect(self.surface, Colors.RED, (self.hp_x,
                         self.hp_y, self.current_hp, self.hp_height))

        # print mp text
        Screen.blit(pygame.font.Font.render(
            FontType.FONT3, 'MP: ', True, Colors.BLUE), (self.mp_x - 25, self.mp_y + self.mp_height / 2 - 3))
        Screen.blit(pygame.font.Font.render(
            FontType.FONT3, str(self.current_mp) + '/' + str(self.full_mp), True, Colors.WHITE), (self.mp_x + 12, self.mp_y + self.mp_height / 2 - 3))

        # draw mp bar
        pygame.draw.rect(self.surface, Colors.BLACK, (self.mp_x,
                         self.mp_y, self.full_mp, self.mp_height))
        pygame.draw.rect(self.surface, Colors.BLUE, (self.mp_x,
                         self.mp_y, self.current_mp, self.mp_height))

        # print lv and exp text:
        Screen.blit(pygame.font.Font.render(FontType.FONT3, 'LV ' + str(self.current_lv) + ' (' + str(self.current_exp) + '/' +
                    str(self.full_exp) + ' exp)', True, Colors.GRASSGREEN), (self.exp_x - 25, self.exp_y + self.exp_height / 2 - 3))

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

    pass


class Inventory():
    def __init__(self):
        # draw inventory
        self.surface_width = 1024
        self.surface_height = 768
        self.surface = pygame.Surface(
            (self.surface_width, self.surface_height), pygame.SRCALPHA)
        self.surface.fill(Colors.LIGHTBROWN)
        self.pos_x = 0
        self.pos_y = 0
        self.inventory_open = False

        # draw background
        # left up rect
        self.left_up_rect_x = 30
        self.left_up_rect_y = 30
        self.left_up_rect_width = self.surface_width * 42 // 100
        self.left_up_rect_height = self.surface_height * 55 // 100
        pygame.draw.rect(self.surface, Colors.WHITE, (self.left_up_rect_x,
                         self.left_up_rect_y, self.left_up_rect_width, self.left_up_rect_height))

        # left down rect
        self.left_down_rect_x = self.left_up_rect_x
        self.left_down_rect_y = self.left_up_rect_y + self.left_up_rect_height + 20
        self.left_down_rect_width = self.left_up_rect_width
        self.left_down_rect_height = self.surface_height - self.left_down_rect_y - 30
        pygame.draw.rect(self.surface, Colors.WHITE, (self.left_down_rect_x,
                         self.left_down_rect_y, self.left_down_rect_width, self.left_down_rect_height))

        # right rect
        self.right_rect_x = self.left_up_rect_x + self.left_up_rect_width + 20
        self.right_rect_y = self.left_up_rect_y
        self.right_rect_width = self.surface_width - self.right_rect_x - 30
        self.right_rect_height = self.left_down_rect_y + self.left_down_rect_height - 30
        pygame.draw.rect(self.surface, Colors.WHITE, (self.right_rect_x,
                         self.right_rect_y, self.right_rect_width, self.right_rect_height))
        pass

    def draw(self, player, item, status):
        def display_char():  # use left_up_rect
            # draw character
            ratio = 3
            width = player.surface_width * ratio
            height = player.surface_height * ratio
            x = self.left_up_rect_x + self.left_up_rect_width // 2 - width // 2
            y = self.left_up_rect_y + self.left_up_rect_height * 60 // 100 - height // 2
            inventory_player_surface = pygame.transform.scale(
                player.surface, (width, height))

            # display name
            name_x = x + width // 2
            name_y = self.left_up_rect_y + self.left_up_rect_width * 8 // 100
            name = player.name
            name_show = pygame.font.Font.render(
                FontType.FONT1, name, True, Colors.LIGHTBROWN)
            name_show_rect = name_show.get_rect(center=(name_x, name_y))
            # display lv
            lv_x = name_x
            lv_y = name_y * 200 // 100
            lv = str(status.current_lv)
            lv_show = pygame.font.Font.render(
                FontType.FONT2, 'LV ' + lv, True, Colors.LIGHTBROWN)
            lv_show_rect = lv_show.get_rect(center=(lv_x, lv_y))

            # display exp
            exp_x = lv_x
            exp_y = lv_y * 130 // 100
            current_exp = str(status.current_exp)
            full_exp = str(status.full_exp)
            exp_show = pygame.font.Font.render(
                FontType.FONT2, current_exp + ' / ' + full_exp, True, Colors.LIGHTBROWN)
            exp_show_rect = exp_show.get_rect(center=(exp_x, exp_y))

            # Draw to screen
            Screen.blit(inventory_player_surface, (x, y))

            # Print Name, Level, Exp
            Screen.blit(name_show, name_show_rect)
            Screen.blit(lv_show, lv_show_rect)
            Screen.blit(exp_show, exp_show_rect)
            pass

        def display_status():
            # use left_down_rect

            def show_status_col1(name, max):
                gap_y = self.left_down_rect_height // 7  # distance between lines
                x = self.left_down_rect_x + self.left_down_rect_width // 6
                y = self.left_down_rect_y

                for i in range(2):
                    text = pygame.font.Font.render(
                        FontType.FONT2, name[i] + str(max[i]), True, Colors.BLACK)
                    text_rect = text.get_rect(center=(x, y + gap_y * (i + 1)))

                    Screen.blit(text, text_rect)
                pass

            def show_status_col2(name, max):
                gap_y = self.left_down_rect_height // 7  # distance between lines
                x = self.left_down_rect_x + self.left_down_rect_width * 70 // 100
                y = self.left_down_rect_y

                for i in range(1):
                    text = pygame.font.Font.render(
                        FontType.FONT2, name[i] + str(max[i]), True, Colors.BLACK)
                    text_rect = text.get_rect(center=(x, y + gap_y * (i + 1)))

                    Screen.blit(text, text_rect)
                pass

            show_status_col1(['HP: ', 'MP: '], [status.max_hp, status.max_mp])
            show_status_col2(['TEST: '], [100])
            # unfinished
            pass

        def display_item():
            # use right_rect
            ratio = 1 / 2

            x = self.right_rect_x + self.right_rect_width * 3 // 100
            y = self.right_rect_y + self.right_rect_height * 1 // 100
            width = 100
            height = width
            item_width = int(item.surface_width * ratio)
            item_height = int(item.surface_height * ratio)
            box = pygame.Surface((width, height), pygame.SRCALPHA)
            box.fill((211, 211, 211))
            pygame.draw.rect(box, Colors.BLACK, (0, 0, width, height), 5)

            item_surface = pygame.transform.scale(
                item.surface, (item_width, item_height))
            item_surface_rect = item_surface.get_rect(
                center=(x + width // 2, y + height // 2))

            Screen.blit(box, (x, y))
            Screen.blit(item_surface, item_surface_rect)

            pass

        def debug():
            # Drawing grids for calculating
            pygame.draw.rect(self.surface, Colors.BLACK, (self.left_up_rect_x +
                             self.left_up_rect_width // 2 - 1, 0, 2, 768))
            pygame.draw.rect(self.surface, Colors.BLACK, (0,
                             self.left_up_rect_y + self.left_up_rect_height // 2 - 1, 1024, 2))

            pygame.draw.rect(self.surface, Colors.BLACK, (self.right_rect_x +
                             self.right_rect_width // 2 - 1, 0, 2, 768))
            pygame.draw.rect(self.surface, Colors.BLACK, (0,
                             self.left_down_rect_y + self.left_down_rect_height // 2 - 1, 1024, 2))
            pass

        if self.inventory_open:
            Screen.blit(self.surface, (self.pos_x, self.pos_y))
            debug()
            display_char()
            display_status()
            display_item()
        pass

    def toggle(self):
        self.inventory_open = not self.inventory_open
        pass

    def update(self):
        pass
    pass
