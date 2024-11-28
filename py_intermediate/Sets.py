# Set is a collection datatype : unordered, mutable, no duplicates
#  created with curly braces just like dictionary but no key value pairs

# creating an empty set -- would be recognized as dictionary without the set function
My_set = set()
my_set = {1, 2, 3, 4, 5,}
my_set = set([1, 2, 3,])

print(my_set)
# adding and removing items --- methods
My_set.add(1)
My_set.add(2)
My_set.add(3)

# My_set.remove(4)        # displays error when element unavailable
My_set.discard(4)         # does not display error
# My_set.clear()          # deletes all items in a set
# My_set.pop()            # deletes last item on a list

# iterating through a set -- can bee done using for loop
for i in my_set:
    print(i)

if 2 in my_set:         # checking for items
    print("Yes")
else:
    print("Not available")

#  method in set
# SET manipulation -- Union Intersection etc

odds = {1, 3, 5, 7, 9}
even = {0, 2, 4, 6, 8}
prime = {2, 3, 5, 7,}

# union of set - joining two sets without duplicates

u = odds.union(even)
# print(u)

#  intersection -- takes elements found in both sets

i = even.intersection(prime)
# print(i)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9,}
setB  = {1, 2, 3, 10, 11, 12, 13,}

set_a = setA.copy()
set_b = setB.copy()

# Difference -- prints the different elements present in set a not in b and vice versa

x = setA.difference(setB)
# print(x)

# symmetric_difference -- prints the different elements in both set together but not in both set
diff = setA.symmetric_difference(setB)
print(diff)

# Update -- takes elements in set B not present in set A to update set A (modifies the original set)
# set_a.update(set_b)
# print(set_a)

# Intersect Update -- takes elements found in both set forming a new set
# setA.intersection_update(set_b)
# print(set_a)

# Difference update - updates the set by removing the elements found in another set and vice versa
# set_a.difference_update(set_b)
print(set_a)

#  symmetric_difference update -- updates a set by removing elements present in both set and keeping both difference
setA.symmetric_difference_update(setB)
print(setA)

# Superset - a set carrying all elements of subset and more
# Subset - a set which all elements are found in superset

subA = {1, 2, 3, 4, 5}
subB = {1, 2, 3}
subC = {6, 7}

print(subA.issubset(subB))  # -- returns False -- returns True vice versa
print(subB.issubset(subA))  # -- returns True -- returns False vice versa

#  Disjoint - when both sets have no intersections (different elements)
print(subA.isdisjoint(subC))  # -- returns True -- returns False when set has common elements

# Frozenset - is a collection datatype, am immutable version of a normal set - cannot be changed after it's creation

a = frozenset([1, 2, 3, 4, 5, 6])
# a.add(8) -- returns error -- cannot be changed
# other set comparison methods works -- intersection, difference, issubset etc.





