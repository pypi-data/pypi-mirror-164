# BB-DateParser

Attempts to convert any written date into a datetime object. It will try to return the most likely format but you can use the `list_all = True` option to get all the results. To make it more useful for my needs (and easier to write :P), it only works for years 1000 - 2099.

## Usage

```python

from dateparser.dateparser import DateParser

dp = DateParser()
my_date = "October 1st, 1985 4:35pm"

date_fmt = dp.parse_date( my_date )

print( date_fmt )
'%B %dst, %Y %I:%M%p'

# To obtain a list of all the results

date_fmt_list = dp.parse_date( my_date, list_all = True )

print( str(date_fmt_list) )
"['%B %dst, %Y %I:%M%p']"

# In this case only one result was found but was returned in list format
# The DateParser class holds the data from the last result
# This is cleared and recreated each time self.parse_date() is used
# Below are the variables created from each date parsed

# separated list of the date string
dp.alldata = ['October', ' ', '01', 'st,', ' ', '1985', ' ', '04', ':', '35', 'PM']

# list of actual date data in dictionary form { 'alldata index': str(data) }
dp.data = { 0: 'October', 2: '1', 5: '1985', 7: '4', 9: '35', 10: 'pm' }

# created datetime object from date string
dp.dateObject = datetime.datetime(1985, 1, 1, 16, 35)

# format code for datetime
dp.formatting = '%B %mst, %Y %I:%M%p'

# boolean - True only if successful in parsing the date
dp.isValid = True

# list of non date data pulled from date string
dp.separators = [' ', 'st,', ' ', ' ', ':']

# list of all possible results (is returned when 'list_all' = True)
dp.format_list = ['%B %dst, %Y %I:%M%p']

# DateParser is a subclass of DateData which is a subclass of the builtin
# dict class. Therefore, all the parsing variables are also available through
# the DateParser class.

```