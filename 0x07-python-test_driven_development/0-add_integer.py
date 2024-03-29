#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Returns the addition of a and b
    Args:
        a(int, float) the first value
        b(int, float) the second value
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    
    if type(a) is float or type(b) is float:
        a = int(a)
        b - int(b)
    return a + b
