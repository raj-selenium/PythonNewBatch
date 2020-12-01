# Set is also a compound data type

# set
# 4 characteristics of Set
# 1. ordered - maintains same order as represented or as given - no
# 2. indexed - retrieve  item based on its position - no
# 3. Allows Duplicate? - no
# 4. Mutable / Changeable - yes

# frozenset
# 4 characteristics of frozenset
# 1. ordered - no
# 2. indexed - no
# 3. Allows Duplicate? - no
# 4. Mutable / Changeable - no

# a set doesnt allow mutable data inside it like list, dict, set etc..

# class set
# set(), frozenset()
# set are represented by {} and values separated by commas
# empty_set - set()
# empty_frozenset - frozenset()

set1 = {1, 2, 3, 4}
set2 = {"apple", 1.78, 34, False, (1,2)}

print(set1)
print(set2)

print(type(set1))

empty_set1 = set()
print(empty_set1)

#set3 = {[1,2], [3,4]} #ypeError: unhashable type: 'list'
#print(set3)

set4 = {1, 3, 4, 5, 3, 5, 5, 6, 7, 1}
print(set4)

print(len(set4))

# print(set4[0]) # TypeError: 'set' object is not subscriptable

# mathematical representation of set

# totally there are 80 students and the roll number is from 1 to 80
# in a class all the even roll number students enrolled themselves in physics
# all the students whose roll number is divided by 5 enrolled in chemistry
# all the students whose roll number is divided by 7 enrolled in math

s_phy = set(range(2,81,2))
s_chem = set(range(5,81,5))
s_math = set(range(7,81,7))

print(s_phy)
print(s_chem)
print(s_math)

# how many students are enrolled in at least one subject?
# how many students has not enrolled at all for any subject?
# how many students are enrolled in both phy and chem
# how many students are enrolled in both phy and math
# how many students are enrolled in both math and chem
# how many students are enrolled in all phy, chem, math


s_atleat_one_subject = s_phy.union(s_chem).union(s_math)
print(len(s_atleat_one_subject))

s_no_subjects = set(range(1,81)).difference(s_atleat_one_subject)
print(len(s_no_subjects))

s_studying_all = s_phy.intersection(s_chem).intersection(s_math)
print(s_studying_all)
print(len(s_studying_all))

# student enrolled only in math

s_only_math = s_math.difference(s_phy.union(s_chem))
print(s_only_math)

s_only_phy = s_phy.difference(s_math.union(s_chem))
print(s_only_phy)

s_only_chem = s_chem.difference(s_math.union(s_phy))
print(s_only_chem)

# students enrolled in only one subject

s_only_one_sub = (s_only_chem.union(s_only_math).union(s_only_phy))
print(s_only_one_sub)

print(len(s_only_one_sub))


setA = {1,2,3,4,5}
setB = {2,4,6,8,10}

# union - all the values, without duplicates
print(setA.union(setB))
print(setA | setB)  # | - union

# intersection, only values that are common in the sets
print(setA.intersection(setB))
print(setA & setB)  # & - intersection

# difference, only values in one set and not in other set

print(setA.difference(setB))
print(setB.difference(setA))
print(setA - setB) # - represent difference

# Symmetric difference, unique values from each set

print(setA.symmetric_difference(setB))
print(setA ^ setB) # ^ - symmetric difference

setA.add(20)
print(setA)

print(setA.pop())
print(setA)

setA.remove(3)
print(setA)

setA.discard(11)
print(setA)

setA.update([1,2,3])
print(setA)


fsetA = frozenset(setA)
fsetB = frozenset(setB)
print(fsetA)
print(fsetB)














