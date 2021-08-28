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
            pygame.draw.rect(self.surface, Colors.GREEN, (self.buy_x,
                             self.buy_y, self.buy_width, self.buy_height))

            # sell
            self.sell_x = self.buy_x + self.buy_width
            self.sell_y = self.buy_y
            self.sell_width = self.buy_width
            self.sell_height = self.buy_height
            pygame.draw.rect(self.surface, Colors.RED, (self.sell_x,
                             self.sell_y, self.sell_width, self.sell_height))

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
        pass

    def draw(self, player, weapon):
        if self.shopping:
            Screen.blit(self.surface, (self.pos_x, self.pos_y))

            # print weapon to stall
            weapon_x = self.stall_x + self.stall_width // 2 - weapon.width // 2
            weapon_y = self.stall_y + self.stall_height // 2 - weapon.height // 2

            Screen.blit(weapon.surface, (weapon_x, weapon_y))

            # print buy and sell
            Screen.blit(pygame.font.Font.render(
                FontType.FONT3, 'BUY', True, Colors.BLACK), (self.buy_x + self.buy_width // 5, self.buy_y + self.buy_height // 5))
            Screen.blit(pygame.font.Font.render(
                FontType.FONT3, 'SELL', True, Colors.BLACK), (self.sell_x + self.sell_width // 5, self.sell_y + self.sell_height // 5))

            # money
            Screen.blit(pygame.font.Font.render(
                FontType.FONT3, 'Money: ', True, Colors.BLACK), (self.money_bar_x * 3 // 2, self.money_bar_y + self.money_bar_height // 3))
            Screen.blit(pygame.font.Font.render(
                FontType.FONT3, str(player.money), True, Colors.BLACK), (self.money_bar_x * 7 // 2, self.money_bar_y + self.money_bar_height // 3))
        pass

    def toggle(self):
        # Toggle Shop
        self.shopping = not self.shopping
        pass

    def trading(self, player, weapon):
        # Check Buy / Sell Mechanism
        (mouseX, mouseY) = pygame.mouse.get_pos()

        #buy
        if mouseX >= self.buy_x and mouseX <= self.buy_x + self.buy_width and mouseY >= self.buy_y and mouseY <= self.buy_y + self.buy_height:
            if player.money >= weapon.buy_price:
                self.buying = True
            else:
                self.buying = False

            if self.buying:
                player.money -= weapon.buy_price
                self.buying = False

        #sell
        if mouseX >= self.sell_x and mouseX <= self.sell_x + self.sell_width and mouseY >= self.sell_y and mouseY <= self.sell_y + self.sell_height:
            self.selling = True

            if self.selling:
                player.money += weapon.sell_price

    def update(self):
        pass
