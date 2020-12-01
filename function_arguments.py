def add(num1, num2):
    return num1+num2

print(add(23, 45)) # 23 and 45 are called positional arguments
print(add(45, 23))

# keyword arguments
def minus(num1, num2):
    return num1-num2

# pass arguments using parameters as keywords
# when using like this, the order is not required
print(minus(num2=30, num1=45))

def get_name(firstname, middlename, lastname):
    return f"{firstname.capitalize()} {middlename.capitalize()} " \
           f"{lastname.capitalize()}"

print(get_name("Aditya", lastname="kapoor", middlename="roy"))
print(get_name("aditya", "roy", "kapoor"))


# default argument/default parameter
# default arguments should come after positional arguments
def fullname(firstname, lastname="kapoor"):
    return f"{firstname.capitalize()} {lastname.capitalize()} "

print(fullname("Rishi", "kapoor"))
print(fullname("Ranbir"))
print(fullname("akshay", "kumar"))

# arbitrary arguments - any no of positional arguments
# by convention people use args, but it is not mandatory
# * is mandatory to represent arbitrary arguments
def calculate_average(*marks):

    total = 0
    if len(marks):
        for mark in marks:
            total += mark       # total = total + mark
        return total/len(marks)
    else:
        return 0

print(calculate_average(65))
print(calculate_average(65, 60))
print(calculate_average(45, 67, 89, 66, 56))
print(calculate_average(65, 60, 80))
print(calculate_average(65, 60, 80, 59, 66, 78, 90, 65, 45))
print(calculate_average())

# how to use arbitrary arguments:
# 1. if u have positional arguments, give them first,
# 2. if u have default parameters it should come after arbitrary arguments
#    and it should be represented as keyword argument in function call

def using_args(name, *args, std=12):
    print(args)
    print(*args)
    avg = calculate_average(*args)
    print(f"{name} studying {std} average is {avg}")

using_args("kamal", 45,67,89,48,70)

using_args("arjun", 45,67,89,48,70, std=3 )

# keyword arbitrary arguments - any no of keyword arguments
# it is represented by **kwargs, kwargs is by convention


def avg(**students):
    print(students)
    for k in students.keys():
        print(f"{k}'s average is {calculate_average(*students.get(k))}")

avg(kamal=(56,67,80), arjun=(78,89,90))

# 1. the kwargs should be the last argument










