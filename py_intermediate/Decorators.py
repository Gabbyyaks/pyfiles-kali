# Decorators - function that takes another function and extends the behavior of the latter function
# without explicitly modifying it
# Types - function and class decorators - function decorators mostly used
from lxml.html.diff import end_tag


def start_end_decorator(func):

    def wrapper():
        print('start')
        func()
        print('end')
    return wrapper

@start_end_decorator            # same as line 17
def print_name():
    print("Perry")

# print_name = start_end_decorator(print_name)  # *********   line - 17
# print_name()

# ************** Decorator taking in arguments ********** template
import functools
from functools import *

def my_decorator(func):

    def greeting(*args, **kwargs):
        print("hello there!")
        result = func(*args, **kwargs)
        print("Good Day")
        return result
    def end_3():
        print("Done")

    return greeting
    return end_3

@my_decorator

def add5(x):
    return x + 5

results = add5(5)
print(results)






















