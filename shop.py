from setting import Screen, Colors, FontType
import pygame
from pygame.locals import *
pygame.init()


class ShopThemeOne():
    def __init__(self):
        # Theme Surface
        self.surface = pygame.Surface((1024, 768), pygame.SRCALPHA)
        self.surface.fill(Colors.LIGHTBROWN)
        self.pos_x = 0
        self.pos_y = 0
        self.shopping = False  # Check if player opens/exits shop

        # Stall

        def stall():
            self.stall_x = 100
            self.stall_y = 100
            self.stall_width = 150
            self.stall_height = 200
            pygame.draw.rect(self.surface, Colors.BLACK, (self.stall_x,
                                                          self.stall_y, self.stall_width, self.stall_height))

            pygame.draw.rect(self.surface, (169, 169, 169), (self.stall_x + self.stall_width // 15,
                                                             self.stall_y + self.stall_height // 14, self.stall_width * 13 // 15, self.stall_height * 12 // 14))

            # Buy / Sell button
            # buy
            self.buy_x = self.stall_x
            self.buy_y = self.stall_y + self.stall_height
            self.buy_width = self.stall_width // 2
            self.buy_height = self.stall_height // 5
            self.buy_button = pygame.Surface(
                (self.buy_width, self.buy_height), pygame.SRCALPHA)
            self.buy_button.fill(Colors.GREEN)

            # sell
            self.sell_x = self.buy_x + self.buy_width
            self.sell_y = self.buy_y
            self.sell_width = self.buy_width
            self.sell_height = self.buy_height
            self.sell_button = pygame.Surface(
                (self.sell_width, self.sell_height), pygame.SRCALPHA)
            self.sell_button.fill(Colors.RED)

        def money_bar():
            # frame
            self.money_bar_x = 30
            self.money_bar_y = 20
            self.money_bar_width = 160
            self.money_bar_height = 50
            pygame.draw.rect(self.surface, Colors.BROWN, (self.money_bar_x,
                             self.money_bar_y, self.money_bar_width, self.money_bar_height))
            pygame.draw.rect(self.surface, Colors.WHITE, (self.money_bar_x + self.money_bar_width // 25,
                             self.money_bar_y + self.money_bar_height // 10, self.money_bar_width * 23 // 25, self.money_bar_height * 8 // 10))

        # draw
        stall()
        money_bar()

        '''VARIABLE FOR MECHANISM'''
        self.buying = False
        self.selling = False

        self.show_buy_price = False
        self.show_sell_price = False
        pass

    def draw(self, player, weapon):
        if self.shopping:
            Screen.blit(self.surface, (self.pos_x, self.pos_y))

            # print weapon to stall
            weapon_x = self.stall_x + self.stall_width // 2 - weapon.width // 2
            weapon_y = self.stall_y + self.stall_height // 2 - weapon.height // 2

            Screen.blit(weapon.surface, (weapon_x, weapon_y))     

            # money
            Screen.blit(pygame.font.Font.render(
                FontType.FONT3, 'Money: ', True, Colors.BLACK), (self.money_bar_x * 3 // 2, self.money_bar_y + self.money_bar_height // 3))
            Screen.blit(pygame.font.Font.render(
                FontType.FONT3, str(player.money), True, Colors.BLACK), (self.money_bar_x * 7 // 2, self.money_bar_y + self.money_bar_height // 3))


            # print buy
            Screen.blit(self.buy_button, (self.buy_x, self.buy_y))

            #show price when hovering
            if self.show_buy_price:
                self.buy_button.fill((221, 221, 221))
                buy_text = str(weapon.buy_price)
                pass
            else: 
                self.buy_button.fill(Colors.GREEN)
                buy_text = 'BUY'
                pass

            buy_show = pygame.font.Font.render(
                FontType.FONT3, buy_text, True, Colors.BLACK)
            buy_show_rect = buy_show.get_rect(center=(self.buy_x + self.buy_width // 2, self.buy_y + self.buy_height // 2))
            
            Screen.blit(buy_show, buy_show_rect)

            # print sell
            Screen.blit(self.sell_button, (self.sell_x, self.sell_y))
            
            #show price when hovering
            if self.show_sell_price:
                self.sell_button.fill((221, 221, 221))
                sell_text = str(weapon.sell_price)
                pass
            else:
                self.sell_button.fill(Colors.RED)
                sell_text = 'SELL'
                pass

            sell_show = pygame.font.Font.render(
                FontType.FONT3, sell_text, True, Colors.BLACK)
            sell_show_rect = sell_show.get_rect(center=(self.sell_x + self.sell_width // 2, self.sell_y + self.sell_height // 2))
            
            Screen.blit(sell_show, sell_show_rect)
        pass

    def toggle(self):
        # Toggle Shop
        self.shopping = not self.shopping
        pass

    def trading(self, player, weapon):
        # Check Buy / Sell Mechanism
        (mouseX, mouseY) = pygame.mouse.get_pos()

        # buy
        if self.buy_button.get_rect(topleft=(self.buy_x, self.buy_y)).collidepoint((mouseX, mouseY)):
            if player.money >= weapon.buy_price:
                self.buying = True
            else:
                self.buying = False

            if self.buying:
                player.money -= weapon.buy_price
                self.buying = False

        # sell
        if self.sell_button.get_rect(topleft=(self.sell_x, self.sell_y)).collidepoint((mouseX, mouseY)):
            self.selling = True

            if self.selling:
                player.money += weapon.sell_price
                self.selling = False
       
    def update(self):
        # show price when mouse hover
        (mouseX, mouseY) = pygame.mouse.get_pos()
        # show price when mouse hover
        if self.buy_button.get_rect(topleft=(self.buy_x, self.buy_y)).collidepoint((mouseX, mouseY)):
            self.show_buy_price = True
        else: 
            self.show_buy_price = False
        
        if self.sell_button.get_rect(topleft=(self.sell_x, self.sell_y)).collidepoint((mouseX, mouseY)):
            self.show_sell_price = True
        else:
            self.show_sell_price = False
        pass
