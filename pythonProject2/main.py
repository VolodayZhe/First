import sys
import pygame
import random

image_path = "/data/data/com.voloday.mygame/files/app/"

def play(num):
    run = True
    if num == 1:
        lvl = First_lvl(screen)
    elif num == 2:
        lvl = Second_lvl(screen)
    elif num == 3:
        lvl = Third_lvl(screen)
    while run:
        screen.fill(pg_color)
        lvl.draw()
        lvl.game()
        lvl.steve()
        lvl.heart_1()
        lvl.but()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                pos = [xm, ym]
                do = 1
                lvl.game(pos, do)
                lvl.game_play(pos)
                lvl.but(pos)

        pygame.display.flip()
        clock.tick(15)


class Button:
    def __init__(self, x, y, width, height, imagepath, text, hover_image_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        self.image = pygame.image.load(imagepath)
        self.image = pygame.transform.scale(self.image, (width, height))
        if hover_image_path:
            self.hover_image = pygame.image.load(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.is_hovered = False

    def draw(self, screen, size):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)
        font = pygame.font.Font(image_path + 'Far Cry Cyr Regular_0.ttf', size)
        text_surface = font.render(self.text, True, (128, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))


def main_menu():
    running = True
    rules_button = Button(299, 320, 203, 111, image_path + 'playbutton.png', 'RULES',
                          image_path + 'playbutton_pressed.png')
    play_button = Button(299, 200, 203, 111, image_path + 'playbutton.png', 'NEW GAME',
                         image_path + 'playbutton_pressed.png')
    while running:
        screen.fill((255, 255, 255))
        screen.blit(main_background, (-85, 0))
        font = pygame.font.Font(image_path + 'Far Cry Cyr Regular_0.ttf', 72)
        text_surface = font.render("DOCTOR", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(400, 50))
        screen.blit(text_surface, text_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            play_button.handle_event(event)
            rules_button.handle_event(event)
            if event.type == pygame.USEREVENT and event.button == play_button:
                level_select()
            if event.type == pygame.USEREVENT and event.button == rules_button:
                rule()
        play_button.check_hover(pygame.mouse.get_pos())
        play_button.draw(screen, 30)
        rules_button.check_hover(pygame.mouse.get_pos())
        rules_button.draw(screen, 30)
        pygame.display.flip()


def level_select():
    back_button = Button(299, 500, 200, 82, image_path + 'playbutton.png', 'BACK', image_path + 'playbutton_pressed.png')
    first_level = Button(299, 200, 144, 82, image_path + 'shortbutton.png', '1 level', image_path + 'shortbutton_pressed.png')
    second_level = Button(299, 300, 144, 82, image_path + 'shortbutton.png', '2 level', image_path + 'shortbutton_pressed.png')
    third_level = Button(299, 400, 144, 82, image_path + 'shortbutton.png', '3 level', image_path + 'shortbutton_pressed.png')
    running = True
    while running:
        screen.fill('White')
        screen.blit(main_background, (-85, 0))
        font = pygame.font.Font(image_path + 'Far Cry Cyr Regular_0.ttf', 72)
        text_surface = font.render("SELECT LEVEL", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(400, 50))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            back_button.handle_event(event)
            first_level.handle_event(event)
            second_level.handle_event(event)
            third_level.handle_event(event)
            if event.type == pygame.USEREVENT and event.button == first_level:
                play(1)
            if event.type == pygame.USEREVENT and event.button == second_level:
                play(2)
            if event.type == pygame.USEREVENT and event.button == third_level:
                play(3)
            if event.type == pygame.USEREVENT and event.button == back_button:
                main_menu()
        first_level.check_hover(pygame.mouse.get_pos())
        first_level.draw(screen, 30)
        second_level.check_hover(pygame.mouse.get_pos())
        second_level.draw(screen, 30)
        third_level.check_hover(pygame.mouse.get_pos())
        third_level.draw(screen, 30)
        back_button.check_hover(pygame.mouse.get_pos())
        back_button.draw(screen, 30)
        pygame.display.flip()


def ggs():
    back_button = Button(299, 500, 200, 82, image_path + 'playbutton.png', 'BACK', image_path + 'playbutton_pressed.png')
    running = True
    while running:
        screen.fill('White')
        screen.blit(main_background, (-85, 0))
        font = pygame.font.Font(image_path + 'Far Cry Cyr Regular_0.ttf', 72)
        text_surface = font.render("GAME OVER", True, (255, 0, 0))
        text_rect = text_surface.get_rect(center=(400, 50))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            back_button.handle_event(event)
            if event.type == pygame.USEREVENT and event.button == back_button:
                main_menu()
        back_button.check_hover(pygame.mouse.get_pos())
        back_button.draw(screen, 30)
        pygame.display.flip()


def win(heart=None):
    back_button = Button(299, 500, 200, 82, image_path + 'playbutton.png', 'BACK', image_path + 'playbutton_pressed.png')
    running = True
    while running:
        screen.fill('White')
        screen.blit(main_background, (-85, 0))
        font = pygame.font.Font(image_path + 'Far Cry Cyr Regular_0.ttf', 72)
        text_surface = font.render("YOU WIN!", True, (255, 0, 0))
        text_rect = text_surface.get_rect(center=(400, 50))
        screen.blit(text_surface, text_rect)
        text_surface = font.render(f"Hearts left: {heart}", True, (255, 0, 0))
        text_rect = text_surface.get_rect(center=(400, 200))
        screen.blit(text_surface, text_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            back_button.handle_event(event)
            if event.type == pygame.USEREVENT and event.button == back_button:
                main_menu()
        back_button.check_hover(pygame.mouse.get_pos())
        back_button.draw(screen, 30)
        pygame.display.flip()


def rule():
    back_button = Button(299, 500, 200, 82, image_path + 'playbutton.png', 'BACK', image_path + 'playbutton_pressed.png')
    running = True
    txt = []
    H = 1
    ttt = 0
    while running:
        screen.fill('White')
        screen.blit(main_background, (-85, 0))
        font = pygame.font.Font(image_path + 'Far Cry Cyr Regular_0.ttf', 50)
        text_surface = font.render("Rules in file 'RULES'", True, (255, 0, 0))
        text_rect = text_surface.get_rect(center=(400, 50))

        with open('rules.txt', 'r', encoding='utf-8') as tekst:
            data = tekst.read()
            for line in data.splitlines():
                if line not in txt:
                    txt.append(line)
                    H = 0
            if H == 0:
                for jey in txt:
                    font1 = pygame.font.Font(image_path + 'Far Cry Cyr Regular_0.ttf', 15)
                    text_surface1 = font1.render(jey, True, (255, 0, 0))
                    screen.blit(text_surface1, (25, 251 + ttt))
                    ttt += 20
                ttt = 0

        screen.blit(text_surface, text_rect)
        clown = pygame.image.load(image_path + 'clown.jpg')
        screen.blit(clown, [299, 150])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            back_button.handle_event(event)
            if event.type == pygame.USEREVENT and event.button == back_button:
                main_menu()
        back_button.check_hover(pygame.mouse.get_pos())
        back_button.draw(screen, 30)
        pygame.display.flip()


class First_lvl():
    def __init__(self, screen):
        self.screen = screen
        self.ip = 0
        self.ill = [
            [1, "Боль в горле", pygame.image.load(image_path + "ill/Steve1.png")],
            [2, "Диарея", pygame.image.load(image_path + "ill/Steve2.png")],
            [3, "Царапина", pygame.image.load(image_path + "ill/Steve3.png")]
        ]
        random.shuffle(self.ill)
        self.B = 0
        self.C = []
        self.hill = 0
        self.heart = 3
        """инициализация Steve"""
        self.image_S = pygame.image.load(image_path + "images/Steve.png")
        self.rect = self.image_S.get_rect()
        self.screen_rect = screen.get_rect()
        """инициализация medical_1"""
        self.image_M1 = pygame.image.load(image_path + "images/jar.png")
        self.rect = self.image_M1.get_rect()
        self.screen_rect = screen.get_rect()

        """инициализация medical_2"""
        self.image_M2 = pygame.image.load(image_path + "images/patch.png")
        self.rect = self.image_M2.get_rect()
        self.screen_rect = screen.get_rect()

        """инициализация medical_3"""
        self.image_M3 = pygame.image.load(image_path + "images/tablet.png")
        self.rect = self.image_M3.get_rect()
        self.screen_rect = screen.get_rect()

        """инициализация Heart_1"""
        self.image_H1 = pygame.image.load(image_path + "images/Heart_1.png")
        self.rect = self.image_H1.get_rect()
        self.screen_rect = screen.get_rect()
        self.image_H2 = pygame.image.load(image_path + "images/Heart_2.png")
        self.rect = self.image_H1.get_rect()
        self.screen_rect = screen.get_rect()
        self.image_H3 = pygame.image.load(image_path + "images/Heart_3.png")
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
            ggs()

    def steve(self):
        """рисование Steve"""
        if len(self.ill) == 0 and self.B == 0:
            win(self.heart)
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
        back_button = Button(50, 20, 200, 82, image_path + 'playbutton.png', 'BACK', image_path + 'playbutton_pressed.png')
        back_button.check_hover(pygame.mouse.get_pos())
        back_button.draw(screen, 30)
        if pos != 0:
            if (50 < pos[0] < 250) and (20 < pos[1] < 100):
                level_select()


class Second_lvl():

    def __init__(self, screen):
        self.screen = screen
        self.ip = 0
        self.ill = [
            [1, "Головная боль", pygame.image.load(image_path + "ill/Steve4.png")],
            [2, "Вирус", pygame.image.load(image_path + "ill/Steve5.png")],
            [3, "Кровотечение", pygame.image.load(image_path + "ill/Steve6.png")]
        ]
        random.shuffle(self.ill)
        self.B = 0
        self.C = []
        self.hill = 0
        self.heart = 2
        """инициализация Steve"""
        self.image_S = pygame.image.load(image_path + "images/Steve.png")
        self.rect = self.image_S.get_rect()
        self.screen_rect = screen.get_rect()
        """инициализация medical_1"""
        self.image_M1 = pygame.image.load(image_path + "images/pill.png")
        self.rect = self.image_M1.get_rect()
        self.screen_rect = screen.get_rect()

        """инициализация medical_2"""
        self.image_M2 = pygame.image.load(image_path + "images/syringe.png")
        self.rect = self.image_M2.get_rect()
        self.screen_rect = screen.get_rect()

        """инициализация medical_3"""
        self.image_M3 = pygame.image.load(image_path + "images/kit.png")
        self.rect = self.image_M3.get_rect()
        self.screen_rect = screen.get_rect()

        """инициализация Heart_1"""
        self.image_H1 = pygame.image.load(image_path + "images/Heart_1.png")
        self.rect = self.image_H1.get_rect()
        self.screen_rect = screen.get_rect()
        self.image_H2 = pygame.image.load(image_path + "images/Heart_2.png")
        self.rect = self.image_H1.get_rect()
        self.screen_rect = screen.get_rect()
        self.image_H3 = pygame.image.load(image_path + "images/Heart_3.png")
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
            ggs()

    def steve(self):
        """рисование Steve"""
        if len(self.ill) == 0 and self.B == 0:
            win(self.heart)
        if len(self.ill) == 0 and self.B == 0:
            win()
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
        back_button = Button(50, 20, 200, 82, image_path + 'playbutton.png', 'BACK', image_path + 'playbutton_pressed.png')
        back_button.check_hover(pygame.mouse.get_pos())
        back_button.draw(screen, 30)
        if pos != 0:
            if (50 < pos[0] < 250) and (20 < pos[1] < 100):
                level_select()


class Third_lvl():

    def __init__(self, screen):
        self.screen = screen
        self.ip = 0
        self.ill = [
            [1, "Боль в горле", pygame.image.load(image_path + "ill/Steve1.png")],
            [2, "Царапина", pygame.image.load(image_path + "ill/Steve3.png")],
            [3, "КРЫСА!!!", pygame.image.load(image_path + "ill/RAAT.png")]
        ]
        random.shuffle(self.ill)
        self.B = 0
        self.C = []
        self.hill = 0
        self.heart = 1
        """инициализация Steve"""
        self.image_S = pygame.image.load(image_path + "images/Steve.png")
        self.rect = self.image_S.get_rect()
        self.screen_rect = screen.get_rect()
        """инициализация medical_1"""
        self.image_M1 = pygame.image.load(image_path + "images/jar.png")
        self.rect = self.image_M1.get_rect()
        self.screen_rect = screen.get_rect()

        """инициализация medical_2"""
        self.image_M2 = pygame.image.load(image_path + "images/kit.png")
        self.rect = self.image_M2.get_rect()
        self.screen_rect = screen.get_rect()

        """инициализация medical_3"""
        self.image_M3 = pygame.image.load(image_path + "images/rat.png")
        self.rect = self.image_M3.get_rect()
        self.screen_rect = screen.get_rect()

        """инициализация Heart_1"""
        self.image_H1 = pygame.image.load(image_path + "images/Heart_1.png")
        self.rect = self.image_H1.get_rect()
        self.screen_rect = screen.get_rect()
        self.image_H2 = pygame.image.load(image_path + "images/Heart_2.png")
        self.rect = self.image_H1.get_rect()
        self.screen_rect = screen.get_rect()
        self.image_H3 = pygame.image.load(image_path + "images/Heart_3.png")
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
            ggs()

    def steve(self):
        """рисование Steve"""
        if len(self.ill) == 0 and self.B == 0:
            win(self.heart)
        if len(self.ill) == 0 and self.B == 0:
            win()
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
        back_button = Button(50, 20, 200, 82, image_path + 'playbutton.png', 'BACK', image_path + 'playbutton_pressed.png')
        back_button.check_hover(pygame.mouse.get_pos())
        back_button.draw(screen, 30)
        if pos != 0:
            if (50 < pos[0] < 250) and (20 < pos[1] < 100):
                level_select()




pygame.init()
size = (850, 500)
clock = pygame.time.Clock()
pg_color = (160, 160, 160)
main_background = pygame.image.load(image_path + 'fon.jpg')
width, height = 800, 600
pygame.mixer.music.load(image_path + 'ЧипиЧипи.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.05)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Doctor")

main_menu()