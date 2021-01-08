num = 10
print(type(num))

def person_details(name, age):
    print(name)
    print(age)

print(type(person_details))

num1 =10 # 30
num2 ="10" #101010


class Person:
    species = "homosapiens"
    def __init__(self, n, age, g="M"):
        self.name = n # p1.name = "kamal"
        self.age = age # p1.age = 35
        self.gender = g # p1.gender = "M"

    def speak(self): #p1
        #"kamal is speaking"
        print(self.name+" is speaking")
        print(self.species)

print(Person.species)

Person.species = "Neandarthal"

print(Person.species)

p1 = Person("kamal", 35)
p2 = Person("kavitha", 36, "F")
print(p1.species)
print(p2.species)
print(p1.name)
print(p2.name)


p1.speak()
p2.speak()

# class and object
# A class is a generalized concept, it will have the structure -  blueprint or template
# An object is something specific and created in memory

class ABC_Employee:
    company_name = "ABC pvt ltd"  #class attribute

    def __init__(self, id, fname, lname, ads, dob, designation, sal, blood_group):
        self.emp_id = id  # instance attributes
        self.fname = fname
        self.lname = lname
        self.address = ads
        self.dob = dob
        self.designation = designation
        self.salary = sal
        self.blood_group = blood_group

    def do_work(obj): # instance method
        print(f"{obj.fname} {obj.lname} is doing the {obj.designation} job in {obj.company_name}")


    def get_details(self):
        print(f"""Name : {self.fname} {self.lname}
Address: {self.address}
DOB: {self.dob}
Designation: {self.designation}
Blood Group: {self.blood_group}
Employee ID: {self.emp_id}""")

    @classmethod
    def get_company_name(cls):
        print(f"Company_name: {cls.company_name}")


    @staticmethod
    def is_adult(age):
        if age >= 21:
            print("is Adult")
        else:
            print("not Adult")



# attributes - 2 types
#             - 1. characteristics common to all the Employee - class attributes
#             - 2. characteristics specific to an Employee    - object or Instance attributes

# methods - 3 types
#           - 1. A method that only uses class attributes - class methods
#           - 2. A method that uses at-least one instance attributes - Instance methods
#           - 3. A method that doesn't use any attributes - static methods

ABC_Employee.get_company_name()
ABC_Employee.is_adult(19)
#ABC_Employee.get_details()

e1 = ABC_Employee("ABC123", "Steve", "Martin", "California", "07-12-1986", "Manager", "6000", "B+")
e2 = ABC_Employee("ABC124", "Peter", "Parker", "California", "08-29-1987", "Developer", "5000", "A+")

e1.do_work()
e2.do_work()

e1.get_details()
e1.address = "New York"
e1.get_details()
e2.get_details()

e1.get_company_name()
ABC_Employee.company_name = "DBA Pvt Ltd"
e1.get_company_name()
e2.get_company_name()

e1.is_adult(23)

# class, object
# attributes and methods

# oops principles
# Inheritance       
# Encapsulation - data hiding
# Abstraction
# Polymorphism

class Person:
    def speak(self, *args, **kwargs):
        for value in args:
            print(value)
    def walk(self):
        print("max speed 20")
    def cook(self):
        pass

p1 = Person()
p1.speak(1,2)
p1.speak(10,20,30,40)
p1.speak()
p1.speak("custard","apple")
p1.walk()

class SuperHuman(Person):
    def walk(self):
        print("max speed 2000")

# method overloading, overriding
# operator overloading


flash = SuperHuman()
flash.walk()

print(1+2)
print("1"+"2")
print([1]+[2])







