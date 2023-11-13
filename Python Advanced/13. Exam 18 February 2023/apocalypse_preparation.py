from collections import deque


textiles = deque(int(x) for x in input().split())
medicaments = deque(int(x) for x in input().split())

healing_items = {"Patch": 0, "Bandage": 0, "MedKit": 0}


while True:

    if not textiles and not medicaments:
        print("Textiles and medicaments are both empty.")
        break

    if not textiles:
        print("Textiles are empty.")
        break

    if not medicaments:
        print("Medicaments are empty.")
        break

    textile = textiles.popleft()
    medicament = medicaments.pop()

    current_healing_item = textile + medicament

    if current_healing_item == 30:
        healing_items["Patch"] += 1

    elif current_healing_item == 40:
        healing_items["Bandage"] += 1

    elif current_healing_item == 100:
        healing_items["MedKit"] += 1

    elif current_healing_item > 100:
        healing_items["MedKit"] += 1
        medicaments[-1] += current_healing_item - 100

    else:
        medicaments.append(medicament + 10)

sorted_healing_items = sorted(healing_items.items(), key=lambda x: (-x[1], x[0]))

for heal, count in sorted_healing_items:
    if count != 0:
        print(f"{heal} - {count}")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(str(x) for x in medicaments)}")
if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")