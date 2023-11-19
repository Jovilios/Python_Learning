from math import ceil

items = input().split("|")
budget = int(input())

starting_budget = budget

final_price = 0
price_with_profit = []

for item in items:
    item_arg = item.split("->")
    type_item = item_arg[0]
    price_item = float(item_arg[1])

    if type_item == "Clothes" and price_item > 50:
        continue
    elif type_item == "Shoes" and price_item > 35:
        continue
    elif type_item == "Accessories" and price_item > 25.50:
        continue

    if budget < price_item:
        continue

    budget -= price_item
    price_with_profit.append(price_item)

for price in price_with_profit:
    price *= 1.4
    final_price += price
    print(f"{price:.2f}", end=" ")

profit = abs(starting_budget - (final_price + budget))

print()
print(f"Profit: {profit:.2f}")

if starting_budget + profit > 150:
    print("Hello, France!")
else:
    print("Not enough money.")
