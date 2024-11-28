# Errors and Exceptions
# Python program terminates as soon as it encounters an error - either a syntax error or exception error
from Dictionary import value

# Syntax Error - this occurs when the parser detects a syntactically incorrect statement

# a = 5
# print(a)))

# Exceptions - even if statement is syntactically correct it may cause an error when executed
# TypeError - multiplying a string with an integer
# ModuleNotFoundError - when imported module not found or correct
# NameError - when variable called is not defined
# FileNotFoundError - Indicated file not available
# ValueError - when requested value not available
# IndexError - when index is out of range / not in sequence
# KeyError - Usually occurs in dictionary when key requested not available



# Raising an Exception - when you want to force an exception to occur when certain conditions are met
# Method 1 - raise
x = -5
# if x < 0:
#     raise Exception("X should be positive")       # ******

# Method 2 - Assert - raises and assertion error if assertion is not true
# Assertion - no if statement required

a = -5
# assert (a>=0), "a should be positive"        # *******




# Handling Errors and Exceptions
# we use try and except block to catch errors to avoid program from stopping
try:
    c = 5 / 1
    d = 10 + "str"
except ZeroDivisionError as e:      # when error type is unknown 'Exception as e' helps identify error
    print(e)
except TypeError as e2:      # when error is known - using error name to optimize program flow
    print(e2)
else:                       # else runs when no exception error occurs
    print("code has no errors")
finally:                    # finally runs weather exceptions are met or not
    print("Cleaning code...")


# Defining our own errors


class ValueTooHighError(Exception):     # where Exception is the base class
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too High")
    if x < 10:
        raise ValueTooSmallError(f"Value too small", x)


try:
    test_value(100)
    test_value(8)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)




















