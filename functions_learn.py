# function - a set of code that can run whenever it is called
# re-usability, code reduction

# 2 steps to use a function
# create the function: declare and define a function
# Execute the function: u have to call the function using function_name

# syntax to create a function
# def - is a keyword used to create a function

# def function_name():
#     steps

# 1. Create the function
def sayhi():
    print("hi")

# 2. Call the function
sayhi()
sayhi()

"""
functions are two types
1. builtin function
    e.g : print(), int(), dict(), len(), type(), id(), dir()
2. user defined functions
    e.g : sayhi()
"""

# getting input from the user during runtime - use parameters in  the function
#------------------------------------------------------------------------------
# parameter - is a local variable given inside the parentheses of the function_name
# parameter will get the data from the function call

# argument is the data passed to the parameter from function call

def sayhello(user):    # user - is the parameter
    #user = "kamal" # local variable
    print(f"hello {user}")


sayhello("kamal")     # kamal - is the argument passed
sayhello("arjun")     # arjun - is the argument passed

def add(num1, num2):
    print(num1 + num2)

add(10, 90)
add(-1, 101)
add(0, 0)
add(-1, -1)

# to get the result of the function outside, return the result
# using the keyword return

# by default a function return None (NoneType)

def multiply(num1, num2):
    return num1*num2

a = multiply(2, 3)
print(a)

def return_multiple_data():
    return 1, 3, 4, 5

print(return_multiple_data())



def letter_count(string):
    c_count = dict.fromkeys(string, 0)

    for k in c_count.keys():
        c_count[k] = string.count(k)

    return c_count

print(letter_count("apple and pineapple are two different fruits"))
print(letter_count("jack and jill went up the hill"))