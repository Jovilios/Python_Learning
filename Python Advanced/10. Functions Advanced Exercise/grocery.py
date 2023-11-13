def grocery_store(**prod):
    prod = sorted(prod.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    result = []

    for product, quantity in prod:
        result.append(f"{product}: {quantity}")

    return '\n'.join(result)




print(grocery_store(bread=5, pasta=12, eggs=12,))

