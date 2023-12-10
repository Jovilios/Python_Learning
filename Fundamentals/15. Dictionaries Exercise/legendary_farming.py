legendary_materials = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}

legendary_wep = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}

junk_items = {}

crafted = False
while not crafted:
    line = input()
    materials = line.split()
    for idx in range(0, len(materials) - 1, 2):
        quantity = int(materials[idx])
        material = materials[idx + 1].lower()

        if material in legendary_materials:
            legendary_materials[material] += quantity
            if legendary_materials[material] >= 250:
                legendary_materials[material] -= 250
                crafted = True
                print(f"{legendary_wep[material]} obtained!")
                break
        else:
            if material in junk_items:
                junk_items[material] += quantity
            else:
                junk_items[material] = quantity


for key, value in legendary_materials.items():
    print(f"{key}: {legendary_materials[key]}")

for key, value in junk_items.items():
    print(f"{key}: {junk_items[key]}")
