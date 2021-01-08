# Opening a file:


with open("fruits.txt") as f:
    print(f.readable())
    print(f.read(5))
    print(f.read(5))

with open("fruits1.txt", mode="w") as f:
    print(f.readable())
    print(f.writable())
    string = "strawberry\nraspberry\nblackberry"
    f.write(string)

with open("fruits1.txt", mode="w") as f:
    fruit_list = ["Strawberry\n", "Raspberry\n", "Blackberry\n"]
    f.writelines(fruit_list)

with open("fruits1.txt", mode="a") as f:
    fruit_list = ["BlackCurrant\n", "Mango\n", "Jackfruit"]
    f.writelines(fruit_list)

import os

print(os.getcwd())
print("Path exists", os.path.exists("veggies.txt"))
os.remove("veggies.txt")
print("Path exists", os.path.exists("veggies.txt"))

with open("veggies.txt", mode="x") as f:
        vegg_list = ["Carrot\n", "Cucumber\n", "Onion\n"]
        f.writelines(vegg_list)

"""
with open("veggies.txt", mode="r+") as f:
    print("readable", f.readable())
    print("writable", f.writable())
    print("seekable", f.seekable())
    print(f.tell())
    print(f.read(10))
    print(f.tell())
    veg_str = "Capsicum\nTomato"
    f.write(veg_str)
    f.seek(0)
    print(f.read())


with open("veggies1.txt", mode="w+") as f:
    vegg_list = ["Carrot\n", "Cucumber\n", "Onion\n"]
    f.writelines(vegg_list)
    print(f.tell())
    f.seek(10)
    print(f.tell())
    veg_str = "Capsicum\nTomato"
    f.write(veg_str)
    f.seek(0)
    print(f.read())



with open("veggies1.txt", mode="a+") as f:
    vegg_list = ["Carrot\n", "Cucumber\n", "Onion\n"]
    f.writelines(vegg_list)
    print(f.tell())
    f.seek(10)
    print(f.tell())
    veg_str = "Capsicum\nTomato"
    f.write(veg_str)
    f.seek(0)
    print(f.read())
"""
# modes r w a x r+ w+ a+

with open("krishna.jpg", mode ="rb") as f:
    file_content = f.read()
    with open("krishna1.png", mode= "wb") as f1:
        f1.write(file_content)


