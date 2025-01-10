class Star:
    def __init__(self, color, slider_dict):
        self.mass = slider_dict["mass"].initial_val
        self.brightness = slider_dict["brightness"].initial_val
        self.color = color

    def update_attr(self, slider_dict):
        self.mass = slider_dict["mass"].value
        self.brightness = slider_dict["brightness"].value
