line = input()

price_of_product = {}
quantity_of_product = {}

while True:
    if line == "buy":
        break
    command = line.split()
    product, price, quantity = command[0], float(command[1]), int(command[2])
    if product not in price_of_product:
        price_of_product[product] = price
        quantity_of_product[product] = quantity
    else:
        price_of_product[product] = price
        quantity_of_product[product] += quantity

    line = input()

for product in price_of_product:
    price = price_of_product[product]
    quantity = quantity_of_product[product]
    total = price * quantity
    print(f"{product} -> {total:.2f}")

