 # lambda function is a small anonymous one line function that is defined without a name
 # lambda arguments : expression -- lambda keyword - takes in arguments: - evaluate expression and give result

add10 = lambda x: x + 10        # adds 10 to given number using lambda func.

print(add10(5))

def adds10(x):      # add 10 to given number using normal func.
    return x + 10


print(adds10(3))

# lambda can also take in multiple arguments

mult = lambda x, y: x*y     # lambda func to multiply the given values

print(mult(5,3))

def mult_func(x, y):        # using normal func to multiply given values
    return x * y


print(mult_func(5,5))


# lambda functions are typically used once in your code -
# or used as an argument to hire other functions (function that takes in other function as argument)
# can be used along with built-in functions - sorted, map, filter, reduce


# sorted

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)      # by default sorts by x argument (x, y), (0, 1)

def sort_y(x):      # sorting by y using normal func.
    return x[1]

points2D_sorted1 = sorted(points2D, key=lambda x: x[1])     # sorts by y argument using lambda func.
points2D_sorted2 = sorted(points2D, key=sort_y)     # using defined func.
points2D_sorted3 = sorted(points2D, key=lambda x: x[0] + x[1])      # sorts according to the sum

print(points2D)
print(points2D_sorted)
print(points2D_sorted1)
print(points2D_sorted2)


# map function transforms each element with a func.
# map(func, seq) - takes function and sequence

a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)   # multiplies the given sequence - returns list mult by 2

print(list(b))

x = [x*2 for x in a]      # using list comprehension - mult. given sequence
print(x)


# filter - returns all elements which function evaluates to true
# filter(func. seq) - func to return true or false

f = [1, 2, 3, 4, 5, 6]
ft = filter(lambda x: x%2==0, f)    # returns element if true (element divide by 2 equals 0)

print(list(ft))

fb1 = [x for x in f if x%2==0]      # filter using list comprehension
print(fb1)

fb = [x%2==0 for x in f]        # returns true or false instead of elements
print(list(fb))


# reduce - repeatedly applies func to elements and returns single value
# reduce(func, seq) - also takes func and seq
from functools import reduce

r = [1, 2, 3, 4]

product_a = reduce(lambda x,y: x*y, r)      # returns product of the sequence / list

print(product_a)






