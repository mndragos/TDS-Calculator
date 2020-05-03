import kivy

kivy.require("1.11.1")

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, DictProperty, ListProperty


class ArrivalSection(BoxLayout):
    year = ObjectProperty()
    mon = ObjectProperty()
    day = ObjectProperty()
    hour = ObjectProperty()
    mins = ObjectProperty()
    tzsign = ObjectProperty()
    tzhour = ObjectProperty()
    tzmin = ObjectProperty()
    arrival_checkbox = ObjectProperty()
    arrival_dict = DictProperty()
