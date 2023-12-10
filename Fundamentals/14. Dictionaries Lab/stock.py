line = input().split()

bakery = {}

for i in range(0, len(line), 2):
    key = line[i]
    value = int(line[i + 1])
    bakery[key] = value

searched_products = input().split()

for el in searched_products:
    if el in bakery:
        print(f"We have {bakery[el]} of {el} left")
    else:
        print(f"Sorry, we don't have {el}")


