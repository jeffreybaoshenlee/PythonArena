__author__ = "jeffrey"
__date__ = "$2015/7/7 下午 04:31:39$"

from nerdtime.rawtime import *
from nerdtime.nerddatetime import *

if __name__ == "__main__":
    time_str = get_local_time_str();
    print(time_str)
    
    utc_str = get_utc_str(time_str)
    print(utc_str)
    
    depart_sfo = '2014-05-01 15:45:16 CST'
    formatted_time_str = parse_and_format_time_str(depart_sfo)
    print(formatted_time_str)
    
    try:
        arrival_nyc = '2014-05-01 23:33:24 EDT'
        formatted_time_str = parse_and_format_time_str(arrival_nyc)
    except ValueError as e:
        print(e)
        
    from datetime import datetime
    local_time = get_local_time(datetime(2015, 1, 1))
    print(local_time)
    
    local_time = '2014-08-10 11:18:30'
    utc_time = get_utc_time(local_time)
    print(utc_time)
    
    arrival_nyc = '2014-05-01 23:33:24'
    utc_time = get_utc_time_with_timezone(arrival_nyc, 'US/Eastern')
    print(utc_time)
    
    local_time = get_local_time_with_timezone(utc_time, 'US/Pacific')
    print(local_time)
    
    local_time = get_local_time_with_timezone(utc_time,'Asia/Katmandu')
    print(local_time)
    
    local_time = get_local_time_with_timezone(utc_time,'Asia/Taipei')
    print(local_time)