decorations = int(input())
days_left = int(input())


total_cost = 0
points = 0


for i in range(1, days_left + 1):
    daily_buy_price = 0
    if i % 11 == 0:
        decorations += 2
    if i % 2 == 0:
        daily_buy_price += 2 * decorations
        points += 5
    if i % 3 == 0:
        daily_buy_price += 8 * decorations
        points += 13
    if i % 5 == 0:
        daily_buy_price += 15 * decorations
        points += 17
        if i % 3 == 0:
            points += 30
    if i % 10 == 0:
        points -= 20
        daily_buy_price += 23

    total_cost += daily_buy_price
if days_left % 10 == 0:
    points -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {points}")
