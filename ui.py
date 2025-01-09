import pygame as pg
from globals import *


class Slider:
    def __init__(
        self,
        pos: tuple,
        width: int,
        height: int,
        min_val: int,
        max_val: int,
        title: str,
    ):
        self.pos = pos
        self.width = width
        self.height = height
        self.rect = pg.Rect(pos[0] - width / 2, pos[1] - height / 2, width, height)
        self.min = min_val
        self.max = max_val
        self.initial_val = (min_val + max_val) / 2
        self.knob_size = height * 1.3
        self.knob_bounding_box = pg.Rect(
            pos[0] - (self.knob_size / 2),
            pos[1] - (self.knob_size / 2),
            self.knob_size,
            self.knob_size,
        )
        self.value = 17
        self.title = title
        self.dragging = False

    def draw(self, screen):
        slider_desc = FONT.render(
            f"{self.title}: {self.value}", True, pg.Color(0, 0, 0)
        )
        screen.blit(
            slider_desc,
            (self.pos[0] - 0.5 * self.width, self.pos[1] - 1.5 * self.height),
        )
        pg.draw.rect(screen, pg.Color(255, 255, 255), self.rect)
        pg.draw.circle(
            screen,
            pg.Color(50, 50, 50),
            self.knob_bounding_box.center,
            self.knob_size / 2,
        )
        slider_min = FONT.render(str(self.min), True, pg.Color(0, 0, 0))
        screen.blit(
            slider_min,
            (self.pos[0] - 0.5 * self.width, self.pos[1] + 0.8 * self.height),
        )
        slider_max = FONT.render(str(self.max), True, pg.Color(0, 0, 0))
        screen.blit(
            slider_max,
            (self.pos[0] + 0.5 * self.width, self.pos[1] + 0.8 * self.height),
        )

    def update_value(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.knob_bounding_box.collidepoint(event.pos):
                self.dragging = True
        else:
            self.dragging = False

        if event.type == pg.MOUSEMOTION and self.dragging:
            mouse_x, _ = event.pos

            if mouse_x < self.pos[0] - 0.5 * self.width:
                setattr(self.knob_bounding_box, "left", self.pos[0] - self.width / 2)
                self.value = self.min
            elif mouse_x > self.pos[1] + 0.5 * self.width:
                setattr(self.knob_bounding_box, "left", self.pos[0] + self.width / 2)
                self.value = self.max
            else:
                setattr(self.knob_bounding_box, "left", mouse_x)
                self.value = mouse_x
