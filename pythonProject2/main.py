import pygame as pg
import sys
from Icon import First_lvl

clock = pg.time.Clock()


def play():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Doctors")
    pg_color = (160, 160, 160)
    run = True
    lvl = First_lvl(screen)
    # steve_timer = pg.USEREVENT + 1
    # pg.time.set_timer(steve_timer, 1000000)
    eve = 0
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