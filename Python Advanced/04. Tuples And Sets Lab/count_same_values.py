numbers = tuple(float(x) for x in input().split())

occurances = {}

for num in numbers:
    if num not in occurances:
        occurances[num] = 0
    occurances[num] += 1

for key, value in occurances.items():
    print(f"{key} - {value} times")
