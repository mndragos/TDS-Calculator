import kivy

kivy.require("1.11.1")

from tds_calculator.common.pop_message import PopMessage


class ErrorMessage(Exception):
    message = PopMessage()

    def on_error(self, value):
        self.message.show_popup(value)
