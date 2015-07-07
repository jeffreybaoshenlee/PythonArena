__author__ = "jeffrey"
__date__ = "$2015/7/7 下午 06:20:25$"

from datetime import datetime
from datetime import timezone
from nerdtime import *
import pytz
from time import mktime

def get_local_time(utc_time):
    utc_time = utc_time.replace(tzinfo=timezone.utc)
    local_time = utc_time.astimezone()
    return local_time

def get_utc_time(local_time):
    local_time = datetime.strptime(local_time, time_format)
    time_tuple = local_time.timetuple()
    utc_time = mktime(time_tuple)
    return utc_time

def get_utc_time_with_timezone(local_time, zone):
    naive_time = datetime.strptime(local_time, time_format)
    zone = pytz.timezone(zone)
    localized_time = zone.localize(naive_time)
    utc_time = pytz.utc.normalize(localized_time.astimezone(pytz.utc))
    return utc_time

def get_local_time_with_timezone(utc_time, zone):
    zone = pytz.timezone(zone)
    local_time = zone.normalize(utc_time.astimezone(zone))
    return local_time