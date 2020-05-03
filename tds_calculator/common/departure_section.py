import kivy

kivy.require("1.11.1")

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, DictProperty, ListProperty


class DepartureSection(BoxLayout):
    day = ObjectProperty()
    mon = ObjectProperty()
    year = ObjectProperty()
    hour = ObjectProperty()
    mins = ObjectProperty()
    tzsign = ObjectProperty()
    tzhour = ObjectProperty()
    tzmin = ObjectProperty()
    depature_checkbox = ObjectProperty()
    departure_dict = DictProperty()
    departure_list = ListProperty()

    def __init__(self, **kwargs):
        super(DepartureSection, self).__init__(**kwargs)
