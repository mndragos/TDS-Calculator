import kivy

kivy.require("1.11.1")
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from datetime import datetime, timedelta, timezone

from tds_calculator.common.departure_section import DepartureSection
from tds_calculator.common.arrival_section import ArrivalSection
from tds_calculator.common.distance_section import DistanceSection
from tds_calculator.common.speed_section import SpeedSection
from tds_calculator.common.error_message import ErrorMessage
from tds_calculator.common.template_date_string import TemplateDateString


class Buttons(BoxLayout):
    departure_section = DepartureSection()
    arrival_section = ArrivalSection()
    distance_section = DistanceSection()
    speed_section = SpeedSection()
    missing_value = ErrorMessage()
    template = TemplateDateString()

    def calculate_time_delta(self) -> float:
        departure_checkbox = self.dep_section.departure_checkbox.active
        arrival_checkbox = self.arr_section.arrival_checkbox.active
        distance_checkbox = self.distance.distance_checkbox.active
        speed_checkbox = self.speed.speed_checkbox.active

        if departure_checkbox or arrival_checkbox:
            speed = float(f"{self.speed.spd.text}")
            distance = float(f"{self.distance.dist.text}")
            time_delta = round(distance / speed, 2)

        elif distance_checkbox or speed_checkbox:
            departure = self.template.string_datetime(self.dep_section.departure_dict)
            arrival = self.template.string_datetime(self.arr_section.arrival_dict)
            time_delta = round(((arrival - departure).total_seconds() / 3600), 2)
        return time_delta

    def calculate_distance(self) -> float:
        speed = float(f"{self.speed.spd.text}")
        time_delta = self.calculate_time_delta()
        distance = round(speed * time_delta, 2)
        return distance

    def calculate_speed(self) -> float:
        distance = float(f"{self.distance.dist.text}")
        time_delta = self.calculate_time_delta()
        speed = round(distance / time_delta, 2)
        return speed

    def calculate_departure_datetime(self) -> datetime.timetuple:
        arrival = self.template.string_datetime(self.arr_section.arrival_dict)
        dtz = self.template.adjust_local_time(self.dep_section.departure_dict)
        time_delta = timedelta(hours=self.calculate_time_delta())
        departure = arrival - time_delta
        departure = departure.astimezone(timezone(dtz))
        return departure.timetuple()

    def calculate_arrival_datetime(self) -> datetime.timetuple:
        departure = self.template.string_datetime(self.dep_section.departure_dict)
        atz = self.template.adjust_local_time(self.arr_section.arrival_dict)
        time_delta = timedelta(hours=self.calculate_time_delta())
        arrival = departure + time_delta
        arrival = arrival.astimezone(timezone(atz))
        return arrival.timetuple()

    def calculate(self):
        departure_checkbox = self.dep_section.departure_checkbox.active
        arrival_checkbox = self.arr_section.arrival_checkbox.active
        distance_checkbox = self.distance.distance_checkbox.active
        speed_checkbox = self.speed.speed_checkbox.active
        try:
            if departure_checkbox:
                dep = self.calculate_departure_datetime()
                self.dep_section.day.text = str(dep[2])
                self.dep_section.mon.text = str(dep[1])
                self.dep_section.year.text = str(dep[0])
                self.dep_section.hour.text = str(dep[3])
                self.dep_section.mins.text = str(dep[4])
                self.time_delta_label.text = str(
                    timedelta(hours=self.calculate_time_delta())
                )
            elif arrival_checkbox:
                arr = self.calculate_arrival_datetime()
                self.arr_section.day.text = str(arr[2])
                self.arr_section.mon.text = str(arr[1])
                self.arr_section.year.text = str(arr[0])
                self.arr_section.hour.text = str(arr[3])
                self.arr_section.mins.text = str(arr[4])
                self.time_delta_label.text = str(
                    timedelta(hours=self.calculate_time_delta())
                )
            elif distance_checkbox:
                self.distance.dist.text = str(self.calculate_distance())
                self.time_delta_label.text = str(
                    timedelta(hours=self.calculate_time_delta())
                )
            elif speed_checkbox:
                self.speed.spd.text = str(self.calculate_speed())
                self.time_delta_label.text = str(
                    timedelta(hours=self.calculate_time_delta())
                )
            else:
                self.missing_value.on_error("Select One Checkbox.")
        except ValueError:
            return self.missing_value.on_error(
                "Please,\nfill in the required fields\ncorrectly."
            )

    def reset(self):
        prop_obj = [
            self.dep_section.year,
            self.dep_section.mon,
            self.dep_section.day,
            self.dep_section.hour,
            self.dep_section.mins,
            self.dep_section.tzsign,
            self.dep_section.tzhour,
            self.dep_section.tzmin,
            self.arr_section.year,
            self.arr_section.mon,
            self.arr_section.day,
            self.arr_section.hour,
            self.arr_section.mins,
            self.arr_section.tzsign,
            self.arr_section.tzhour,
            self.arr_section.tzmin,
            self.distance.dist,
            self.speed.spd,
            self.time_delta_label,
        ]

        for items in prop_obj:
            items.text = ""
