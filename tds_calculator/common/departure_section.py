import kivy

kivy.require("1.11.1")

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, DictProperty, ListProperty


class DepartureSection(BoxLayout):
    depature_checkbox = ObjectProperty()
    departure_dict = DictProperty()
    departure_list = ListProperty()
    items_list = ["self.year", "self.mon", "self.day", "self.hour", "self.mins"]

    def text_color(self):
        if self.departure_checkbox.state == "down":
            for items in self.items_list:
                eval(items).background_color = (0, 0, 1, 0.5)
        elif self.departure_checkbox.state == "normal":
            for items in self.items_list:
                eval(items).background_color = (1, 1, 1, 1)

    def text_disable(self):
        if self.departure_checkbox.state == "down":
            for items in self.items_list:
                eval(items).disabled = True
        elif self.departure_checkbox.state == "normal":
            for items in self.items_list:
                eval(items).disabled = False
