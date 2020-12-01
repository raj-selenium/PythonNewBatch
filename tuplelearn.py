# tuple - is also a compound data type like list
# tuple
# 4 characteristics of tuple
# 1. ordered - maintains same order as represented or as given - yes
# 2. indexed - retrieve  item based on its position - yes
# 3. Allows Duplicate? - yes
# 4. Mutable / Changeable - no

# list is mutable, whereas tuple is not
# once u create a list u can always modify it
# once u create a tuple u can not modify it


# tuple is represented by (), each value separated by commas
# class tuple
# tuple() to create or convert one data to tuple

tuple1 = (1, 2, 3, 4)
tuple2 = ("apple", "banana", "orange", "kiwi")
tuple3 = (1, "apple", 2.0, 3+5j, True, [1, 2, 3])

empty_tuple = tuple()
empty_tuple1 = ()

print(tuple1)
print(tuple2)
print(tuple3)
print(empty_tuple)

list1 = [2,4,6,8]

tuple4 = tuple(list1)
print(tuple4)

print(tuple("apple"))

# packing and unpacking
a = 1, 2, 3, 4  # packing => a = (1, 2, 3)

print(type(a))

a1, a2, a3, a4 = a # unpacking  => a1 = 1, a2 = 2, a3 = 3, a4 = 4

print(a1)
print(a2)
print(a3)
print(a4)

# only during the assignment, a tuple can be represented without ()

# Single valued tuple:
# a single valued tuple should always followed by a comma

b1 = 1
b2 = (1)
print(type(b1))
print(type(b2))

c1 = 1,

c2 = (1,)
print(type(c1))
print(type(c2))

# 1. ordered - maintains same order as represented or as given - yes
tuple2 = ("apple", "banana", "orange", "kiwi", "pineapple", "guava", "apple")
print(tuple2)

# 2. indexed - retrieve  item based on its position - yes
print(tuple2[0])
print(tuple2[3])
print(tuple2[5])

print(tuple2[1:4])

# 3. Allows Duplicate? - yes
print(tuple2[0])
print(tuple2[-1])

# 4. Mutable / Changeable - no

# tuple2[5] = "avacado" # TypeError: 'tuple' object does not support item assignment


# methods of a tuple:

print(tuple2.index("apple"))   # 0
print(tuple2.index("apple",1)) # 6
#print(tuple2.index("apple",2,5)) # ValueError: tuple.index(x): x not in tuple

print(tuple2.count("apple"))   # 2
print(tuple2.count("grapes"))  # 0

# adding two or more tuples
tuple5 = (1, 2, 3 ,4)
tuple6 = (5, 6, 7, 8)
print(tuple5 + tuple6)

# duplicating

print(tuple5 * 2)
print(tuple5 * 3)

# inserting a value inside a tuple # 1, 2, 10, 3, 4

tuple5 = tuple5[0:2] + (10,) + tuple5[2:4] # re-assigning tuple5
#   tuple5[0:2] = (1,2)
#   + (10,)  = (1, 2, 10)
#   tuple5[2:4] = (3,4)
#   (1, 2, 10) + (3, 4) = (1, 2, 10, 3, 4)
#   tuple7 = (1, 2, 10, 3, 4) # assigning to a new variable
#   tuple5 = (1, 2, 10, 3, 4) # reassigning to already available variable

print(tuple5)

# when u pass a tuple to any function, u can pack and unpack on the go










