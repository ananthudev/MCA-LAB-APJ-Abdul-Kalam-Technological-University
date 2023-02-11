input_string = input('enter a string')
input_string = input_string.casefold()
vowels = "aeiou"
data = {}.fromkeys(vowels, 0)
for charecter in input_string:
    if charecter in vowels:
        data[charecter] += 1
for vowel in data:
    print(vowel, "=>", data[vowel])
