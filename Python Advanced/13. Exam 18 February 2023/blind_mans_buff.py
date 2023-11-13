rows, cols = [int(x) for x in input().split()]

matrix = []

moves = 0
touched_opponents = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

start = ()

for row in range(rows):
    matrix.append(input().split())
    for col in range(cols):
        if matrix[row][col] == "B":
            start = row, col



while True:
    command = input()

    if command == "Finish":
        break

    new_row, new_col = directions[command][0] + start[0], directions[command][1] + start[1]

    if not 0 <= new_row < rows or not 0 <= new_col < cols or matrix[new_row][new_col] == "O":
        continue

    if matrix[new_row][new_col] == "P":
        touched_opponents += 1


    moves += 1
    matrix[new_row][new_col] = "B"
    matrix[start[0]][start[1]] = "-"
    start = new_row, new_col

    if touched_opponents == 3:
        break


print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves}")


