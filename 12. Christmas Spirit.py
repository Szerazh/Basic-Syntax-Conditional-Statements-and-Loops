quantity_decorations = int(input())
rem_days_to_christmas = int(input())
total_cost = 0
total_spirit = 0
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

#every 2 day - ornaments set
#every 3 day - tree skirt, tree garland
#every 5 day - tree lights
for current_day in range(1, rem_days_to_christmas + 1):
    if current_day % 11 == 0:
        quantity_decorations += 2
    if current_day % 2 == 0:
        total_cost += quantity_decorations * ornament_set_price
        total_spirit += 5
    if current_day % 3 == 0:
        total_cost += quantity_decorations * (tree_skirt_price + tree_garland_price)
        total_spirit += 10 + 3
    if current_day % 5 == 0:
        total_cost += quantity_decorations * tree_lights_price
        total_spirit += 17
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt_price + tree_garland_price + tree_lights_price
if rem_days_to_christmas % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
