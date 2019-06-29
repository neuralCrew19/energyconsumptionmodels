import datetime


def get_year(date_string: datetime) -> int:
    # Create date object
    date_obj = datetime.datetime.strptime(
        date_string, '%Y-%m-%d %H:%M:%S')
    # Get the year value.
    year = int(date_obj.strftime('%Y'))
    # Return the year.
    return year
