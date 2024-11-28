# List is a collection datatype : ordered, mutable, allows duplicate values

myList = ["Banana", "Apple", "Orange"]
# print(myList)

mylist0 = [-2, -3, -5, 0, 3, 1, 2]

mylist1 = list()
# print(mylist1)

# Lists allows different datatypes
mylist2 = [5, True, "allow", 20.1]
for i in mylist2:
    print(type(i))

# you can assess items in a list using the item index - 0
item = mylist2[2]   # prints third item on the list
print(item)

# -1 selects the last items in the list
item1 = myList[-1]
print(item1)

# iterating items in list (where i, can be set as anything)
for i in myList:
    print(i)

# checking if items are available in a list
if "Banana" in myList:
    print("Yes")
else:
    print("No")

# Methods on a list

print(len(myList))  # prints length of elements in a list
myList.append("cherry")     # add items to the end of a list
print(myList)

myList.insert(1, "Mango")   # add items in a list using specific index
print(myList)

print(myList.pop())     # prints and deletes the lst item on a list
print(myList)
myList.remove("Mango")   # removes specific items in a list (generates error if item not present)
print(myList)
myList.reverse()    # prints inverse of the list
print(myList)
# myList.clear()      # Deletes all items on a list
# print(myList)
print(mylist0)
# mylist0.sort()      # Sorts the list in ascending order - also modifies the original list
new_list0 = sorted(mylist0)     # sorting list method 2 without modifying the original list
print(new_list0)

# Tips to creating & manipulating a list
list0 = [0] * 5     # creates a list with five zeros
print(list0)

list1 = [1, 2, 3, 4, 5]

n_list = list0 + list1      # creates a list with items of list0 & list1
print(n_list)

# Slicing list operation [start : stop : step]
fresh_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(fresh_list)
a_list = fresh_list[1:]    # start at index 1 and prints all remaining value
print(a_list)
a_list = fresh_list[:5]     # without indicating start index, prints till stop index
print(a_list)
a_list = fresh_list[1:5]    # starts at index 1 and stops at index 5
print(a_list)
b_list = fresh_list[::1]    # step by default is 1
print(b_list)
b_list = fresh_list[::2]    # skips the second value
print(b_list)
b_list = fresh_list[::-1]    # prints in reverse form
print(b_list)

# Copying a list
org_list = ["bread", "butter", "bake"]

cpy_list = org_list     # copies list but changes made affect the original list
# cpy_list.append("lemon")
# print(cpy_list)
# print(org_list)

# Best practice copying list --
cpy_list0 = org_list.copy()     # using copy method/function
cpy_list1 = list(org_list)      # using list reserved word
cpy_list2 = org_list[:]     # using slicing to copy list
# print(cpy_list0)
# print(cpy_list1)
# print(cpy_list2)

# List comprehension
x = [1, 2, 3, 4, 5, 6]
print(x)
#  creating a list with squared value of original list
y = [i*i for i in x]    # where i, can be set  as anything
print(y)

z = [i for i in range(9)]   # creates a list with range 9
print(z)
