# control structure - based on a decision - controlling the flow of execution
# 1. selection
# 2. Iteration

# selection = based on a condition, i want to execute a set of statements
#           - which set of statements the program has to execute
#           - if, else, elif

# Iteration = based on a condition, i want to execute the same set of statements again and again
#           = based on no of items, for each item i wan tot perform the same task
#           = based on no of times
#           - while, for

# break, continue

# selection
# e.g: browser = chrome: i want to open chrome browser
#      browser = ff: i want to open ff browser


# iteration
# e.g: 20 integer items in a list
#      multiply each int item in the list by 2
#      for each item i will repeat the statement multiply_by_2

# selection
# __________

# input() - builtin function, to get an input from the user
#         - the result will be returned as a String
#         - the string within the input() is called as prompt


num = input("Enter an Integer number: ")

# if condition:
#   statements  # True - these statements will get executed

"""
if num.isnumeric():
    num = int(num)
    print(num)

print("code completed")
"""

# else:
#   statements  # False - these statements will get executed

# if block can appear separately
# there should be only one if block under a single control structure
# else can appear along with if only
# there should be only one else block under a single control structure
"""
if num.isnumeric():
    num = int(num)
    print(num)
else:
    print("U have not entered an Integer number")
    
print("code completed")
"""

# nested if-else
"""
if num.isnumeric():
    num = int(num)
    if num%2 == 0:
        print("The given number is Even")
    else:
        print("The given number is Odd")
else:
    print("U have not entered an Integer number")

print("code completed")
"""


# elif  - else if
# elif will only run if if statement is false
# elif can exist with if only
# elif should be followed by if
# if there is an else part, it should come after elif
# elif should have a condition



num = int(num)
if num == 0:
    print("the given number is neutral")
elif num < 0:
    print("the given number is negative")
#elif num > 0:
else: # if every condition is false, then else will execute
    print("the given number is positive")


    

