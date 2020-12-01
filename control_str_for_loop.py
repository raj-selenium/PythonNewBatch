# for loop - for no of times, no of items

# range(stop) - it will produce a sequence of int numbers starting from 0 until the stop value
# range(start, stop, step) - it will start from the start position and go up to the stop

print(range(10)) # range(0,10)

a = range(10)


# iter, next
# iter() is a function that will create an iterator over an iterable
# next() is a builtin func, used to iterate over the iterator one item at a time
iterator = iter(a)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# it will throw StopIteration error , if u go beyond the limit

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

# syntax: for tmpVar in items:

# no of times
for i in range(10):
    print(i)

for i in range(2,10,2):
    print(i)


for i in range(20):
    print("kamal")

names = ["jamal", "kamal", "rajesh", "francis", "amal"]

# no of items
for name in names:
    print(name)

# print all the names that ends-with "mal"

for name in names:
    if name.endswith("mal"):
        print(name)

fruit = "apple"

length = len(fruit) # 5

# no of times
for i in range(length): # for i in range(5): 0-4
    print(fruit[i]) # fruit[0], fruit[1], ... fruit[4]


# no of items
for letter in fruit:
    print(letter)


# else, break, continue

numbers = [23,46,78,99,84,121]

for num in numbers:
    if num%21 == 0:
        print(num)
        break

for num in numbers:
    print(num*5)
else: # the loop is exited cleanly, then else will get executed
    print("loop completed")

for num in numbers:
    if num == 99:
        print("found")
        break
else:
    print("not found")


for i in range(5,30,5):
    if i == 15:
        continue

    print(i)

for i in range(1,11):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")








