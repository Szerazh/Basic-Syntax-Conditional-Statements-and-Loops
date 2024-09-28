word = input()
total = 0
word_1 = "Sand"
word_2 = "Water"
word_3 = "Fish"
word_4 = "Sun"
word_lower = word.lower()

if word_1.lower() in word_lower:
    total += word_lower.count(word_1.lower())
if word_2.lower() in word_lower:
    total += word_lower.count(word_2.lower())
if word_3.lower() in word_lower:
    total += word_lower.count(word_3.lower())
if word_4.lower() in word_lower:
    total += word_lower.count(word_4.lower())

print(total)
