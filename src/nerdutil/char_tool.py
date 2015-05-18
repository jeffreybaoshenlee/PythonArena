__author__ = "jeffrey"
__date__ = "$2015/5/12 下午 12:23:27$"

# TODO: Write a multiplexer function which returns a value to indicate whether 
#           the specified instance is of the type A or B. If neither, it raises
#           an exception.

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    elif isinstance(bytes_or_str, str):
        value = bytes_or_str
    else:
        raise RuntimeError("The argument must be a bytes or a str.")

    return value

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    elif isinstance(bytes_or_str, bytes):
        value = bytes_or_str
    else:
        raise RuntimeError("The argument must be a bytes or a str.")
    return value
