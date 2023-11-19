numbs = list(map(int, input().split(", ")))

# Правим го в рейндж дължината на списъка за да вземаме индекса не числото / в if проверката проверяваме числото от индекс

indexes = [x for x in range(len(numbs)) if numbs[x] % 2 == 0]

print(indexes)