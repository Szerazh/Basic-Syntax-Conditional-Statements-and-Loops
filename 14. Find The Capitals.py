word = input()
capital_letters = []
for index, letter in enumerate(word):
    if letter.isupper():
        capital_letters.append(index)

print(capital_letters)
