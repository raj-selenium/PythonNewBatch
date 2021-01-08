# Datatypes - Primitive data types and Composite Data type

# Primitive or Simple Data type:
# Numbers - int, float, complex
# Text - str
# Boolean - bool (True or False)

# Numbers
#int - whole numbers
"""
a  = 10

print(type(a))  #<class 'int'>

# datatype - i mean it is a class integer = 10, 20, 3

# float - numbers with fractional part (.)

b = 20.0 # 0.000000000000000001,  0.6, 0.0, 20000000000000000.0

print(type(b)) #<class 'float'>

# complex

c = 10+6j # j -> sqrt(-1)

print(type(c)) # <class 'complex'>
print(c.imag)
print(c.real)

# bin(), oct(), hex()
print(bin(12)) #0b
print(hex(12)) #0x
print(oct(12)) #0o

# int()
print(int(0b1100))
print(int("23"))
print(int(2.999999))

# u can convert one number system to another by using the functions
print(bin(0o14))

# float() is used to convert int to float
print(float(12))
print(float("12.35"))  # 12.35

#convert int, float and string containing complex to complex
print(complex(12))
print(complex(12.3))
print(complex("12+5j"))

# we cannot convert a complex to int or float

#String data type
#-----------------

# a string is a sequence of characters (alphabet, number, symbol)
# represented within single quotes or double quotes
# ex: "234rty90><?'"
# ex: 'appl3'

print("KFC's fried chicken")
print('I am "Ironman"')

print("apple")
print('apple')

print("123")
print(123)

fruit = "apple"

print(id(fruit))
print(id("apple"))

fruit2 = "apple"
print(id(fruit2))

# String are immutable

# 0nce a string is created in memory, u cannot modify or delete the string

fruit = "guava"

# indexing in string - positional index (it starts from 0)
#  g   u   a    v    a
#  0   1   2    3    4

print(fruit[0])
print(fruit[1])
print("guava"[2])
print(fruit[3])
print(fruit[4])
# print(fruit[5]) # IndexError: string index out of range

# length of the string

print(len(fruit))  #5

print(fruit[len(fruit)-1])   #5-1 = 4 => fruit[4] => a
print(fruit[len(fruit)-2])   #5-2 = 3
print(fruit[len(fruit)-3])   #5-3 = 2
print(fruit[len(fruit)-4])   #5-4 = 1
print(fruit[len(fruit)-5])   #5-5 = 0

# neagtive index (index starts from -1)

# g   u    a    v    a
# -5 -4   -3   -2   -1

print(fruit[-1])
print(fruit[-2])
print(fruit[-3])
print(fruit[-4])
print(fruit[-5])

# slicing -> used to take a substring of the string
# g     u       a       v       a
# 0     1       2       3       4
# -5    -4      -3      -2      -1

# [start:stop:step]
# start - starting index from where u want to start in the string
#       - mandatory (by default it starts from 0]
# stop  - stop index (before which position u want to stop in the string)
#       - stop index is excluded
#       - mandatory (by default it stops in len)
# step  - how many position u want to move from the start index for each value until  the stop
#       - not mandatory (by default step is 1)

print(fruit[2:4])
# start position 2, stop position 4 (4 excluded), step by default is 1
# guava ---  av

print(fruit[:])
# start position by default 0
# stop position by default len(fruit) = 5 (5 excluded)
# step, by default is 1
# 0, +1 = 1, +1 = 2, +1 = 3, +1 = 4
# guava ---- guava

print(fruit[::2])
# start 0, stop (5), step = 2
# 0, +2 = 2, +2 = 4
# guava  ---- gaa

print(fruit[::-1])
# start - 0, stop (5), step -1
# 0-1 = -1, +(-1) = -2, +(-1) = -3,-4, -5
# guava  -- avaug

print(fruit[-1:-5:-1])
#-1 -1-1 -2-1  -3-1
# guava --- avau

#print(fruit[2:-20:-1]) # this is not going to return any string
#2, 2-1 = 1,  1-1 = 0
#guava   aug

#String Methods:

# changing cases
fruit = "apple"

print(fruit.upper())
print(fruit)

sentence = "Jack and Jill went up the hill."

print(len(sentence))
print(sentence.lower())
print(sentence.title())
print(sentence.capitalize())
print(sentence.swapcase())

# finding the position of substring
# substring is a part of the string
print(sentence.index("ill"))
print(sentence.index("ill",11))
print(sentence.index("n"))
print(sentence.index("n",7))
# print(sentence.index("n", 7, 15)) #ValueError: substring not found

print("How many n in sentence?", sentence.count("n"))
print("How many 'ill' in sentence?", sentence.count("ill"))
print("How many space in sentence?", sentence.count(" "))
print(sentence.count("z")) # 0


# what characters a string contains inside it

num = "23"

print(num.isnumeric())

alphabets = "abcdefg"

print(alphabets.isalpha())

alnum = "abc123"

print(alnum.isalnum())
print(alnum.isalpha())
print(alphabets.isalnum())

allchars = "abc 123"
print(allchars.isalnum())

sentence = "i like fruits and vegetables"

print(sentence.split())
print(sentence.split("e"))
print(sentence.split("and"))
print(sentence.split(" ",2))
print(sentence.split("z"))

mylist = ["I", "am", "Ironman"]

print(" ".join(mylist))
print("_".join(mylist))

#replace

mystring = "apple"

print(mystring.replace('e','3'))

print(mystring.replace("p","9"))

print(mystring.replace("pp",""))
print("I am an apple".replace(" ","",2))

# endswith, startswith
word = "good morning"

print(word.startswith("go"))
print(word.endswith("ind"))

filename = "data.xlsx" # ['data','xlsx']

ext = filename.split(".")[-1]  # 'xlsx'
print(ext.startswith("xls")) # if True excel sheet

# String formatting

name = "arjun"
age = 7
std = 3

exp_sentence = "My name is arjun. I am 7 years old. I am studying Grade 3."

# 1. concatenation
# str - builtin function, used to convert any data into string

print("custard "+"apple")

print("My name is "+name+". I am "+str(age)+" years old. I am studying Grade "+str(std)+".")

# 2. % formatter %s, %d, %f

sentence = "My name is %s. I am %d years old. I am studying Grade %d."

print(sentence%(name, age, std))
print(sentence%("arjitt",4,0))
print(sentence%("kavitha",14,10))

# 3. format method

sentence = "My name is {}. I am {} years old. I am studying Grade {}."

print(sentence.format(name, age, std))
print(sentence.format("arjitt", 4, 0))

# u can place the position values of the data and pass them wherever u want
# and as many times as u want
sentence = "My name is {0}. I am {2} years old. I am studying Grade {2}."
print(sentence.format("arjitt", 0, 4))

# 4. f formatter
sentence = f"My name is {name}. I am {age} years old. I am studying Grade {std}."

print(sentence)
"""
# multi line string

