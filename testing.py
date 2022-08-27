import csv

with open('command.csv', 'r') as data:
    reader = csv.reader(data)
    for row in reader:
        print(row)