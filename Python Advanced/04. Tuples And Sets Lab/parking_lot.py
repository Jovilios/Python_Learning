n = int(input())
parking = set()

for _ in range(n):
    command, plate = input().split(", ")
    if command == "IN":
        parking.add(plate)
    elif command == "OUT":
        parking.remove(plate)

if parking:
    print(*parking, sep="\n")
else:
    print("Parking Lot is Empty")