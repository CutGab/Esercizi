import re

def is_integer(n):
    match = re.fullmatch(r'[+-]?\d+', n)
    return match



is_integer("123")
