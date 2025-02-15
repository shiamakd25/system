import math
from ui import *


class Planet:
    def __init__(self, color: tuple, slider_dict: dict[str, Slider]):
        self.mass = slider_dict["mass"].initial_val
        self.display_mass = (8 * math.sqrt(3 * self.mass)) / 3 + 40
        self.distance = slider_dict["distance"].initial_val
        self.color = color
        self.x, self.y = (
            DISPLAY_WIDTH / 2 + self.distance,
            DISPLAY_HEIGHT / 2 + self.distance,
        )

    def update_attr(self, slider_dict: dict[str, Slider]):
        self.mass = slider_dict["mass"].value
        self.display_mass = (8 * math.sqrt(3 * self.mass)) / 3 + 40
        self.distance = slider_dict["distance"].value

    def orbit(self, theta):
        theta = theta % (2 * math.pi)
        if theta < 2 * math.pi:
            x = math.cos(theta) * self.distance + DISPLAY_WIDTH / 2
            y = math.sin(theta) * self.distance + DISPLAY_HEIGHT / 2
            self.x = x
            self.y = y
        # else:
        #     theta = 0
