number = int(input())
new_highest_number = sorted(str(number), reverse=True)
max_number = int(''.join(new_highest_number))

print(max_number)
