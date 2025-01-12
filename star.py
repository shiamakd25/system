import math
from ui import *


class Star:
    def __init__(self, color: tuple, slider_dict: dict[str, Slider]):
        self.mass = slider_dict["mass"].initial_val
        self.brightness = slider_dict["brightness"].initial_val
        self.display_mass = (8 * math.sqrt(3 * self.mass)) / 3 + 40
        self.display_brightness = self.display_mass + 1.4 * self.brightness + 10
        self.color = color

    def update_attr(self, slider_dict: dict[str, Slider]):
        self.mass = slider_dict["mass"].value
        self.display_mass = (8 * math.sqrt(3 * self.mass)) / 3 + 40
        self.brightness = slider_dict["brightness"].value
        self.display_brightness = self.display_mass + 1.4 * self.brightness + 10
