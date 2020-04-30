import kivy

kivy.require("1.11.1")
from kivy.config import Config

Config.set("modules", "screen", "ipad")  # droid2, onex, ipad, note2
Config.set("graphics", "width", "400")
Config.set("graphics", "height", "600")

from kivy.resources import resource_add_path
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from tds_calculator.common.buttons_section import Buttons

# class SpeedSection(BoxLayout):
#     spd = ObjectProperty()
#     speed_checkbox = ObjectProperty()


# class DistanceSection(BoxLayout):
#     dist = ObjectProperty()
#     distance_checkbox = ObjectProperty()


class TDSCalculator(BoxLayout):
    pass


class CalculatorApp(App):
    kivy.resources.resource_add_path("tds_calculator\\kv")

    def build(self):
        return TDSCalculator()


if __name__ == "__main__":
    CalculatorApp().run()
