import kivy

kivy.require("1.11.1")
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class DistanceSection(BoxLayout):
    dist = ObjectProperty()
    distance_checkbox = ObjectProperty()

    def distance_string(self, distance: str) -> str:
        """Uses a template to create the distance from the GUI text input interface.

        Arguments:
            dist {str} -- string in the format '0.00'.

        Returns:
            str -- '0.00'
        """
        return "{}".format(distance)
