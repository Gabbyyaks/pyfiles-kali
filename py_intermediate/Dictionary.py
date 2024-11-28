# Dictionary is a collection Datatype: Key-value pairs, Unordered, Mutable (key maps to its associated value

# Creating a dictionary
mydict = {"name": "Max", "age": 28, "city":"New york"}  # first method, key - value pairs
print(mydict)
mydict2 = dict(name= "Max", age=23, city= "Boston")     # using dict function to create dictionary
print(mydict2)

print(mydict2["city"])      # printing values using keys, -- returns error if key unavailable
print(mydict2["name"])

# adding pairs to existing dictionary -- mutable(changeable)
mydict["email"] = "max@yxl.com"     # overwrites existing value when created with same key
print(mydict)

mydict["email"] = "maxwell@onion.com"
print(mydict)

# Deleting items in a dictionary

del mydict["email"]     # using del function to delete items
print(mydict)

mydict.pop("name")      # remove items by key
print(mydict)

mydict.popitem()        # removes last item on the dictionary
print(mydict)

mydict["name"] = "Max"
mydict["city"] = "New Jersey"

# Checking for items in a dictionary

if "name" in mydict:        # using if statement
    print(mydict["name"])
else:
    print("None")

try:        # using Try and except statement
    print(mydict["email"])
except KeyError:
    print("No value not found!")

# Looping through dictionary

for key in mydict:                  # getting keys in dictionary - mydict.key() can also be used
    print(key)

for value in mydict.values():       # getting values in dictionary
    print(value)

for item in mydict.items():         # getting key value pairs
    print(item)

for key, value in mydict.items():   # method 2, getting key value pairs
    print(f'{key}: {value}')

# Copying Dictionary

# mydict_cpy = mydict           # modifies the original dict -- not best practice
mydict_cpy = mydict.copy()      # Does not modify original dict
mydict_cpy0 = dict(mydict)      # Does not modify original dict
mydict_cpy["email"] = "madmax@pdfg.com"
print(mydict)
print(mydict_cpy)

# updating dictionary

a_dict = {"name": "max", "age":28, "city":"Boston" }
b_dict = dict(name="Mary", age=20, email="Madmax@mail.com")

a_dict.update(b_dict)
print(a_dict)

# Dictionary can also be created using tuple
# keys can also bee numerical
#  tuples can be used to create dictionaries, but not list cus list are mutable(changeable)

# mydict = {8: 16, 4:8}
# mytuple = (2, 4)
# mydict{mytuple: 15}



