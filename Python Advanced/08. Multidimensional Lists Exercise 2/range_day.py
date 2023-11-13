SIZE = 5

matrix = [[x for x in input().split()] for _ in range(SIZE)]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

start = ()
all_targets = 0
shooted_targets = 0

for rows in range(SIZE):
    for cols in range(SIZE):
        if matrix[rows][cols] == "A":
            start = (rows, cols)
        elif matrix[rows][cols] == "x":
            all_targets += 1


shoote = []

for _ in range(int(input())):
    command = input().split()

    if command[0] == "move":
        steps = int(command[2])
        direction = command[1]

        new_row, new_col = start

        for _ in range(steps):
            new_row += directions[direction][0]
            new_col += directions[direction][1]

        if 0 <= new_row < SIZE and 0 <= new_col < SIZE and matrix[new_row][new_col] == ".":
            start = new_row, new_col

    elif command[0] == "shoot":
        direction = command[1]

        new_row, new_col = directions[direction][0] + start[0], directions[direction][1] + start[1]

        while 0 <= new_row < SIZE and 0 <= new_col < SIZE:

            if matrix[new_row][new_col] == "x":
                matrix[new_row][new_col] = "."
                shoote.append([new_row, new_col])
                shooted_targets += 1
                break

            new_row += directions[direction][0]
            new_col += directions[direction][1]

        if shooted_targets == all_targets:
            print(f"Training completed! All {all_targets} targets hit.")
            break


if shooted_targets < all_targets:
    print(f"Training not completed! {all_targets - shooted_targets} targets left.")

print(*[x for x in shoote], sep="\n")