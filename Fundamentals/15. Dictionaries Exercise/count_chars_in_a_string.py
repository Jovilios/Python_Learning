elements = [x for x in input() if x != " "]

dictionary = {}

for el in elements:
    if el not in dictionary:
        dictionary[el] = 0
    dictionary[el] += 1

for key, value in dictionary.items():
    print(f"{key} -> {dictionary[key]}")

