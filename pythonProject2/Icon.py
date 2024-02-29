import pygame
import sys
import random


class First_lvl():

    def __init__(self, screen):
        self.screen = screen
        self.ip = 0
        self.ill = [
            [1, "Боль в горле", pygame.image.load("ill/Steve1.png")],
            [2, "Диарея", pygame.image.load("ill/Steve2.png")],
            [3, "Царапина", pygame.image.load("ill/Steve3.png")]
        ]
        random.shuffle(self.ill)
        self.B = 0
        self.C = []
        self.hill = 0
        self.heart = 3
        """инициализация Steve"""
        self.image_S = pygame.image.load("images/Steve.png")
        self.rect = self.image_S.get_rect()
        self.screen_rect = screen.get_rect()
        """инициализация medical_1"""
        self.image_M1 = pygame.image.load("images/jar.png")
        self.rect = self.image_M1.get_rect()
        self.screen_rect = screen.get_rect()

        """инициализация medical_2"""
        self.image_M2 = pygame.image.load("images/patch.png")
        self.rect = self.image_M2.get_rect()
        self.screen_rect = screen.get_rect()

        """инициализация medical_3"""
        self.image_M3 = pygame.image.load("images/tablet.png")
        self.rect = self.image_M3.get_rect()
        self.screen_rect = screen.get_rect()

        """инициализация Heart_1"""
        self.image_H1 = pygame.image.load("images/Heart_1.png")
        self.rect = self.image_H1.get_rect()
        self.screen_rect = screen.get_rect()
        self.image_H2 = pygame.image.load("images/Heart_2.png")
        self.rect = self.image_H1.get_rect()
        self.screen_rect = screen.get_rect()
        self.image_H3 = pygame.image.load("images/Heart_3.png")
        self.rect = self.image_H1.get_rect()
        self.screen_rect = screen.get_rect()
        self.hp = [self.image_H1, self.image_H2, self.image_H3]
        self.t = 0
        """инициализация Font"""
        self.font = pygame.font.Font(None, 36)

    def draw(self):
        """рисование medical_1"""
        self.screen.blit(self.image_M1, (600, 100))
        """рисование medical_2"""
        self.screen.blit(self.image_M2, (600, 260))
        """рисование medical_3"""
        self.screen.blit(self.image_M3, (600, 420))
        """рисование Font"""
        text1 = self.font.render("Афлубин", True, "Red")
        text2 = self.font.render("Пластырь", True, "Red")
        text3 = self.font.render("Таблетка от диареи", True, "Red")
        text_lvl = self.font.render("Первый уровень", True, "Red")
        self.screen.blit(text_lvl, (300, 0))
        self.screen.blit(text1, (600, 80))
        self.screen.blit(text2, (600, 240))
        self.screen.blit(text3, (550, 400))

    def heart_1(self):
        """рисование Heart_1"""
        if self.heart == 1 and self.t == "two":
            self.t = 0
        if self.heart == 3:
            self.screen.blit(self.image_H1, (210, 450))
            self.screen.blit(self.image_H1, (135, 450))
            self.screen.blit(self.image_H1, (60, 450))
        elif self.heart == 2 and self.t != "two":
            self.screen.blit(self.hp[self.t], (210, 450))
            self.screen.blit(self.image_H1, (135, 450))
            self.screen.blit(self.image_H1, (60, 450))
            self.t += 1
            if self.t == 3:
                self.t = "two"
        elif self.heart == 2 and self.t == "two":
            self.screen.blit(self.hp[2], (210, 450))
            self.screen.blit(self.image_H1, (135, 450))
            self.screen.blit(self.image_H1, (60, 450))
        elif self.heart == 1 and (self.t != "two" and self.t != "three"):
            self.screen.blit(self.hp[2], (210, 450))
            self.screen.blit(self.hp[self.t], (135, 450))
            self.screen.blit(self.image_H1, (60, 450))
            self.t += 1
            if self.t == 3:
                self.t = "three"
        elif self.heart == 1 and self.t == "three":
            self.screen.blit(self.hp[2], (210, 450))
            self.screen.blit(self.hp[2], (135, 450))
            self.screen.blit(self.image_H1, (60, 450))
        if self.heart == 0:
            pass

    def steve(self):
        """рисование Steve"""
        if self.B == 0 and len(self.ill) == 0:
            print(True)
        if self.B == 0:
            for i in self.ill:
                self.C = i
                self.B = 1
                self.ill.remove(i)
                break
        if self.B == 1:
            self.screen.blit(self.C[2], (80, 160))
            text_steve = self.font.render(self.C[1], True, "Red")
            self.screen.blit(text_steve, (380, 300))


    def game_play(self, pos):
        if 80 < pos[0] < 230 and 160 < pos[1] < 410:
            if self.hill == self.C[0]:
                self.B = 0
            else:
                self.heart -= 1


    def game(self, pos="", do=0):
        """Рисование обводок лекарств"""
        if do != 0:
            self.hill = self.ip
            self.ip = 0
        if pos == "":
            pos = [1000000000, 100000000]
        if (600 < pos[0] < 710) or self.ip != 0:
            if (100 < pos[1] < 210) or self.ip == 1:
                pygame.draw.rect(self.screen, "red", (600, 100, 110, 110), 5)
                self.ip = 1
                pygame.draw.rect(self.screen, "black", (600, 260, 110, 110), 5)
                pygame.draw.rect(self.screen, "black", (600, 420, 110, 110), 5)

            elif (260 < pos[1] < 370) or self.ip == 3:
                pygame.draw.rect(self.screen, "red", (600, 260, 110, 110), 5)
                self.ip = 3
                pygame.draw.rect(self.screen, "black", (600, 100, 110, 110), 5)
                pygame.draw.rect(self.screen, "black", (600, 420, 110, 110), 5)

            elif (420 < pos[1] < 530) or self.ip == 2:
                pygame.draw.rect(self.screen, "red", (600, 420, 110, 110), 5)
                self.ip = 2
                pygame.draw.rect(self.screen, "black", (600, 100, 110, 110), 5)
                pygame.draw.rect(self.screen, "black", (600, 260, 110, 110), 5)
        else:
            pygame.draw.rect(self.screen, "black", (600, 100, 110, 110), 5)
            pygame.draw.rect(self.screen, "black", (600, 260, 110, 110), 5)
            pygame.draw.rect(self.screen, "black", (600, 420, 110, 110), 5)
    def but(self, pos=0):
        pygame.draw.rect(self.screen, "blue", (50, 20, 60, 60), 5)
        if pos != 0:
            if (50 < pos[0] < 110) and (20 < pos[1] < 80):
                print(True)




