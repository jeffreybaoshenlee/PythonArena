__author__ = "jeffrey"
__date__ = "$2015/7/7 下午 06:20:25$"

from time import localtime
from time import mktime
from time import strftime
from time import strptime
from time import time

from nerdtime import *

def get_local_time_str():
    now = time()
    local_tuple = localtime(now)
    time_str = strftime(time_format, local_tuple)
    return time_str

def get_utc_str(time_str):
    time_tuple = strptime(time_str, time_format)
    utc_str = mktime(time_tuple)
    return utc_str

def parse_and_format_time_str(time_str):
    time_tuple = strptime(time_str, parse_format)
    formatted_time_str = strftime(time_format, time_tuple)
    return formatted_time_str