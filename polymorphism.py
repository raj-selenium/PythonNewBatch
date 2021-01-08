class Parent:
    def method1(self):
        self.__private_method()
        print("I am method1")

    def method2(self,*args,**kwargs):
        if args:
            print(args)

        if kwargs:
            print(kwargs)

    def __private_method(self):
        print("I am private method")

p1 = Parent()

# method overloading
# same method -   having different no of parameters or different type of parameters
p1.method2()
p1.method2(1)
p1.method2("kamal")
p1.method2(1,2,3,name="kamal",age="35")

# method overriding
# rewriting the same method in child, which is already available in parent
# when u create an object for the child it will only call the overriden method of child
class Child(Parent):
    def method1(self):
        print("I am method1 in child")


c1 = Child()

c1.method1()
p1.method1()

# operator overloading
# same operator behave differently with different data types
print(1+2)
print("1"+"2")

