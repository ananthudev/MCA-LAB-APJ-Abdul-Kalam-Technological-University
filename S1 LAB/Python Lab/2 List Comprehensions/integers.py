numList = [34, 1, 0, -23, 82, -5]
print('original numbers in the list',numList)
positiveNum = list(filter(lambda X: X > 0, numList))
print('positive numbers in the given list',positiveNum)
