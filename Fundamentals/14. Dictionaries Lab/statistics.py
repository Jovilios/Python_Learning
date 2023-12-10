products = {}

line = input()

while True:
    if line == "statistics":
        break
    command = line.split(": ")
    key = command[0]
    value = int(command[1])
    if key not in products:
        products[key] = 0
    products[key] += value
    line = input()
print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")
