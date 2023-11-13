def shopping_cart(*args):

    prod_max_len = {"Soup": 3, "Pizza": 4, "Dessert": 2}

    meals = {"Soup": [], "Pizza": [], "Dessert": []}

    for el in args:
        if el == "Stop":
            break
        if el[0] not in meals:
            meals[el[0]] = []

        if len(meals[el[0]]) < prod_max_len[el[0]] and el[1] not in meals[el[0]]:
            meals[el[0]].append(el[1])

    for value in meals.values():
        if len(value) > 0:
            break
    else:
        return 'No products in the cart!'

    result = ""

    sorted_meals = sorted(meals.items(), key=lambda x: (-len(x[1]), x[0]))

    for meal, products in sorted_meals:
        sorted_products = sorted(products)
        result += f"{meal}:\n"
        for product in sorted_products:
            result += f" - {product}\n"

    return result




print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))

