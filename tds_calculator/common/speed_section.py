import kivy

kivy.require("1.11.1")
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class SpeedSection(BoxLayout):
    spd = ObjectProperty()
    speed_checkbox = ObjectProperty()

    def speed_string(self, speed: str) -> str:
        """Uses a template to create the speed from the GUI text input interface.

        Arguments:
            spd {str} -- string in the format '0.00'.

        Returns:
            str -- '0.00'
        """
        # spd = self.spd.text

        return "{}".format(speed)
