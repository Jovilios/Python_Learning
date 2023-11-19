wagons_in_train = int(input())
wagons = [0] * wagons_in_train

while True:
    commands = input()
    if commands == "End":
        break
    current_command = commands.split()
    if current_command[0] == "add":
        people = int(current_command[1])
        wagons[-1] += people
    elif current_command[0] == "insert":
        idx = int(current_command[1])
        people = int(current_command[2])
        wagons[idx] += people
    elif current_command[0] == "leave":
        idx = int(current_command[1])
        people = int(current_command[2])
        wagons[idx] -= people
print(wagons)


