SIZE = int(input())

matrix = []

mine_hit = 0
enemy_hit = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

start = []

for row in range(SIZE):
    matrix.append(list(input()))
    for col in range(SIZE):
        if matrix[row][col] == "S":
            start = [row, col]
            matrix[row][col] = "-"

command = input()

while True:

    new_row, new_col = directions[command][0] + start[0], directions[command][1] + start[1]

    if matrix[new_row][new_col] == "*":
        mine_hit += 1
        if mine_hit == 3:
            matrix[new_row][new_col] = "S"
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{new_row}, {new_col}]!")
            break

    if matrix[new_row][new_col] == "C":
        enemy_hit += 1
        if enemy_hit == 3:
            matrix[new_row][new_col] = "S"
            print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

    matrix[new_row][new_col] = "-"
    start = [new_row, new_col]

    command = input()

# [print(*row) for row in matrix]
for row in matrix:
    print(''.join(row))