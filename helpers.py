import datetime

"""
	This is a helper file that holds reusable functions.

"""


def get_year(date_string: datetime) -> int:
	""" This is a date time helper function that takes in a date time string and returns a year.
	Args:
	        date_string: This is a date time string. In the dataset it's formatted as 'YYYY-MM-DD HH:MM:SS'
	Returns:
	        Returns the year for date time string as an integer.
	"""

    # Create date object
    date_obj = datetime.datetime.strptime(
        date_string, '%Y-%m-%d %H:%M:%S')
    # Get the year value.
    year = int(date_obj.strftime('%Y'))
    # Return the year.
    return year