class Second_lvl():

    def __init__(self, screen):
        self.screen = screen
        self.ip = 0
        self.ill = [
            [1, "Головная боль", pygame.image.load("ill/Steve4.png")],
            [2, "Вирус", pygame.image.load("ill/Steve5.png")],
            [3, "Кровотечение", pygame.image.load("ill/Steve6.png")]
        ]
        random.shuffle(self.ill)
        self.B = 0
        self.C = []
        self.hill = 0
        self.heart = 2
        """инициализация Steve"""
        self.image_S = pygame.image.load("images/Steve.png")
        self.rect = self.image_S.get_rect()
        self.screen_rect = screen.get_rect()
        """инициализация medical_1"""
        self.image_M1 = pygame.image.load("images/pill.png")
        self.rect = self.image_M1.get_rect()
        self.screen_rect = screen.get_rect()

        """инициализация medical_2"""
        self.image_M2 = pygame.image.load("images/syringe.png")
        self.rect = self.image_M2.get_rect()
        self.screen_rect = screen.get_rect()

        """инициализация medical_3"""
        self.image_M3 = pygame.image.load("images/kit.png")
        self.rect = self.image_M3.get_rect()
        self.screen_rect = screen.get_rect()

        """инициализация Heart_1"""
        self.image_H1 = pygame.image.load("images/Heart_1.png")
        self.rect = self.image_H1.get_rect()
        self.screen_rect = screen.get_rect()
        self.image_H2 = pygame.image.load("images/Heart_2.png")
        self.rect = self.image_H1.get_rect()
        self.screen_rect = screen.get_rect()
        self.image_H3 = pygame.image.load("images/Heart_3.png")
        self.rect = self.image_H1.get_rect()
        self.screen_rect = screen.get_rect()
        self.hp = [self.image_H1, self.image_H2, self.image_H3]
        self.t = 0
        """инициализация Font"""
        self.font = pygame.font.Font(None, 36)

    def draw(self):
        """рисование medical_1"""
        self.screen.blit(self.image_M1, (600, 100))
        """рисование medical_2"""
        self.screen.blit(self.image_M2, (600, 260))
        """рисование medical_3"""
        self.screen.blit(self.image_M3, (600, 420))
        """рисование Font"""
        text1 = self.font.render("Таблетка", True, "Red")
        text2 = self.font.render("Антидот", True, "Red")
        text3 = self.font.render("First aid kit", True, "Red")
        text_lvl = self.font.render("Второй уровень", True, "Red")
        self.screen.blit(text_lvl, (300, 0))
        self.screen.blit(text1, (600, 80))
        self.screen.blit(text2, (600, 240))
        self.screen.blit(text3, (590, 400))

    def heart_1(self):
        """рисование Heart_1"""
        if self.heart == 1 and self.t == "two":
            self.t = 0
        if self.heart == 2:
            self.screen.blit(self.image_H1, (165, 450))
            self.screen.blit(self.image_H1, (105, 450))
        elif self.heart == 1 and (self.t != "two" and self.t != "three"):
            self.screen.blit(self.hp[self.t], (165, 450))
            self.screen.blit(self.image_H1, (105, 450))
            self.t += 1
            if self.t == 3:
                self.t = "three"
        elif self.heart == 1 and self.t == "three":
            self.screen.blit(self.hp[2], (165, 450))
            self.screen.blit(self.image_H1, (105, 450))
        if self.heart == 0:
            pass

    def steve(self):
        """рисование Steve"""
        if len(self.ill) == 0:
            pass
        if self.B == 0:
            for i in self.ill:
                self.C = i
                self.B = 1
                self.ill.remove(i)
                break
        if self.B == 1:
            self.screen.blit(self.C[2], (80, 160))
            text_steve = self.font.render(self.C[1], True, "Red")
            self.screen.blit(text_steve, (380, 300))

    def game_play(self, pos):
        if 80 < pos[0] < 230 and 160 < pos[1] < 410:
            if self.hill == self.C[0]:
                self.B = 0
            else:
                self.heart -= 1

    def game(self, pos="", do=0):
        """Рисование обводок лекарств"""
        if do != 0:
            self.hill = self.ip
            self.ip = 0
        if pos == "":
            pos = [1000000000, 100000000]
        if (600 < pos[0] < 710) or self.ip != 0:
            if (100 < pos[1] < 210) or self.ip == 1:
                pygame.draw.rect(self.screen, "red", (600, 100, 110, 110), 5)
                self.ip = 1
                pygame.draw.rect(self.screen, "black", (600, 260, 110, 110), 5)
                pygame.draw.rect(self.screen, "black", (600, 420, 110, 110), 5)

            elif (260 < pos[1] < 370) or self.ip == 2:
                pygame.draw.rect(self.screen, "red", (600, 260, 110, 110), 5)
                self.ip = 2
                pygame.draw.rect(self.screen, "black", (600, 100, 110, 110), 5)
                pygame.draw.rect(self.screen, "black", (600, 420, 110, 110), 5)

            elif (420 < pos[1] < 530) or self.ip == 3:
                pygame.draw.rect(self.screen, "red", (600, 420, 110, 110), 5)
                self.ip = 3
                pygame.draw.rect(self.screen, "black", (600, 100, 110, 110), 5)
                pygame.draw.rect(self.screen, "black", (600, 260, 110, 110), 5)
        else:
            pygame.draw.rect(self.screen, "black", (600, 100, 110, 110), 5)
            pygame.draw.rect(self.screen, "black", (600, 260, 110, 110), 5)
            pygame.draw.rect(self.screen, "black", (600, 420, 110, 110), 5)
    def but(self, pos=0):
        pygame.draw.rect(self.screen, "blue", (50, 20, 60, 60), 5)
        if pos != 0:
            if (50 < pos[0] < 110) and (20 < pos[1] < 80):
                print(True)


