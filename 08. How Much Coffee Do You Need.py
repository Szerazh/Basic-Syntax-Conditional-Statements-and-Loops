number_of_coffees = 0
list_of_events = ["coding", "dog", "cat", "movie"]

while True:
    event = input()
    if event == "END":
        break
    elif event.lower() in list_of_events:
        if event.isupper():
            number_of_coffees += 2
        else:
            number_of_coffees += 1
if number_of_coffees > 5:
    print("You need extra sleep")
else:
    print(number_of_coffees)
