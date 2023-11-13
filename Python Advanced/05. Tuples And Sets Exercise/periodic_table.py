n = int(input())

chemicals = set()

for _ in range(n):
    for chem in input().split():
        chemicals.add(chem)

print(*chemicals, sep="\n")


# n = int(input())
#
# periodic_table = {x for _ in range(n) for x in input().split()}
#
# print(periodic_table)