import kivy

kivy.require("1.11.1")
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import ObjectProperty


class PopMessage(Popup):
    pop_label = ObjectProperty()

    def show_popup(self, value):
        popmessage = PopMessage()
        popmessage.pop_label.text = f"{value}"
        popmessage.open()
        # popmessage = Popup(
        #     title_align="center",
        #     title_size="18sp",
        #     title_color=(0, 0, 0, 1),
        #     title="Error Warning",
        #     background="tds_calculator\\img\\grey.png",
        #     content=Label(
        #         font_size="18sp",
        #         halign="center",
        #         valign="middle",
        #         color=(0, 0, 0, 1),
        #         text="{}".format(value),
        #     ),
        #     size_hint=(0.7, 0.3),
        # )
        # popmessage.open()
