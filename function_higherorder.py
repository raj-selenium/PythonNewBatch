#function itself is an object


def add():
    return 10+20

b = add
print(b())

print(type(add))
print(add)

# here func is a higher order function
# when a function takes another function reference as parameter

def func(param1):    # add
    print(param1())  # add()

func(add)

def outer():
    def inner():
        return 20
    return inner()

c = outer()
print(c)

def sayhi():
    def inner():
        return "hi"
    return inner

d = sayhi()
print(d)
print(d())

names = ["kamal", "arjun", "amal", "jamal", "vimal", "komal", "arjitt"]

"""
cap_names = []
for name in names:
    cap_names.append(name.capitalize())

print(cap_names)
"""
cap_names = map(str.capitalize, names)
print(list(cap_names))

def my_filter(name):
    if name.endswith('mal'):
        return name


filter_names = filter(my_filter, names)

print(list(filter_names))

# lambda expressions - nameless functions (anonymous function)

print(list(filter(lambda name: name.startswith('a'), names)))

# scope
# lambda
# comprehension
# closure
# decorators


