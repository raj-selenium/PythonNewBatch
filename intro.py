# comments   - is for the fellow programmer (instruction for humans)
# statements - is for the computer (instruction for the machine to do something)

# comment is represented with # (hash or octothrope) symbol

# Statements will be read by the computer and it will execute the program line by line

a = 11
print(a)


# A computer program that reads and executes a program is called as Interpreter or
# Compiler

# convert the Program written in high level languages java, python, C#
# into machine understandable language

# Interpreter and compiler:
# Interpreter will convert a program line by line
# Compiler will convert the whole in to machine language and then execute the whole program

# python is an interpreted language

# keywords, operators(+ # _ =), pre defined commands, names and data
# keywords are reserved words to define the syntax and structure of the Python language.

if a > 10:
    pass


sentence = "jack and jill went up the hill"

print(sentence.count(" "))

# data - piece of information (data, datum)
# datatype - classification of data
# price = 12000
# model = M31s  Text(String)
# brand = samsung
# GST = 1200
# price + GST = total price =

# variable, data , datatype


def calculate_price(base_price, tax, discount10_):
    print(base_price+tax-discount10_)


calculate_price(10000, 1000, 500)
calculate_price(20000, 2000, 1000)


# namespace                                 data
#------------                           ------------
# a ------------------------------->     abc123  =  int data  11
# sentence------------------------->     abc124  =  string data ""
# calculate_price ----------------->     abc2323 =  function() data
        # base_price  ------------>            20000
        # tax         ------------>            2000
        # discount     ----------->            1000


# Identifiers - variables, function_name, class_name

# rules for naming identifiers:
# 1. Identifiers cannot be keywords
# 2. Identifiers should only contain alphabets, numbers and underscore
# 3. Identifiers cannot start with numbers (it can start with alphabets and underscore)
# 4. Identifiers are case sensitive - name, Name, NAME


# Different types of data in python Numbers, Strings, Boolean