#mu_string = """This is an article.
#I am going to write about multi-line string in python.
#
#    Multi               line string is represented by \"\"\"\"\"\" or ''''''."""
#
#print(mu_string)

# escape characters  \

print("I am \"Ironman\"")

# special escape characters
# \n - new line
# \\ - \
# \" - "
# \' - '
# \b - backspace
# \t - tab

print("c:\\\\new folder\\table")

print("ate" in "hate")

fruit = "apple"

for char in fruit:
    print(char)


# 3. bool data type

# represents True or False

# boolean comes form a class called bool

isAvailable = True

print(isAvailable)

# type is a builtin function, used to get the class of the data

print(type(isAvailable))

# bool() - builtin function, used to convert any data to boolean

print(bool(10))
print(bool(1))
print(bool(0))

# any data default value will give False, when converted to bool

print(int())
print(float())
print(str())
print(complex())
print(list())
print(tuple())
print(set())
print(dict())
print(bool())

print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool(set()))
print(bool({}))
print(bool(False))

print(bool(10))
print(bool(0.01))
print(bool(1j))
print(bool(" "))
print(bool([1,2]))
print(bool((1,2)))
print(bool({1,2}))
print(bool({"name":"arjun"}))
print(bool(True))

# bool data is used for checking conditions
# comparison
name = "kamal"
age = 35
std = 20

sentence = "My name is {name}. I am {age} years old. I am studying Grade {std}."
print(sentence.format(name="arjitt", std=0, age=4))
print(sentence.format(name=name, std=std, age=age))




