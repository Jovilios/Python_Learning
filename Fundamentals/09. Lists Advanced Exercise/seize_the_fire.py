fires = input().split("#")
water = int(input())

total_fire = 0

valid_cells = []

for cell in fires:
    cells_args = cell.split(" = ")
    level = cells_args[0]
    value = int(cells_args[1])

    if water < value:
        continue
    if level == "High" and (value < 81 or value > 125):
        continue
    elif level == "Medium" and (value < 51 or value > 80):
        continue
    elif level == "Low" and (value < 1 or value > 50):
        continue
    else:
        total_fire += value
        water -= value
        valid_cells.append(value)

print("Cells:")
for cell in valid_cells:
    print(f" - {cell}")

effort = total_fire * 0.25
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
