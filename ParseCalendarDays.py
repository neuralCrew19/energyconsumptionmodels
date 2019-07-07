from typing import Dict

Dates = Dict[str, str]

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

    def get_tos_feature_scale(self):
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

        # First we need to check to see if the data passed in has multiple years. If so
        # then we need to loop through all of the years and return a row vector for each date
        # of each year.
        #
        # If the dates for one particular year was passed in, then we just return a row vector
        # for each date.

        multiple_years_provided = False

        try:
            if len(self.datetimelist.keys()) > 0:
                multiple_years_provided = True
        except AttributeError as e:
            pass

        if multiple_years_provided:
            # If multiple years provided, then loop through the years.
            for year, date_list in self.datetimelist.items():
                # First, get the previous year from the current year. This will be needed to see
                # if a particular date falls within the winter season.
                beginning_current_year = datetime.date(
                    year=int(year), month=1, day=1)
                previous_year = beginning_current_year.replace(
                    year=beginning_current_year.year - 1).year

                # Now create the season date objects

                # Winter season
                winter_start = datetime.date(
                    year=previous_year, month=12, day=1)
                winter_end = datetime.date(year=int(year), month=2, day=28)
                # Spring season
                spring_start = datetime.date(year=int(year), month=3, day=1)
                spring_end = datetime.date(year=int(year), month=5, day=31)
                # Summer season
                summer_start = datetime.date(year=int(year), month=6, day=1)
                summer_end = datetime.date(year=int(year), month=8, day=31)
                # Fall season
                fall_start = datetime.date(year=int(year), month=9, day=1)
                fall_end = datetime.date(year=int(year), month=11, day=30)

                # Initialize numpy array.
                season_row_vector = np.zeros([1, len(date_list)])

                # Create a counter, which will help update the values in the row
                # vector.
                counter = 0

                # Next, loop through the dates provided in the year list for the current year in the
                # iteration.
                for date in date_list:
                    # Create the date object for the date in the dataset which needs to
                    # be evaluated.
                    date_in_dataset = datetime.datetime.strptime(
                        date, '%Y-%m-%d %H:%M:%S').date()

                    if winter_start <= date_in_dataset <= winter_end:
                        # The date falls in the winter season.
                        season_row_vector[0, counter] = 0.011
                    elif spring_start <= date_in_dataset <= spring_end:
                        # The date falls in the spring season.
                        season_row_vector[0, counter] = 0.012
                    elif summer_start <= date_in_dataset <= summer_end:
                        # The date falls in the summer season.
                        season_row_vector[0, counter] = 0.013
                    else:
                        # Then date falls in fall season.
                        season_row_vector[0, counter] = 0.014
                    # Increment the counter
                    counter += 1
        else:
            # Doing nothing for now.

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
