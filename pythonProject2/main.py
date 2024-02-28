import pygame as pg
import sys
from Icon import First_lvl


def play():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Doctors")
    pg_color = (160, 160, 160)
    run = True
    level = First_lvl(screen)

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        screen.fill(pg_color)
        level.output_S()
        level.output_M1()
        level.output_M2()
        level.output_M3()
        level.output_H1()
        pg.draw.rect(screen, "black",
                         (600, 100, 110, 110), 5)
        pg.draw.rect(screen, "black",
                     (600, 260, 110, 110), 5)
        pg.draw.rect(screen, "black",
                     (600, 420, 110, 110), 5)
        level.output_F()

        pg.display.flip()
play()