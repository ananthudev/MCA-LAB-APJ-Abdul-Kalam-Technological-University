import csv

with open('csvfile.csv','r')as csvfile:
    data=csv.reader(csvfile)
    for line in data:
        print(line[2])
