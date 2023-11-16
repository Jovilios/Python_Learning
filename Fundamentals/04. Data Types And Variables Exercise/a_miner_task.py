dictionary = {}

while True:
    goods = input()
    if goods == "stop":
        break
    quantity = int(input())
    if goods not in dictionary:
        dictionary[goods] = 0
    dictionary[goods] += quantity

for key, value in dictionary.items():
    print(f"{key} -> {dictionary[key]}")
