from datetime import datetime, timedelta


class TemplateLocalTime:
    def __init__(self, date_dict):
        self.date_dict = date_dict
        self.adjust_local_time = None

    @property
    def adjust_local_time(self):
        return self.__adjust_local_time

    @adjust_local_time.setter
    def adjust_local_time(self, local_time):
        time_tzhour = self._time_tzhour(self.date_dict)
        local_time = timedelta(
            hours=int(time_tzhour[0:3]), minutes=int(time_tzhour[4:])
        )
        self.__adjust_local_time = local_time

    def _time_tzhour(self, date_dict):
        return f"{date_dict['tzsign']}{date_dict['tzhour']}:{date_dict['tzmin']}"
