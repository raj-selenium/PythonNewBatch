#Programming Style

# Sequential

a= 10
b= 20
print(a+b)


# functional

def add(x,y):
    print(x+y)

add(10,20)
add(20,49)


# object oriented programming # class combines data and the operation performed on that data
class Calc:
    def __init__(self, x, y):
        self.x =x
        self.y = y

    def add(self):
        print(self.x + self.y)

    def minus(self):
        print(self.x - self.y)


calc1 = Calc(10,30)
calc1.add()
calc1.minus()

calc2 = Calc(40,30)
calc2.add()
calc2.minus()

# class


class BankAccount:
    acc_id
    balance
    transaction

    deposit()
    withdraw()
    get_transaction_details()

BankAccount("ACC123", 40000, [10000, 30000])


