import kivy

kivy.require("1.11.1")
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class DistanceSection(BoxLayout):
    dist = ObjectProperty()
    distance_checkbox = ObjectProperty()

    def text_color(self):
        if self.distance_checkbox.state == "down":
            self.dist.background_color = (0, 0, 1, 0.5)
        elif self.distance_checkbox.state == "normal":
            self.dist.background_color = (1, 1, 1, 1)

    def text_disable(self):
        if self.distance_checkbox.state == "down":
            self.dist.disabled = True
        elif self.distance_checkbox.state == "normal":
            self.dist.disabled = False
