import kivy

kivy.require("1.11.1")

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, DictProperty, ListProperty


class ArrivalSection(BoxLayout):
    arr_year = ObjectProperty()
    arr_mon = ObjectProperty()
    arr_day = ObjectProperty()
    arr_hour = ObjectProperty()
    arr_min = ObjectProperty()
    arr_tzsign = ObjectProperty()
    arr_tzhour = ObjectProperty()
    arr_tzmin = ObjectProperty()
    arrival_checkbox = ObjectProperty()
    arrival_dict = DictProperty()
