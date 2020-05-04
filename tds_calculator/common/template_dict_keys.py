from datetime import datetime, timedelta


class TemplateDictKeys:
    def __init__(self, prop_obj, date_dict):
        self.prop_obj = prop_obj
        self.date_dict = date_dict
        self.build_list = []
        self.key_list = None

    @property
    def key_list(self):
        return self._key_list

    @key_list.setter
    def key_list(self, build_list):
        build_list = self.build_list
        for key, val in self.date_dict.items():
            build_list.append(f"self.{self.prop_obj}.{key}.text")
        self._key_list = build_list
