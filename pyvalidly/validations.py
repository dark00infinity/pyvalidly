import re

def is_email(value):
    if not isinstance(value, str):
        return False
    return re.match(r"[^@]+@[^@]+\.[^@]+", value) is not None

def is_url(value):
    if not isinstance(value, str):
        return False
    return re.match(r"https?://[^\s]+", value) is not None

def min_value(min_val):
    return lambda x: isinstance(x, (int, float)) and x >= min_val

def max_value(max_val):
    return lambda x: isinstance(x, (int, float)) and x <= max_val

def min_length(min_len):
    return lambda x: hasattr(x, '__len__') and len(x) >= min_len

def max_length(max_len):
    return lambda x: hasattr(x, '__len__') and len(x) <= max_len

def is_validation_func(obj):
    return callable(obj)