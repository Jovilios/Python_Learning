SIZE = 6

matrix = [[x for x in input().split()] for _ in range(SIZE)]

start_position = input()
start = [int(start_position[1]), int(start_position[-2])]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

commands = input()

while commands != "Stop":

    command, *args = commands.split(", ")

    new_row, new_col = directions[args[0]][0] + start[0], directions[args[0]][1] + start[1]

    if command == "Create" and matrix[new_row][new_col] == ".":
        matrix[new_row][new_col] = args[1]

    elif command == "Update" and matrix[new_row][new_col] != ".":
        matrix[new_row][new_col] = args[1]

    elif command == "Delete" and matrix[new_row][new_col] != ".":
        matrix[new_row][new_col] = "."

    elif command == "Read" and matrix[new_row][new_col] != ".":
        print(matrix[new_row][new_col])

    start = [new_row, new_col]
    commands = input()

[print(*row) for row in matrix]

