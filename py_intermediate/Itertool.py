# itertools - a collection of tools for handling iterators
# - iterators are datatypes that can be used in a for loop - most common type is list
# itertools - Product, Permutations, combinations, accumulate, groupBy, and infinite iterators

from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
import operator     # use additional function with accumulate function
from itertools import groupby
from itertools import count, cycle, repeat


# Product - prints product of two lists (all possible outcomes)
a = [1, 2]
b = [3, 4]
# prod = product(a, b, repeat= 2) - repeat twice
prod = product(a, b)
# print(list(prod))         ********


# Permutation - returns all possible ordering of an input
p = [1, 2, 3]
perm = permutations(p)
# print(list(perm))   # use list function to print iterable objects  ********
perm1 = permutations(p, 2)  # "2" - specify the length of the output
# print(list(perm1))            *******


# Combination - Makes all possible combinations with a specified length
c = [1, 2, 3, 4]
comb = combinations(c, 3)       # "3" - specified length of combination
# print(list(comb))     *******

# combination_with_replacement - allows repetition (using same number combinations)
comb_wr = combinations_with_replacement(c, 2)
# print(list(comb_wr))   *******


# Accumulate - makes an iterator that returns accumulated sums or any binary function given as input

am = [1, 2, 5, 3, 4]
print(am)
acc = accumulate(am)    # - by default returns sum - import operators to use mul and other funcs
print(list(acc))

acm = accumulate(am, func= operator.mul)    # returns multiplication
print(am)
print(list(acm))

acm1 = accumulate(am, func=max)         # returns max value when compared to each element
print(am)
print(list(acm1))


# GroupBy - makes an iterator that returns keys and groups from an iterable

def less_than_3(x):
    return x < 3

g = [1, 2, 3, 4]
grp = groupby(g, key=less_than_3)   # groups elements less than 3, return false and group false elements

grp1 = groupby(g, key=lambda x: x < 3)   # using lambda expression - same as less_than function
for key, value in grp:
    print(key, list(value))

# Example 2 - GroupBy

persons = [{"name": "Lisa", "age": 25}, {"name": "max", "age": 27},
           {"name": "Tim", "age": 25}, {"name": "Claire", "age": 28}]

grp2 = groupby(persons, key=lambda x: x["age"])
for key, value in grp2:
    print(key, list(value))


# infinite iterators - count, cycle, repeat

for i in count(10):     # prints infinite loop starting from 10
    print(i)
    if i == 25:
        break

# cycle

ab = [1, 2, 3]
# for x in cycle(ab):     # prints infinite loop repeating items in list ab (cycle form)
#     print(x)


# repeat -
for i in repeat(1, 5):      # infinitely prints indicated number ("1") unless a stop (second) argument is indicated (5)
    print(i)

#  prints "1" infinitely or stops at the indicated number (second argument)









