from typing import List

Dates = List[str]

""" Documentation for ParseCalendarDays class
This class is responsible for handling the parsing of the date information provided
by the dataset. It has various methods to return the appropriate feature values
per provided date and time.
"""


class ParseCalendarDays:

    def __init__(self, datetimelist: Dates):
        """ Class instantiation
        Args:
                self: The current class instance.
                dateTimeList: A list of date with time strings.
        Returns:
                None
        """
        self.datetimelist = datetimelist

    def get_dow_feature_scale(self, min: float, max: float, increment: float):
        """ Get a feature value for each day of the week for a given date
        Args:
                self: The current class instance.
                min: The minimum scale value.
                max: The maximum scale value.
                increment: The size between values within the min max range.
        Returns:
                Returns a row vector for each example in the date list.
        """

    def get_tos_feature_scale(self, min: float, max: float, increment: float):
        """ Get a feature value for the time of season for a given date
        Args:
                self: The current class instance.
                min: The minimum scale value.
                max: The maximum scale value.
                increment: The size between values within the min max range.
        Returns:
                Returns a row vector for each example in the date list.                

        Time Of Season Reference:

        Winter: December 1st -> February 28th
        Spring: March 1st -> May 31st
        Summer: June 1st -> August 31st
        Fall: September 1st -> November 30th

        """

    def get_tod_feature_scale(self, min: float, max: float, increment: float):
        """ Get a feature value for the time of day for a given date
        Args:
                self: The current class instance.
                min: The minimum scale value.
                max: The maximum scale value.
                increment: The size between values within the min max range.
        Returns:
                Returns a row vector for each example in the date list.
        """

    def is_national_holiday(self, min: float, max: float):
        """ Get a feature value for the time of day for a given date
        Args:
                self: The current class instance.
                min: The minimum scale value.
                max: The maximum scale value.
        Returns:
                Returns a row vector for each example in the date list.
        """
