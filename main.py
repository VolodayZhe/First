import sys

import pygame

size = (850, 500)


class Button:
    def __init__(self, x, y, width, height, imagepath, text, hover_image_path=None, sound_path=None):
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
        font = pygame.font.Font('Far Cry Cyr Regular_0.ttf', size)
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
    rules_button = Button(299, 320, 203, 111, 'playbutton.png', 'RULES',
                             'playbutton_pressed.png')
    play_button = Button(299, 200, 203, 111, 'playbutton.png', 'NEW GAME',
                             'playbutton_pressed.png')
    while running:
        screen.fill((255, 255, 255))
        screen.blit(main_background, (-85, 0))
        font = pygame.font.Font('Far Cry Cyr Regular_0.ttf', 72)
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
    back_button = Button(299, 500, 200, 82, 'playbutton.png', 'BACK', 'playbutton_pressed.png')
    first_level = Button(299, 200, 144, 82, 'shortbutton.png', '1 level', 'shortbutton_pressed.png')
    second_level = Button(299, 300, 144, 82, 'shortbutton.png', '2 level', 'shortbutton_pressed.png')
    third_level = Button(299, 400, 144, 82, 'shortbutton.png', '3 level', 'shortbutton_pressed.png')
    running = True
    while running:
        screen.fill('White')
        screen.blit(main_background, (-85, 0))
        font = pygame.font.Font('Far Cry Cyr Regular_0.ttf', 72)
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
                pass #подключить к игре
            if event.type == pygame.USEREVENT and event.button == second_level:
                pass #подключить к игре
            if event.type == pygame.USEREVENT and event.button == third_level:
                pass #подключить к игре
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
    back_button = Button(299, 500, 200, 82, 'playbutton.png', 'BACK', 'playbutton_pressed.png')
    running = True
    while running:
        screen.fill('White')
        screen.blit(main_background, (-85, 0))
        font = pygame.font.Font('Far Cry Cyr Regular_0.ttf', 72)
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
def win():
    back_button = Button(299, 500, 200, 82, 'playbutton.png', 'BACK', 'playbutton_pressed.png')
    running = True
    while running:
        screen.fill('White')
        screen.blit(main_background, (-85, 0))
        font = pygame.font.Font('Far Cry Cyr Regular_0.ttf', 72)
        text_surface = font.render("YOU WIN!", True, (255, 0, 0))
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
def rule():
    back_button = Button(299, 500, 200, 82, 'playbutton.png', 'BACK', 'playbutton_pressed.png')
    running = True
    while running:
        screen.fill('White')
        screen.blit(main_background, (-85, 0))
        font = pygame.font.Font('Far Cry Cyr Regular_0.ttf', 50)
        text_surface = font.render("RULES ARE IN FILE 'RULES'", True, (255, 0, 0))
        text_rect = text_surface.get_rect(center=(400, 50))
        screen.blit(text_surface, text_rect)
        clown = pygame.image.load('clown.jpg')
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

pygame.init()
main_background = pygame.image.load('fon.jpg')
width, height = 800, 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("doctor")

main_menu()
