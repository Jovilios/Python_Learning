first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())


for _ in range(int(input())):
    commands, position, *data = input().split()

    command = commands + " " + position

    if command == "Add First":
        [first.add(int(x)) for x in data]
    elif command == "Add Second":
        [second.add(int(x)) for x in data]
    elif command == "Remove First":
        [first.discard(int(x)) for x in data]
    elif command == "Remove Second":
        [second.discard(int(x)) for x in data]
    elif command == "Check Subset":
        print(first.issubset(second) or second.issubset(first))

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")
