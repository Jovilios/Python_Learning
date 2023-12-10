count = int(input())

parking = {}

for _ in range(count):
    commands = input().split()
    command, name = commands[0], commands[1]
    if command == "register":
        plate_number = commands[2]
        if name in parking:
            print(f"ERROR: already registered with plate number {parking[name]}")
            continue
        else:
            parking[name] = plate_number
            print(f"{name} registered {plate_number} successfully")
    if command == "unregister":
        if name not in parking:
            print(f"ERROR: user {name} not found")
        else:
            parking.pop(name)
            print(f"{name} unregistered successfully")

for key, value in parking.items():
    print(f"{key} => {value}")
