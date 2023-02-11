word = input('enter a word')
print('ordinal values of the word : ',word)
for character in word:
    print(character, "=>",ord(character))
