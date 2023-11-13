from collections import deque


materials = deque(int(x) for x in input().split())
magic_level = deque(int(x) for x in input().split())

presents_crafted = {"Gemstone": 0, "Porcelain Sculpture": 0, "Gold": 0, "Diamond Jewellery": 0}


while materials and magic_level:
    material = materials.pop()
    cur_level = magic_level.popleft()

    present = material + cur_level

    if present < 100:
        if present % 2 == 0:
            material *= 2
            cur_level *= 3
        else:
            material *= 2
            cur_level *= 2

        present = material + cur_level

        if present < 100:
            continue

    if present > 499:
        material /= 2
        cur_level /= 2

        present = material + cur_level
        if present > 499:
            continue

    if 99 < present < 200:
        presents_crafted["Gemstone"] += 1

    elif 199 < present < 300:
        presents_crafted["Porcelain Sculpture"] += 1

    elif 299 < present < 400:
        presents_crafted["Gold"] += 1

    elif 399 < present < 500:
        presents_crafted["Diamond Jewellery"] += 1


if presents_crafted["Gemstone"] != 0 and presents_crafted["Porcelain Sculpture"] != 0 or presents_crafted["Gold"] != 0 and presents_crafted["Diamond Jewellery"] != 0:
    print("The wedding presents are made!")
else:
    print(f"Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

for key, value in sorted(presents_crafted.items()):
    if value != 0:
        print(f"{key}: {value}")