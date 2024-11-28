# String - is a collection datatype, ordered, immutable, text-representation
# created with single or double quotes -- triple quotes are used for multiple lines or documentations - ''' or """
# \ - escaping a single quote within a single quote statement -- \n - next line)
from orca.debug import printStack

my_string = "hello world"
My_string = 'Hello World'
print(my_string)
print(My_string)

# Accessing string characters - use same indexing method as list - but does not support assignments (cannot be changed)
char = my_string[1]  # prints letter with index 1
print(char)

# Accessing a substring with slicing -- [start : stop : step]
sub_string = my_string[0:4]  # start -- prints from index 0 - 6 but excluding 6
print(sub_string)

char1 = my_string[:5]  # stop - without start index prints to stop index
print(char1)

char2 = my_string[::2]  # step (1 by default): takes all second character or indicated number [ -1 reverse the string]

# String concatenation -- joining two or more strings

hello = "Hello there, my name is"
name = "Maxwell"

greeting  = hello + " " + name
print(greeting)

#  iterating a string
for i in name:
    print(i)

#  checking for letters or substring

if "M" in name:
    print("Yes")
else:
    print("No")

if "well" in name:
    print("True")
else:
    print("None")

# useful string methods
speech = "  hey there  "
print(speech.strip())  # removes the blank spaces - do not modify original string - unless reassign to a variable
speech = speech.strip()  # reassigned variable

word = "Gabby is a security engineer"

print(word.upper())     # - prints all uppercase
print(word.lower())     # - prints all lowercase
print(word.startswith("Gabby"))     # returns True if startswith Gabby
print(word.endswith("eer"))         # returns True if endswith 'eer'
print(word.find("b"))       # prints index of first occurrence of "b"
print(word.replace("engineer", "Analyst")) # - replace abd prints new string - does not modify original string
print(word)

# Converting lists to string - vice versa
words_1 = "How are you doing"
print(words_1)
# string to list
new_list = words_1.split() # -- default delimiter " " (space) -
print(new_list)

# List to string
new_word = ' '.join(new_list) # - empty string " ''.join " can be filled with any delimiter
print(new_word)

#  String concatenation -- best practice to concatenate

b_list = ["a"] * 6
print(b_list)

# Bad practice
string1 = ""
for i in b_list:
    string1 += i
print(string1)

# Good Practice -- Faster
string2 = "".join(b_list)
print(string2)

#  Formatting strings
# %, .format{}, f-string

var = "Max"
var2 = 3.2721

# %s
s_var = "the variable is %s" %var   # old method of string formatting - %s - string, %d - decimal/integer, %f - float
print(s_var)

# .format{}
b_var = "the variable is {:.2f}".format(var2) # - :.2f - number of float to print
print(b_var)
b_var1 = "the variable is {} and {}".format(var, var2) # second old method for multiple variables
print(b_var1)

# New Method - F-string

c_var = f"The variable is {var} and {var2}"
print(c_var)

c_var1 = f"the variable is {var} and {var2 * 2}"    # operational within the statement
print(c_var1)
