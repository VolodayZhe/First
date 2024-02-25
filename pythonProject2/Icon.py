import pygame as pg
import sys

class First_lvl():

    def __init__(self, screen):
        self.screen = screen
        """инициализация Steve"""
        self.image_S = pg.image.load("images/Steve.png")
        self.rect = self.image_S.get_rect()
        self.screen_rect = screen.get_rect()
        # self.rect.centerx = self.screen_rect.centerx
        # self.rect.bottom = self.screen_rect.bottom
        """инициализация medical_1"""
        self.image_M1 = pg.image.load("images/jar.png")
        self.rect = self.image_M1.get_rect()
        self.screen_rect = screen.get_rect()
        """инициализация medical_2"""
        self.image_M2 = pg.image.load("images/patch.png")
        self.rect = self.image_M2.get_rect()
        self.screen_rect = screen.get_rect()
        """инициализация medical_3"""
        self.image_M3 = pg.image.load("images/tablet.png")
        self.rect = self.image_M3.get_rect()
        self.screen_rect = screen.get_rect()
        """инициализация Heart_1"""
        self.image_H1 = pg.image.load("images/Heart_1.png")
        self.rect = self.image_H1.get_rect()
        self.screen_rect = screen.get_rect()
        """инициализация Font"""
        self.font = pg.font.Font(None, 36)

    def output_S(self):
        """рисование Steve"""
        self.screen.blit(self.image_S, (80, 160))

    def output_M1(self):
        """рисование medical_1"""
        self.screen.blit(self.image_M1, (600, 100))

    def output_M2(self):
        """рисование medical_2"""
        self.screen.blit(self.image_M2, (600, 260))

    def output_M3(self):
        """рисование medical_3"""
        self.screen.blit(self.image_M3, (600, 420))

    def output_H1(self):
        """рисование Heart_1"""
        self.screen.blit(self.image_H1, (60, 450))
        self.screen.blit(self.image_H1, (135, 450))
        self.screen.blit(self.image_H1, (210, 450))
    def output_F(self):
        """рисование medical_3"""
        self.text1 = self.font.render("Афлубин", True, "Red")
        self.text2 = self.font.render("Пластырь", True, "Red")
        self.text3 = self.font.render("Таблетка от диареи", True, "Red")
        self.text_lvl = self.font.render("Первый уровень", True, "Red")
        self.screen.blit(self.text_lvl, (300, 0))
        self.screen.blit(self.text1, (600, 80))
        self.screen.blit(self.text2, (600, 240))
        self.screen.blit(self.text3, (550, 400))






