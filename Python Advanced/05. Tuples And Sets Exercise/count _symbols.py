word = tuple(x for x in input())

occurances = {}

for el in word:
    if el not in occurances:
        occurances[el] = 0
    occurances[el] += 1


for key, value in sorted(occurances.items()):
    print(f"{key}: {value} time/s")
