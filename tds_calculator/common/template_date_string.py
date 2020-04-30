from datetime import datetime, timedelta


class TemplateDateString:
    def _date_dict(self, date_dict):
        return "{year}-{mon}-{day} {hour}:{min} {tzsign}{tzhour}:{tzmin}".format(
            **date_dict
        )

    def _time_tzhour(self, date_dict):
        return f"{date_dict['tzsign']}{date_dict['tzhour']}:{date_dict['tzmin']}"

    def adjust_local_time(self, date_dict):
        alt = self._time_tzhour(date_dict)
        return timedelta(hours=int(alt[0:3]), minutes=int(alt[4:]))

    def string_datetime(self, date_dict):
        date_string = self._date_dict(date_dict)
        return datetime.strptime(date_string, "%Y-%m-%d %H:%M %z")
