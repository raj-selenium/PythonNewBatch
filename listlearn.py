# List is a compound data type - collection of several data inside a particular variable

name = "kamal" # singular items inside a variable
age = 35 # singular items inside a variable


# List
# 4 characteristics of List
# 1. ordered - maintains same order as represented or as given - yes
# 2. indexed - retrieve  item based on its position - yes
# 3. Allows Duplicate? - yes
# 4. Mutable / Changeable - yes

# List - represented by class list
# it is represented in code by items inside the [] and each item separated by comma
# list() - builtin function to convert or to create a list

names = ["kamal","kandan","kabilan"]  # homogenous data
person_data = ["kamal", 35, 30000.00, "Indian", "Software Trainer"] # hybrid data

fruits = ["apple"] # list with single item

print(type(fruits))

empty_list1 = list()
print(empty_list1)
empty_list2 = []
print(empty_list2)

# adding an item to the list
# append() - will append an item at last
fruits.append("pineapple")
fruits.append("custardapple")
fruits.append("banana")
print(fruits)

# insert will add an item at the given position
fruits.insert(1, "guava")
print(fruits)



# length or no of items inside a list:
print(len(fruits))

# indexing - based on position doing operations
# index position starts from 0
# retrieval
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])
# print(fruits[5]) # IndexError: list index out of range

# Negative index
print(fruits[-1])

# slicing can be used in list
print(fruits[2:4])
print(fruits[:])
print(fruits[::2])
print(fruits[::-1])

# Modifying (mutability/changeable)

fruits[0] = "grapes" # replaces "apple" at position 0
print(fruits)

print(name[0])
# name[0] = "J"  # TypeError: 'str' object does not support item assignment

# fruits[5] = "apple" # IndexError: list assignment index out of range

fruits.insert(10,"apple")
print(fruits)

fruits.append(["muskmelon", " watermelon"])
print(fruits)
print(fruits[6][0]) # retrieving an item inside a list item # fruit[6] yields list
print(fruits[0][0]) # retrieving a char string from a string item # fruit[o] yields string

fruits.extend(["muskmelon", "watermelon"])
print(fruits)

# string will be converted into a list of characters
print(list(name))


# remove items from a list

# by index
print(fruits.pop()) # return the item it is removing
print(fruits)

print(fruits.pop(6))
print(fruits)

# print(fruits.pop(8))  # IndexError: pop index out of range

# by item itself
fruits.remove("pineapple")
print(fruits)

fruits.reverse()
print(fruits)

# adding a duplicate value
fruits.append("apple")
print(fruits)

print(fruits.count("apple"))

print(fruits.index("apple"))
print(fruits.index("apple", 2))
#print(fruits.index("apple", 2,4)) #ValueError: 'apple' is not in list

fruits.sort()
print(fruits)

list2 = fruits.copy()
print(list2)

list2.clear()
print(list2)

del fruits[1]

print(fruits)

del fruits
# print(fruits) # NameError: name 'fruits' is not defined

# we can combine two or more liste by using + operator
print([1,2,3]+[3,4,5,6,7])

# TypeError: can only concatenate list (not "int") to list
# print([1,2,3]+4)

# list * int
print([1,2,3]*2)
print([1,2,3]*5)





