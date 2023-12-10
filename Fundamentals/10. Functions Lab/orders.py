def order_price(product, quantity):
    if product == "coffee":
        return quantity * 1.5
    elif product == "coke":
        return quantity * 1.4
    elif product == "water":
        return quantity * 1
    elif product == "snacks":
        return quantity * 2


products = input()
products_quantity = int(input())

result = order_price(products, products_quantity)

print(f"{result:.2f}")
