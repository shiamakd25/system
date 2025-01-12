import math
from ui import *


class Planet:
    def __init__(self, color: tuple, slider_dict: dict[str, Slider]):
        self.mass = slider_dict["mass"].initial_val
        self.display_mass = (8 * math.sqrt(3 * self.mass)) / 3 + 40
        self.distance = slider_dict["distance"].initial_val
        self.color = color

    def update_attr(self, slider_dict: dict[str, Slider]):
        self.mass = slider_dict["mass"].value
        self.display_mass = (8 * math.sqrt(3 * self.mass)) / 3 + 40
        self.distance = slider_dict["distance"].value
