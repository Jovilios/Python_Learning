SIZE = int(input())
racing_number = input()

matrix = [[x for x in input().split()] for _ in range(SIZE)]
km = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

start = [0, 0]

commands = input()

while True:
    if commands == "End":
        matrix[start[0]][start[1]] = "C"
        print(f"Racing car {racing_number} DNF.")
        break

    new_row, new_col = directions[commands][0] + start[0], directions[commands][1] + start[1]

    if matrix[new_row][new_col] == "T":
        matrix[new_row][new_col] = "."
        for row in range(SIZE):
            for col in range(SIZE):
                if matrix[row][col] == "T":
                    matrix[row][col] = "."
                    new_row, new_col = [row, col]
                    km += 20
                    break

    if matrix[new_row][new_col] == "F":
        km += 10
        matrix[new_row][new_col] = "C"
        print(f"Racing car {racing_number} finished the stage!")
        break

    km += 10
    start = [new_row, new_col]
    commands = input()

print(f"Distance covered {km} km.")
# [print(*row) for row in matrix]
for row in matrix:
    print(''.join(row))