# Random Modules - pseudo random numbers, - secret module - cryptographically strong numbers, - Numpy - generate arrays
import random

# Random module - generates pseudo random numbers for various distributions ( random but reproducible

a = random.random()     # prints random float from zero to one ( 0 - 1 )
print(a)
a = random.uniform(1, 5)    # random float from 1 - 5
print(a)
a = random.randint(1, 10)   # random integer from 1 - 10 ( may include upper bound sometimes i.e 1 or 10
print(a)
a = random.randrange(1, 10)     #  random integer 1 - 9 ( does not include upper bound (10)
print(a)
b = random.normalvariate(0, 1)  # useful for statistics - generate value with mean 0, and standard deviation 1
print(b)


# function / sequence using random modules
mylist = list("ABCDEFGH")
print(mylist)
c = random.choice(mylist)   # selects a random element from the list
print(c)
c = random.choices(mylist, k=3)     # selects 3 random element and can select same element multiple times
print(c)
c = random.sample(mylist, 3)    # selects 3 random element
print(c)
mylist1 = mylist.copy()
random.shuffle(mylist1)      # shuffles the original list
print(mylist)
print(mylist1)


# Reproducing random Numbers

random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randint(1, 10))

random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randint(1, 10))


# Module for non reproducible numbers
# used for tokens, authentication or passkeys etc

import secrets

d = secrets.randbelow(10)   # generates number from 0 to 9 excluding the upperbound 10
print(d)

d = secrets.randbits(4)     # generates random number of not more than 4 (k=4) bits
print(d)

db = list('ABCDEFGGH')
print(secrets.choice(db))   # prints non-reproducible random alphabet from the list


# Using Numpy - numpy uses different mode of number generation / seed from the standard library

import numpy as np

ab = np.random.rand(3, 3)  # prints 3D floats (3), also 3x3D float (3, 3)
print(ab)

ab = np.random.randint(0, 10,(3,4)) # generate random integer from 0-9 in 3D (0, 10, 3), - (0, 10,(3, 4)) - for 4D array
print(ab)

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(arr)
np.random.shuffle(arr)
print(arr)

# Numpy seed

np.random.seed(1)
print(np.random.rand(3,3))      # generates 3x3 Dimension random float

np.random.seed(1)
print(np.random.rand(3,3))















