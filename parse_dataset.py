# Will use pretty print for debugging purposes
import sys
import pandas as pd
import datetime
import helpers
import numpy as np
from pprint import pprint
from ParseCalendarDays import ParseCalendarDays

# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
data = pd.read_csv("DOM_hourly.csv")

# Preview the first 5 lines of the loaded data
data.head()

# Create the DataFrame object which allows the manipulation of the csv data
df = pd.DataFrame(data)
# Convert the data into a dictionary. By doing this the column headers of the csv data set become the
# keys and the data underneath the column headers become the key values split into their numerical dictionary
#
# In order to see this, execute this: pprint(df.head(10).to_dict())
#
# TODO: Replace with df.to_dict()
#
df_dict = df.to_dict()

# Get the access to the date time dictionary values
df_datetimes_dict = df_dict.get('Datetime')

# Loop through the date times and create a list of datetime strings
date_times = []
for key, value in df_datetimes_dict.items():
    date_times.append(value)

# Group the date times by year into a dictionary of values.
#
# So if you want all dates for 2010 for example, then you can access them by:
#   datetimes_grouped_by_year.get('2010')
#
datetimes_grouped_by_year = {}
for single_date in date_times:
    # Get the year for the date.
    single_date_year = helpers.get_year(single_date)
    datetimes_grouped_by_year.setdefault(
        str(single_date_year), []).append(single_date)

dataset_object = ParseCalendarDays(datetimes_grouped_by_year)

pprint(dataset_object.get_tos_feature_scale())
