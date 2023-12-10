elements = input().lower().split()

dictionary = {}

for el in elements:
    if el not in dictionary:
        dictionary[el] = 0
    dictionary[el] += 1

for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")