from collections import deque

chocolates = deque(int(x) for x in input().split(", "))  # 20, 24, -5, 17, 22, 60, this - 26
cups_of_milk = deque(int(x) for x in input().split(", ")) # this - 26, 60, 22, 17, 24, 10, 55

milkshakes = 0

while milkshakes != 5 and chocolates and cups_of_milk:
    chocolate = chocolates.pop()
    milk = cups_of_milk.popleft()

    if chocolate == milk:
        milkshakes += 1

    elif chocolate <= 0:
        cups_of_milk.appendleft(milk)
        continue

    elif milk <= 0:
        chocolates.append(chocolate)
        continue

    else:
        cups_of_milk.append(milk)
        chocolates.append(chocolate - 5)


if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups_of_milk) or 'empty'}")