gifts = input().split()

while True:
    commands = input()
    if commands == "No Money":
        break
    list_of_commands = commands.split()
    command = list_of_commands[0]
    gift = list_of_commands[1]

    if command == "OutOfStock":
        for idx in range(len(gifts)):
            if gifts[idx] == gift:
                gifts[idx] = "None"

    elif command == "Required":
        idx = int(list_of_commands[2])
        if 0 <= idx < len(gifts):
            gifts[idx] = gift

    elif command == "JustInCase":
        gifts[-1] = gift

for gift in gifts:
    if gift == "None":
        continue
    else:
        print(gift, end=" ")
