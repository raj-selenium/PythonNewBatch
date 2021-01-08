# error

# print(hi) #NameError

"""  # SyntaxError
if True
    print("hello")
"""

""" #IndentationError
if True:
print("hello")
"""


# try    - where ur code which is expected to give exception is given
# except - which will handle the exception
# finally- which will run the codes under it, whether u handle an exception or not

# try cannot come alone, either it has to be tagged with except or finally or both
# except block can be given multiple times

"""
a = int(input("Enter a denominator: "))
try:
    print(10/a)
except ZeroDivisionError as e:
    print(e)
    print("Denominator cannot be a zero")
    
print("This code will run only when u handle the exception")

"""
"""
a = int(input("Enter a denominator: "))

try:
    print(10 / a)
finally:
    print("this line of code will run even if u DON'T handle exception")

print("This code will run only when u handle the exception")
"""

"""
try:
    a = int(input("Enter a denominator: "))
    print(10 / a)
except ZeroDivisionError as e:
    print("Denominator can not be zero")
except ValueError as e:
    print("Input cannot be a character other than digit")
finally:
    print("this line of code will run even if u DON'T handle exception")

print("This code will run only when u handle the exception")
"""


"""
try:
    a = int(input("Enter a denominator: "))
    print(10 / a)
except ZeroDivisionError as e:
    print("0")
except ValueError as e:
    print("Please enter only numbers")
    a = int(input("Enter a denominator: "))
    print(10 / a)
except Exception as e:
    print(e)
    print("This input is not valid")

"""

salary = int(input("Enter ur salary: "))

if salary<10000:
    raise Exception("Salary cannot be lesser than 10000")