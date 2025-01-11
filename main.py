import pygame as pg
from globals import *
from star import *
from planet import *
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

p_mass_slider = Slider(
    (SCREEN_WIDTH - (CONTROL_PANEL_WIDTH / 2), 280),
    SLIDER_WIDTH,
    SLIDER_HEIGHT,
    1,
    300,
    "Planet Mass",
)

p_dist_slider = Slider(
    (SCREEN_WIDTH - (CONTROL_PANEL_WIDTH / 2), 370),
    SLIDER_WIDTH,
    SLIDER_HEIGHT,
    0,
    100,
    "Distance from Star",
)

star_slider_dict = {"mass": mass_slider, "brightness": brightness_slider}
star = Star((255, 228, 0), star_slider_dict)

planet_slider_dict = {"mass": p_mass_slider, "distance": p_dist_slider}
planet = Planet((255, 0, 225), planet_slider_dict)

run = True

while run:
    screen.fill((0, 0, 0))
    pg.draw.circle(
        screen,
        pg.Color(tuple(val * star.brightness / 350 for val in star.color)),
        (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2),
        star.display_mass + 1.4 * star.brightness + 10,
    )
    pg.draw.circle(
        screen,
        pg.Color(star.color),
        (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2),
        star.display_mass,
    )
    pg.draw.circle(
        screen,
        pg.Color(planet.color),
        (DISPLAY_WIDTH / 2 + planet.distance, DISPLAY_HEIGHT / 2 + planet.distance),
        planet.display_mass,
    )
    control_panel.fill((100, 100, 100))
    screen.blit(control_panel, (SCREEN_WIDTH - CONTROL_PANEL_WIDTH, 0))
    mass_slider.draw(screen)
    brightness_slider.draw(screen)
    p_mass_slider.draw(screen)
    p_dist_slider.draw(screen)

    star.update_attr(star_slider_dict)
    planet.update_attr(planet_slider_dict)

    for event in pg.event.get():
        mass_slider.update_value(event)
        brightness_slider.update_value(event)
        p_mass_slider.update_value(event)
        p_dist_slider.update_value(event)
        if event.type == pg.QUIT:
            run = False

    pg.display.flip()


pg.quit()
