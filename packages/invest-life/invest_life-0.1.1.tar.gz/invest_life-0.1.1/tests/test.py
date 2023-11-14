# -*- coding: utf-8 -*-

from investlife import *

set_token(token = 'KfcgMhoufAhfZD-UQkr9eA5PoxTteObNO2HceqOc4VPa-okVYet5q9qOxo4KmXck')

data = stock_list()
# data = get_realtime_quotes()
print(data.head())
