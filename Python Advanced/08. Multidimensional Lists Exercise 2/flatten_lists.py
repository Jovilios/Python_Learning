word = input().split("|")

new_list = []

for el in word[::-1]:
    new_list.extend(el.split())

print(*new_list)