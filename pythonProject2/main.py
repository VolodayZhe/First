import pygame as pg
import sys
from Icon import First_lvl


def play():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Doctors")
    pg_color = (160, 160, 160)
    run = True
    steve = First_lvl(screen)
    med1 = First_lvl(screen)
    med2 = First_lvl(screen)
    med3 = First_lvl(screen)
    heart1 = First_lvl(screen)
    txt1 = First_lvl(screen)

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        screen.fill(pg_color)
        steve.output_S()
        med1.output_M1()
        med2.output_M2()
        med3.output_M3()
        heart1.output_H1()
        pg.draw.rect(screen, "black",
                         (600, 100, 110, 110), 5)
        pg.draw.rect(screen, "black",
                     (600, 260, 110, 110), 5)
        pg.draw.rect(screen, "black",
                     (600, 420, 110, 110), 5)
        txt1.output_F()

        pg.display.flip()

play()