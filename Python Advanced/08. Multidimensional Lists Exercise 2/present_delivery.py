number_of_presents = int(input())

size = int(input())

matrix = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

nice_kids = 0
kids_with_gift = 0

start = ()

for rows in range(size):
    matrix.append(input().split())
    for cols in range(size):
        if matrix[rows][cols] == "S":
            start = rows, cols
        elif matrix[rows][cols] == "V":
            nice_kids += 1

commands = input().split()

while True:

    if commands[0] == "Christmas" and commands[1] == "morning" or number_of_presents == 0:
        break

    direction = commands[0]

    new_row, new_col = directions[direction][0] + start[0], directions[direction][1] + start[1]

    if matrix[new_row][new_col] == "V":
        number_of_presents -= 1
        kids_with_gift += 1

    elif matrix[new_row][new_col] == "C":
        for dir, pos in directions.items():

            row, col = new_row + pos[0], new_col + pos[1]

            if matrix[row][col] != "-":

                if matrix[row][col] == "V":
                    kids_with_gift += 1

                number_of_presents -= 1
                matrix[row][col] = "-"

    matrix[new_row][new_col] = "S"
    matrix[start[0]][start[1]] = "-"
    start = new_row, new_col

    if nice_kids == kids_with_gift:
        break

    if number_of_presents <= 0 < nice_kids - kids_with_gift:
        print("Santa ran out of presents!")
        break

    commands = input().split()

[print(*row) for row in matrix]
if nice_kids == kids_with_gift:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - kids_with_gift} nice kid/s.")
