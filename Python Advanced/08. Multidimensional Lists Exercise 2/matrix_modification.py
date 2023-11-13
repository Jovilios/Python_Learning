size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]

commands = input().split()

while commands[0] != "END":

    command, new_row, new_col, value = commands[0], int(commands[1]), int(commands[2]), int(commands[3])

    if command == "Add" and 0 <= new_row < size and 0 <= new_col < size:
        matrix[new_row][new_col] += value

    elif command == "Subtract" and 0 <= new_row < size and 0 <= new_col < size:
        matrix[new_row][new_col] -= value

    else:
        print("Invalid coordinates")

    commands = input().split()

[print(*row) for row in matrix]