rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]

commands = input()

while True:
    command, *parameters = commands.split()
    if command == "END":
        break

    elif command == "swap" and len(parameters) == 4:
        row1, col1, row2, col2, = int(parameters[0]), int(parameters[1]), int(parameters[2]), int(parameters[3])
        valid_rows = range(rows)
        valid_cols = range(cols)

        if {row1, row2}.issubset(valid_rows) and {col1, col2}.issubset(valid_cols):
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            [print(*row) for row in matrix]

        else:
            print("Invalid input!")

    else:
        print("Invalid input!")

    commands = input()
