rows, cols = [int(x) for x in input().split(", ")]

matrix = []

decorations = 0
gifts = 0
cookies = 0
all_items = 0

directions = {
    "left": lambda r, c: [r, (c - 1) % cols],
    "right": lambda r, c: [r, (c + 1) % cols],
    "up": lambda r, c: [(r - 1) % rows, c],
    "down": lambda r, c: [(r + 1) % rows, c],
}

start = []

for row in range(rows):
    matrix.append(input().split())
    for col in range(cols):
        if matrix[row][col] == "Y":
            start = [row, col]
            matrix[row][col] = "x"
        elif matrix[row][col] != "." and matrix[row][col] != "Y":
            all_items += 1


commands = input()

while True:

    if commands == "End":
        matrix[start[0]][start[1]] = "Y"
        break

    command, steps = commands.split("-")
    steps = int(steps)

    for _ in range(steps):
        santa_position = directions[command](*start)
        position = matrix[santa_position[0]][santa_position[1]]

        if position == "D":
            decorations += 1
            all_items -= 1

        elif position == "G":
            gifts += 1
            all_items -= 1

        elif position == "C":
            cookies += 1
            all_items -= 1

        matrix[santa_position[0]][santa_position[1]] = "x"
        start = santa_position

        if all_items == 0:
            position = "Y"
            print("Merry Christmas!")
            break

    if all_items == 0:
        matrix[start[0]][start[1]] = "Y"
        break

    commands = input()

print("You've collected:")
print(f"- {decorations} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")
[print(*row) for row in matrix]


