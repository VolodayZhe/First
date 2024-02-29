import pygame
import sys
from Icon import First_lvl
from Icon import Second_lvl
from Icon import Third_lvl

clock = pygame.time.Clock()
pg_color = (160, 160, 160)
screen = pygame.display.set_mode((800, 600))
pygame.init()
pygame.display.set_caption("Doctors")
num = 1
def play(num):
    run = True
    if num == 1:
        lvl = First_lvl(screen)
    elif num == 2:
        lvl = First_lvl(screen)
    elif num == 3:
        lvl = First_lvl(screen)
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
play(num)