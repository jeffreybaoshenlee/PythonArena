#! /usr/bin/python

def safe_division(number, divisor, ignore_overflow,
                  ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

__author__ = "jeffrey"
__date__ = "$2015/5/28 下午 02:55:00$"

if __name__ == "__main__":
    print(safe_division(1,10**500,False,False));
#    print(safe_division(1.0,10**500,False,False));
    print(safe_division(1.0,10**500,True,False));
#   The overflow is actually ocurring in the conversion from 10**500 to its
#       corresponding float value.
    print(safe_division(1.0,10**500,False,False));