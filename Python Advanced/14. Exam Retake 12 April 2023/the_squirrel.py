from collections import deque

size = int(input())
move_direction = deque(input().split(", "))

matrix = [list(input()) for _ in range(size)]
hazelnuts = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

start = ()

for rows in range(size):
    for cols in range(size):
        if matrix[rows][cols] == "s":
            start = rows, cols

while True:

    if not move_direction:
        print("There are more hazelnuts to collect.")
        break

    direction = move_direction.popleft()
    new_row, new_col = directions[direction][0] + start[0], directions[direction][1] + start[1]

    if not 0 <= new_row < size or not 0 <= new_col < size:
        print("The squirrel is out of the field.")
        break

    if matrix[new_row][new_col] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break

    if matrix[new_row][new_col] == "h":
        hazelnuts += 1

    matrix[new_row][new_col] = "s"
    matrix[start[0]][start[1]] = "*"
    start = new_row, new_col

    if hazelnuts == 3:
        print("Good job! You have collected all hazelnuts!")
        break



print(f"Hazelnuts collected: {hazelnuts}")



# [print(*row) for row in matrix]