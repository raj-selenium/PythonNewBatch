import csv

with open("employee.csv") as f:
    data = csv.reader(f)
    header = next(data)

    for line in data:
        print(line)

