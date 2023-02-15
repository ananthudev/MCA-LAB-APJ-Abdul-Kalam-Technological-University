import csv

with open('csvfile.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(list(row))
