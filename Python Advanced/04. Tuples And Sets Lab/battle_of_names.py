n = int(input())

odd_set = set()
even_set = set()

for i in range(1, n + 1):
    name_sum = sum(ord(el) for el in input()) // i

    if name_sum % 2 == 0:
        even_set.add(name_sum)
    else:
        odd_set.add(name_sum)

if sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")
