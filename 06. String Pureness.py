number_of_string = int(input())

for number in range(number_of_string):
    string = input()
    if "," in string or "." in string or "_" in string:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")
