def shopping_list(budget, **kwargs):
    products = {}

    if budget < 100:
        return "You do not have enough budget."

    for key, value in kwargs.items():

        if len(products.keys()) >= 5:
            break

        if value[0] * value[1] > budget:
            continue

        if key not in products:
            products[key] = ()


        products[key] = value[0] * value[1]
        budget -= value[0] * value[1]

    result = ""

    for prod, price in products.items():
        result += f"You bought {prod} for {price:.2f} leva.\n"

    return result




print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

