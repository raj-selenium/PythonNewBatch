# closure
# the function should have an inner function and return the same
# the function should have an enclosed variable
# the enclosed variable should be used inside the inner function

def outer(a,b):
    def inner():
        return a*b
    return inner


x = outer(10,15)

print(x.__closure__[0].cell_contents)
print(x.__closure__[1].cell_contents)
print(x())

class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def multi(self):
        return self.a*self.b

c1 = Calc(10,15)

print(c1.a)
print(c1.b)
print(c1.multi())