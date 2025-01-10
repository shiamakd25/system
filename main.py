import pygame as pg
from globals import *
from star import *
from ui import *
import math

pg.init()


screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Solar System")

control_panel = pg.Surface((CONTROL_PANEL_WIDTH, CONTROL_PANEL_HEIGHT))

mass_slider = Slider(
    (SCREEN_WIDTH - (CONTROL_PANEL_WIDTH / 2), 100),
    SLIDER_WIDTH,
    SLIDER_HEIGHT,
    1,
    300,
    "Star Mass (Solar Mass)",
)

brightness_slider = Slider(
    (SCREEN_WIDTH - (CONTROL_PANEL_WIDTH / 2), 190),
    SLIDER_WIDTH,
    SLIDER_HEIGHT,
    0,
    100,
    "Star Brightness (%)",
)

slider_dict = {"mass": mass_slider, "brightness": brightness_slider}
star = Star((255, 228, 0), slider_dict)

run = True

while run:
    screen.fill((0, 0, 0))
    pg.draw.circle(
        screen,
        pg.Color(tuple(val * star.brightness / 350 for val in star.color)),
        (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2),
        4 * star.mass + star.brightness,
    )
    pg.draw.circle(
        screen,
        pg.Color(star.color),
        (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2),
        star.display_mass,
    )
    control_panel.fill((100, 100, 100))
    screen.blit(control_panel, (SCREEN_WIDTH - CONTROL_PANEL_WIDTH, 0))
    mass_slider.draw(screen)
    brightness_slider.draw(screen)

    star.update_attr(slider_dict)

    for event in pg.event.get():
        mass_slider.update_value(event)
        brightness_slider.update_value(event)
        if event.type == pg.QUIT:
            run = False

    pg.display.flip()


pg.quit()
