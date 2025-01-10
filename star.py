import math


class Star:
    def __init__(self, color, slider_dict):
        self.mass = slider_dict["mass"].initial_val
        self.brightness = slider_dict["brightness"].initial_val
        self.display_mass = (8 * math.sqrt(3 * self.mass)) / 3 + 40
        self.display_brightness = self.brightness
        self.color = color

    def update_attr(self, slider_dict):
        self.mass = slider_dict["mass"].value
        self.brightness = slider_dict["brightness"].value
