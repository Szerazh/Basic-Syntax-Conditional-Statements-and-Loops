queue = input()

sheep_in_danger = 0
list_animals = queue.split()
if list_animals[(len(list_animals) - 1)] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    list_animals.reverse()
    for list_index in range(len(list_animals)):
        if list_animals[list_index] == "wolf,":
            sheep_in_danger = list_index
            print(f"Oi! Sheep number {sheep_in_danger}! You are about to be eaten by a wolf!")
