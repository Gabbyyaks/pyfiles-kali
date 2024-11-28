# Collections implements special container datatypes and provides alternatives with additional functionality compared
# to the general builtin containers like Dictionary, list, and tuples.
# Collections : Counter, namedtuple, OrderedDict, defaultDict, and deque

from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

# Counter - a container that stores elements as dictionary keys and counts as dictionary value

a = "aaaaabbbccc"

my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1)) # - prints most common element - element with the highest counts
print(my_counter.most_common(2)) # - prints two most common elements
print(my_counter.most_common(1)[0])  # access tuple at index 0 in the list
print(my_counter.most_common(1)[0][0])  # access element with index 0 in the tuple

# having a list with different elements in variable "a"
print(my_counter.elements())
print(list(my_counter.elements())) # convert iterable to list to view elements

# NamedTuple - first import
# easy to create lightweight object type similar to a struct

Point = namedtuple("Point", "x, y")     # creating a class (Point) with field X and Y
pt = Point(1, -5)       # Assigning values to X and Y fields
print(pt)
print(pt.x, pt.y)


#  OrderedDict - Just like regular dictionary but remembers the order the items were inserted
#  - now available in regular dict from v 3.7 and older

ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict["d"] = 4

print(ordered_dict)

ordered_dict2 = {}
ordered_dict2["b"] = 2
ordered_dict2["a"] = 1
ordered_dict2["c"] = 3
ordered_dict2["d"] = 4

print(ordered_dict2)

# defaultDict - similar to regular dictionary but has a default value if key hasn't been set

d = defaultdict(int)  # - pass in default value, int, float, or list
d["a"] = 1
d["b"] = 4
print(d)
print(d["c"])   # - undefined key - returns default set value (int, float, or list) - return no value when set to str


# Deque  - double ended queue, used to add or remove elements from both ends

dq = deque()

dq.append(1)        # - add items
dq.append(2)
dq.appendleft(3)    # - add items to left
print(dq)

dq.pop()
print(dq)

dq.popleft()        # remove items from left
print(dq)

dq.extend([3, 5, 4,])           # adding more items(e.g list)
print(dq)

dq.extendleft([7, 8, 9])        # adding more items(e.g list) to left
print(dq)

dq.rotate(1)    # rotates the elements starting from the first element
print(dq)

dq.rotate(2)    # rotates the elements starting from the second element
print(dq)

dq.rotate(-1)   # rotates the elements starting from the opposite direction
print(dq)


