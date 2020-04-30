import kivy

kivy.require("1.11.1")

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, DictProperty


class DepartureSection(BoxLayout):
    dep_day = ObjectProperty()
    dep_mon = ObjectProperty()
    dep_year = ObjectProperty()
    dep_hour = ObjectProperty()
    dep_min = ObjectProperty()
    dep_tzsign = ObjectProperty()
    dep_tzhour = ObjectProperty()
    dep_tzmin = ObjectProperty()
    depature_checkbox = ObjectProperty()
    departure_dict = DictProperty()
