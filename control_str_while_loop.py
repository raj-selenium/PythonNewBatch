# while - based on condititon
"""
a = 11

if a >= 10:
    print("if - a is greater than or equal to 10")
else:
    pass # i ll implement in future

while a >= 10:
    print("while - a is greater than or equal to 10")
    a = a-1
else:
    print("loop is completed")


print("code completed")

"""
"""
import random
num = int(input("enter a number between 1 to 10, 0 to exit: "))

# random is a module, which contains several method to generate random numbers

while num != 0:
    rand_num = random.randint(1,10)
    if rand_num == num:
        print(rand_num, num, "are same", ", you win")
    else:
        print(rand_num, num, "better luck next time")

    num = int(input("enter a number between 1 to 10, 0 to exit: "))
else:
    print("U have pressed 0, Thanks for playing")


print("Code Completed")


# break

import random
num = int(input("enter a number between 1 to 10, 0 to exit: "))

count = 1
while num != 0:

    rand_num = random.randint(1,10)
    if rand_num == num:
        print(rand_num, num, "are same", ", you win")
    else:
        print(rand_num, num, "better luck next time")

    if count >= 3:
        print("Exceeded maximum play time")
        break

    num = int(input("enter a number between 1 to 10, 0 to exit: "))

    count += 1

else:
    print("U have pressed 0, Thanks for playing")

"""
# continue

token_number = 71

while token_number != 0:
    token_number -= 1

    if token_number % 4 == 0:
        print(token_number, "allowed")
        continue

    print(token_number, " u r not allowed ")






