import pygame as pg
from star import *
from ui import *

pg.init()

SCREEN_INFO = pg.display.Info()
SCREEN_WIDTH = SCREEN_INFO.current_w
SCREEN_HEIGHT = SCREEN_INFO.current_h - 96

CONTROL_PANEL_WIDTH = 0.25 * SCREEN_WIDTH
CONTROL_PANEL_HEIGHT = SCREEN_HEIGHT

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Solar System")

control_panel = pg.Surface((CONTROL_PANEL_WIDTH, CONTROL_PANEL_HEIGHT))

mass_slider = Slider(
    (SCREEN_WIDTH - (CONTROL_PANEL_WIDTH / 2), 100), 225, 25, 15, 20, "Star Mass (M☉)"
)

star = Star((255, 228, 0))

run = True

while run:
    screen.fill((0, 0, 0))
    control_panel.fill((100, 100, 100))
    screen.blit(control_panel, (SCREEN_WIDTH - CONTROL_PANEL_WIDTH, 0))
    pg.draw.circle(
        screen,
        pg.Color(tuple(val * star.brightness / 100 for val in star.color)),
        (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
        40 * star.mass + star.brightness,
    )
    pg.draw.circle(
        screen,
        pg.Color(star.color),
        (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
        50 * star.mass,
    )
    mass_slider.draw(screen)
    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

pg.quit()