class Third_lvl():

    def __init__(self, screen):
        self.screen = screen
        self.ip = 0
        self.ill = [
            [1, "Боль в горле", pygame.image.load("ill/Steve1.png")],
            [2, "Царапина", pygame.image.load("ill/Steve3.png")],
            [3, "КРЫСА!!!", pygame.image.load("ill/RAAT.png")]
        ]
        random.shuffle(self.ill)
        self.B = 0
        self.C = []
        self.hill = 0
        self.heart = 1
        """инициализация Steve"""
        self.image_S = pygame.image.load("images/Steve.png")
        self.rect = self.image_S.get_rect()
        self.screen_rect = screen.get_rect()
        """инициализация medical_1"""
        self.image_M1 = pygame.image.load("images/jar.png")
        self.rect = self.image_M1.get_rect()
        self.screen_rect = screen.get_rect()

        """инициализация medical_2"""
        self.image_M2 = pygame.image.load("images/kit.png")
        self.rect = self.image_M2.get_rect()
        self.screen_rect = screen.get_rect()

        """инициализация medical_3"""
        self.image_M3 = pygame.image.load("images/rat.png")
        self.rect = self.image_M3.get_rect()
        self.screen_rect = screen.get_rect()

        """инициализация Heart_1"""
        self.image_H1 = pygame.image.load("images/Heart_1.png")
        self.rect = self.image_H1.get_rect()
        self.screen_rect = screen.get_rect()
        self.image_H2 = pygame.image.load("images/Heart_2.png")
        self.rect = self.image_H1.get_rect()
        self.screen_rect = screen.get_rect()
        self.image_H3 = pygame.image.load("images/Heart_3.png")
        self.rect = self.image_H1.get_rect()
        self.screen_rect = screen.get_rect()
        self.hp = [self.image_H1, self.image_H2, self.image_H3]
        self.t = 0
        """инициализация Font"""
        self.font = pygame.font.Font(None, 36)

    def draw(self):
        """рисование medical_1"""
        self.screen.blit(self.image_M1, (600, 100))
        """рисование medical_2"""
        self.screen.blit(self.image_M2, (600, 260))
        """рисование medical_3"""
        self.screen.blit(self.image_M3, (600, 420))
        """рисование Font"""
        text1 = self.font.render("Таблетка", True, "Red")
        text2 = self.font.render("IFAK", True, "Red")
        text3 = self.font.render("?", True, "Red")
        text_lvl = self.font.render("Третий уровень", True, "Red")
        self.screen.blit(text_lvl, (300, 0))
        self.screen.blit(text1, (600, 80))
        self.screen.blit(text2, (625, 240))
        self.screen.blit(text3, (645, 400))

    def heart_1(self):
        """рисование Heart_1"""
        if self.heart == 1:
            self.screen.blit(self.image_H1, (135, 450))
        if self.heart == 0:
            pass

    def steve(self):
        """рисование Steve"""
        if len(self.ill) == 0:
            pass
        if self.B == 0:
            for i in self.ill:
                self.C = i
                self.B = 1
                self.ill.remove(i)
                break
        if self.B == 1:
            self.screen.blit(self.C[2], (80, 160))
            text_steve = self.font.render(self.C[1], True, "Red")
            self.screen.blit(text_steve, (380, 300))

    def game_play(self, pos):
        if 80 < pos[0] < 230 and 160 < pos[1] < 410:
            if self.hill == self.C[0]:
                self.B = 0
            else:
                self.heart -= 1

    def game(self, pos="", do=0):
        """Рисование обводок лекарств"""
        if do != 0:
            self.hill = self.ip
            self.ip = 0
        if pos == "":
            pos = [1000000000, 100000000]
        if (600 < pos[0] < 710) or self.ip != 0:
            if (100 < pos[1] < 210) or self.ip == 1:
                pygame.draw.rect(self.screen, "red", (600, 100, 110, 110), 5)
                self.ip = 1
                pygame.draw.rect(self.screen, "black", (600, 260, 110, 110), 5)
                pygame.draw.rect(self.screen, "black", (600, 420, 110, 110), 5)

            elif (260 < pos[1] < 370) or self.ip == 2:
                pygame.draw.rect(self.screen, "red", (600, 260, 110, 110), 5)
                self.ip = 2
                pygame.draw.rect(self.screen, "black", (600, 100, 110, 110), 5)
                pygame.draw.rect(self.screen, "black", (600, 420, 110, 110), 5)

            elif (420 < pos[1] < 530) or self.ip == 3:
                pygame.draw.rect(self.screen, "red", (600, 420, 110, 110), 5)
                self.ip = 3
                pygame.draw.rect(self.screen, "black", (600, 100, 110, 110), 5)
                pygame.draw.rect(self.screen, "black", (600, 260, 110, 110), 5)
        else:
            pygame.draw.rect(self.screen, "black", (600, 100, 110, 110), 5)
            pygame.draw.rect(self.screen, "black", (600, 260, 110, 110), 5)
            pygame.draw.rect(self.screen, "black", (600, 420, 110, 110), 5)
    def but(self, pos=0):
        pygame.draw.rect(self.screen, "blue", (50, 20, 60, 60), 5)
        if pos != 0:
            if (50 < pos[0] < 110) and (20 < pos[1] < 80):
                print(True)






