# Lambda Functions?
# Are called as anonymous function or nameless functions - a function without a name

# it used with a keyword called lambda
# will not have def and return keyword

# syntax for lambda

# lambda argumnets: expression

x = 5

add_10 = lambda a: a+10

print(add_10(x)) # the result of the expression will be returned

def add10(a):
    return a+10

print(add10(x))

y = lambda: 4
print(y())

def limit_validation(limit, number): # limit = "MAX", number = 31
    if limit=="MAX":
        return lambda value: value>number
    elif limit=="MIN":
        return lambda value: value<number

is_number_max = limit_validation("MAX", 27)
# is_number_max = lambda value: value > 31  # 15 > 31


print(is_number_max(15)) # False
print(is_number_max(32)) # True

add = lambda x,y=10: x+y

print(add(3))
print(add(3,5))

add_more_numbers = lambda *numbers : sum(numbers)

print(add_more_numbers(13,34,56,78,90))
print(add_more_numbers(13,34))