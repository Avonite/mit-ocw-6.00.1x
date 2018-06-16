gtstr = str(input("Please type your string: "))

numVowels = 0

for letter in gtstr:
    if letter == "a" or letter == "o" or letter == "i" or letter == "e" or letter == "u":
        numVowels += 1
print(numVowels)