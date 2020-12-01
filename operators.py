# 1. Arithmetic ops
# +   -   *   /    //    %    **

num1 = 20
num2 = 3


print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1//num2)   # this will yield quotient - floeer division
print(num1%num2)    # this will yield remainder
print(num1**num2)   # power symbol

print("custard"+"apple") # concatenate a str with another str
print("123" * 3) # multiply the str with int
print("Hi" * 3)


# print("apple"+3) # TypeError: can only concatenate str (not "int") to str
print("apple"+str(3))
print(int("123")+3)
print(-(num1))

"""
+   __add__
-   __sub__
*   __mul__
/   __divmod__
//  __floordiv__
%   __mod__
**  __pow__
"""

# 2. comparision ops   - result will be boolean (True/False)

# num1 = 20, num2 =3
print(num1 > num2)  # __gt__
print(num1 >= num2)  # __ge__  num1 greater_than or equal_to num2
print(num1 < num2)  # __lt__
print(num1 <= num2) # __le__
print(num1 == num2) # __ eq__  # the values are equal
print(num1 != num2) #__ne__ # the values are not equal

#str values will use comparision operators
#it will compare the ascii value of a character one by one.

# 3. assignment ops   =

name = "kamal"
age = 20

#the value/ data/ object on the rhs is assigned to the variable on lhs

a = 10 # a is 10

a = a+10  # a is 20

a += 10  # is equal to (a = a+10)
print(a)
a -= 10
print(a)
a *= 5
print(a)

# logical operators
# and    or    not
# and - if all the values are True, then the result will be True
# or  - if any one value is True, then the result will be True
# not - True will become False and Vice versa

num1 = 10

num2 = 6

num3 = 6

print(num1>num2 and num1>num3)
print(num1>=num2 and num1>=num2)
print(num2==num3 and num1>num2 and num1>num3 and num1<num2)

print(num2==num3 or num1<num2)

print(not num2==num3)
print(not num2>num3)

# 5. identity op  - is   - yield True or False as result
# it will compare if both the id of the value is same

# id - builtin function - it will return the identity of each object
print(id(num1))
print(id(num2))
print(id(num3))

print(num1 is num2)
print(num2 is num3)

# 6. membership op  - in  - yield True or False as result
# it will verify if an item is available inside the object

print("at" in "cat")
print("at" in "bata")
print(7 in [1,2,3,4])
print(7 in [1,2,3,4,7])

# 7. Bitwise









