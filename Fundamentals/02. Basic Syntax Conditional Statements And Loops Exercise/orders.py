orders = int(input())

total_price = 0
for _ in range(orders):
    capsule_price = float(input())
    days = int(input())
    need_capsules = int(input())
    if capsule_price < 0.01 or capsule_price > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif need_capsules < 1 or need_capsules > 2000:
        continue
    price = capsule_price * days * need_capsules
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")
