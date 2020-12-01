# Scope - Local, Enclosed, Global, Builtin (LEGB)

"""
print(type(23))

def type(num):
    return 0

print(type(23))


fruit = "apple"  # global
a = 10 # global
def print_fruit(): # global
    a = 5 # local
    print(f"i have eaten {a} {fruit}s")

print_fruit()
print(f"i have eaten {a} {fruit}s")

def outer():
    a = 20 # enclosed
    def inner():
        a = 15 # local
        print(f"i have eaten {a} {fruit}s")
    inner()
    print(f"i have eaten {a} {fruit}s")

outer()

"""

def func():
    global a # global
    a = 10
    print(a)

func()
print(a)

def outer():
    a = 6 # enclosed
    def inner():
        nonlocal a #enclosed
        a = 7 #
        print(a) # 7
    inner()
    print(a) #7

outer()
print(a)

# global to make any local variable global
# nonlocal to make a local variable as enclosed

