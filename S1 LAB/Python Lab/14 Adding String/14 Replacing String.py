string = input("Enter a string: ")
if string.endswith('ing'):
    string += 'ly'
else:
    if len(string) >= 3:
        string += 'ing'
print(string)
