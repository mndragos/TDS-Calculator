import kivy

kivy.require("1.11.1")

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, DictProperty


class ArrivalSection(BoxLayout):
    arrival_checkbox = ObjectProperty()
    arrival_dict = DictProperty()
    items_list = ["self.year", "self.mon", "self.day", "self.hour", "self.mins"]

    def text_color(self):
        if self.arrival_checkbox.state == "down":
            for items in self.items_list:
                eval(items).background_color = (0, 0, 1, 0.5)
        elif self.arrival_checkbox.state == "normal":
            for items in self.items_list:
                eval(items).background_color = (1, 1, 1, 1)

    def text_disable(self):
        if self.arrival_checkbox.state == "down":
            for items in self.items_list:
                eval(items).disabled = True
        elif self.arrival_checkbox.state == "normal":
            for items in self.items_list:
                eval(items).disabled = False
