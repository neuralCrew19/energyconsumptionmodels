# Will use pretty print for debugging purposes
from pprint import pprint
# Using Python Pandas for CSV analyzing
import pandas as pd

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
df_dict = df.head(10).to_dict()

# Get the access to the date time dictionary values
df_datetimes_dict = df_dict.get('Datetime')

# Loop through the date times and create a list of datetime strings
date_times = []
for key, value in df_datetimes_dict.items():
    date_times.append(value)

pprint(date_times)
