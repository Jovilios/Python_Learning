names = input().split(", ")

# (-len(x), x) означава първо сортирай по дължината на думата във низходящ ред, ако има 2 еднакви дължини
# сортирай по азбучен ред

name_list = sorted(names, key=lambda x: (-len(x), x))

print(name_list)