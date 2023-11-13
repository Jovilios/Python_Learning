from collections import deque

elfs_energy = deque(int(x) for x in input().split())
materials_in_box = deque(int(x) for x in input().split())

total_toys = 0
energy_used = 0
day = 1

while elfs_energy and materials_in_box:
    energy = elfs_energy.popleft()
    material = materials_in_box.pop()

    if energy < 5:
        materials_in_box.append(material)
        continue

    if day % 3 == 0 or day % 5 == 0:

        if day % 15 == 0:
            if energy >= material * 2:
                energy_used += (material * 2)
                elfs_energy.append(energy - (material * 2))
            else:
                elfs_energy.append(energy * 2)
                materials_in_box.append(material)

        elif day % 5 == 0:
            if energy >= material:
                energy_used += material
                elfs_energy.append(energy - material)
            else:
                elfs_energy.append(energy * 2)
                materials_in_box.append(material)

        elif day % 3 == 0:
            if energy >= material * 2:
                energy_used += (material * 2)
                total_toys += 2
                elfs_energy.append((energy - (material * 2)) + 1)
            else:
                elfs_energy.append(energy * 2)
                materials_in_box.append(material)

    elif energy >= material:
        energy_used += material
        total_toys += 1
        elfs_energy.append((energy - material) + 1)

    else:
        elfs_energy.append(energy * 2)
        materials_in_box.append(material)
    day += 1

print(f"Toys: {total_toys}")
print(f"Energy: {energy_used}")

if elfs_energy:
    print(f"Elves left: {', '.join(str(elf) for elf in elfs_energy)}")
if materials_in_box:
    print(f"Boxes left: {', '.join(str(box) for box in materials_in_box)}")

