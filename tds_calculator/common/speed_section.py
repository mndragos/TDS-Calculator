import kivy

kivy.require("1.11.1")
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class SpeedSection(BoxLayout):
    spd = ObjectProperty()
    speed_checkbox = ObjectProperty()

    def text_color(self):
        if self.speed_checkbox.state == "down":
            self.spd.background_color = (0, 0, 1, 0.5)
        elif self.speed_checkbox.state == "normal":
            self.spd.background_color = (1, 1, 1, 1)

    def text_disable(self):
        if self.speed_checkbox.state == "down":
            self.spd.disabled = True
        elif self.speed_checkbox.state == "normal":
            self.spd.disabled = False
