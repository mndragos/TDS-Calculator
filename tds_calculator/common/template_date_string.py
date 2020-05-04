from datetime import datetime, timedelta


class TemplateDateString:
    def __init__(self, date_dict):
        self.date_dict = date_dict
        self.string_datetime = None

    @property
    def string_datetime(self):
        return self.__string_datetime

    @string_datetime.setter
    def string_datetime(self, to_datetime):
        date_string = self._date_dict(self.date_dict)
        to_datetime = datetime.strptime(date_string, "%Y-%m-%d %H:%M %z")
        self.__string_datetime = to_datetime

    def _date_dict(self, date_dict):
        return "{year}-{mon}-{day} {hour}:{mins} {tzsign}{tzhour}:{tzmin}".format(
            **date_dict
        )
