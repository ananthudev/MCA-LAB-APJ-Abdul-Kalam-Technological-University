startYear = 2020
print ("Enter last year")
endYear = int(input())
print ("List of leap years:")
for year in range(startYear, endYear):
    if (0 == year % 4) and (0 != year % 100) or (0 == year % 400):
        print (year)
