# Comprehension:
# getting meaning from written text

mylist = [3,8,10,12,17,30]

double_mylist =[]

for i in mylist:
    double_mylist.append(i*2)

double_only_odd_numbers = []

for i in mylist:
    if i%2 != 0 and i%3==0:
        double_only_odd_numbers.append(i*2)

print(double_mylist)
print(double_only_odd_numbers)

double_mylist2 = [i*2 for i in mylist]
double_only_odd_numbers2 = [i*2 for i in mylist if i%2!=0 and i%3==0]
print(double_mylist2)
print(double_only_odd_numbers2)

double_odd_numbers = []
for i in mylist:
    if i%2 != 0:
        double_odd_numbers.append(i*2)
    else:
        double_odd_numbers.append(i)

print(double_odd_numbers)


double_numbers_only_if_odd = [i*2 if i%2 !=0 else i for i in mylist]

print(double_numbers_only_if_odd)

print([i*2 if i%2 !=0 else i*3 if i%5==0 else i for i in mylist])

print({"Even" if i % 2 == 0 else "Odd" for i in range(5)})

names = ["kamal", "kandan", "krish", "anish", "deepan", "kabilan", "saravanan"]

names_dict = {}
for name in names:
    names_dict.update({name[0]: [n for n in names if n[0]==name[0]]})

print(names_dict)

print({name[0]:[n for n in names if n[0]==name[0]] for name in names})

dict1 = {name[0]:[n for n in names if n[0]==name[0]] for name in names}


print([n for n in dict1.values()])
print([x for n in dict1.values() for x in n])