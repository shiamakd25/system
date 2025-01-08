import pygame as pg


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
        self.title = title

    def draw(self, screen):
        pg.draw.rect(screen, pg.Color(255, 255, 255), self.rect)
        pg.draw.circle(
            screen,
            pg.Color(50, 50, 50),
            self.knob_bounding_box.center,
            self.knob_size / 2,
        )
