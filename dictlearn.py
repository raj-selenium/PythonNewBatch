# dict is also a compound data type
# dict always stores a data in key and value pair

# fruit list
#------------
# apple - 30
# banana - 12
# kiwi - 4
# guava - 15
# watermelon - 2

# key is also a data type - it should be an immutable data type
# key should always be unique in a dictionary

# class dict
# dict() - in built function used to create  a dict object
# {} - a data inside the dictionary will be a key and value
# each key and value pair separated by commas
from functions_learn import letter_count

dict1 = {"apple":30, "banana":12, "kiwi":4, "guava":15, "watermelon":2}
print(dict1)
print(type(dict1))

dict2 = dict(apple=30, banana=12, kiwi=4, guava=15, watermelon=2)
print(dict2)

# the dict() will allow only the str as key

dict3 = {1:"one", 2:"two"}
print(dict3)

# dict4 = dict(1="one", 2="two")

# there is no positional index in dictionary
print(dict1["kiwi"]) #we can use only key as the index in dict
print(dict3[1])

# key cannot be a duplicate
dict4 = {"carrot":34, "beetroot": 4, "carrot":4}
print(dict4)

# u can modify the value of a dictionary
dict4["beetroot"] = 6
print(dict4)

dict4["beans"] = 15
print(dict4)

del dict4["carrot"]
print(dict4)

print(dict1.keys())
print(dict1.values())
print(dict1.items())

for k in dict1.keys():
    print(k)

for v in dict1.values():
    print(v)

for item in dict1.items():
    print(item)

for k,v in dict1.items():
    print(k,v)

for k in dict1:
    print(k)

for k in dict1:
    print(dict1[k])

print(dict1.pop("kiwi"))
print(dict1)

print(dict1.popitem())
print(dict1)

dict1.update(watermelon=5, guava=4)
print(dict1)

print(dict1.get("apple"))

mylist = ["kamal","amal","jamal"]

rank_mylist = dict.fromkeys(mylist,0)
print(rank_mylist)

sentence = "arjun and arjitt are brothers"
print(letter_count(sentence))

dict1.setdefault("banana", 5)
print(dict1)

dict1.setdefault("grapes", 5)
print(dict1)










