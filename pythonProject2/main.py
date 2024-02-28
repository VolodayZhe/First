import pygame as pg
import sys
from Icon import First_lvl
from Icon import Second_lvl
from Icon import Third_lvl

clock = pg.time.Clock()


def play():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Doctors")
    pg_color = (160, 160, 160)
    run = True
    lvl = Third_lvl(screen)
    while run:
        screen.fill(pg_color)
        lvl.draw()
        lvl.game()
        lvl.steve()
        lvl.heart_1()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                xm, ym = pg.mouse.get_pos()
                pos = [xm, ym]
                do = 1
                lvl.game(pos, do)
                lvl.game_play(pos)


        pg.display.flip()
        clock.tick(15)
play()