# Tuple is a collection datatype : ordered, immutable, allows duplicate items - Similar to list but cannot be changed
# Creating tuple
mytuple = "Max", 28, "Nigeria"  # can be created without parenthesis
mytuple = ("Max", 28, "Nigeria")    # tuple uses normal parenthesis for creation
print(mytuple)
print(type(mytuple))

mytuple0 = ("Max")   # using single items is stored as string -- add coma ',' to change to tuple
print(type(mytuple0))

mytuple1 = tuple(["Max", 28, "Nigeria"])    # can also be crated using tuple function
print(type(mytuple1))

# Accessing items in a tuple
tuple0 = "Max", 28, "Nigeria"
print(tuple0)
item = mytuple[0]   # Using item index to access values
print(item)
item = mytuple[1]
# print(item)
item = mytuple[-1]  # prints last item
# print(item)
item = mytuple[-2]  # prints second to last item
# print(item)
# iterating through a tuple
for i in tuple0:  # where i, can be anything
    print(i)

# tuple0[0] = "Tim"   # generates error, tuple cannot be changed after creation

# check if items are present in a tuple
if "Max" in tuple0:
    print("Yes")
else:
    print("No")

# Useful methods in tuple
mytup1 = ('a', 'p', 'p', 'l', 'e')

print(len(mytup1))      # length of elements in the tuple
print(mytup1.count('p'))    # count how many letter 'p'
print(mytup1.index('l'))    # get index of letter 'l'

# converting tuple to list & vice versa

my_tuple = ('bread', 'eggs', 'milk')
print(my_tuple)

my_list = list(my_tuple)
print(my_list)

my_tuple2 = tuple(my_list)
print(my_tuple2)

# Tuple Slicing [start : stop : step]

a_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)

b = a_tup[2:5]      # start printing from index 2 and stops at index 5 without printing the last index
print(b)

b = a_tup[:5]       # no start index prints all through stop index
print(b)

b = a_tup[::2]      # skips all second index -- 1 by default
print(b)

# Unpacking

b_tup = 'Max', 28, 'Nigeria'

name, age, country = b_tup      # Automatically assigns each variable to value, returns error when unevenly matched
print(name)
print(age)
print(country)

n_tup = (1, 2, 3, 4, 5,)
i1, *i2, i3 = n_tup     # using astric automatically assigns remaining value to a list
print(i1)       # prints first value
print(i3)       # prints last value
print(i2)       # converts remaining value to list

# Comparing List & Tuple
import sys
list1 = [1, 2, 3, 'hello', True]
tuple1 = (1, 2, 3, 'hello', True)
print(sys.getsizeof(list1), "bytes")
print(sys.getsizeof(tuple1), "bytes")

import timeit
print(timeit.timeit(stmt="[1, 2, 3, 4, 5,]", number=1000000))
print(timeit.timeit(stmt="(1, 2, 3, 4, 5,)", number=1000000))


