budget = float(input())
price_flour_kg = float(input())
price_pack_eggs = 0
price_pack_eggs += 0.75 * price_flour_kg
liter_milk = 0
liter_milk += 1.25 * price_flour_kg
num_colored_eggs = 0
one_loaf_of_bread_price = price_flour_kg + price_pack_eggs + (liter_milk / 4)
num_bread = budget // one_loaf_of_bread_price
whole_num_bread = int(num_bread)
left_over = 0
leftover = budget % one_loaf_of_bread_price

for i in range(1, whole_num_bread + 1):
    num_colored_eggs += 3
    if i % 3 == 0:
        num_colored_eggs -= i - 2

print(f"You made {int(num_bread)} loaves of Easter bread! Now you have {num_colored_eggs} eggs and {leftover:.2f}BGN left.")
