size = int(input())

matrix = [list(input()) for _ in range(size)]

directions = (
    (-2, -1),
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),

)

removed_knight = 0

while True:
    best_knight = 0
    knight_with_most_attacks_pos = []

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                attacks = 0

                for x, y in directions:
                    new_row, new_col = row + x, col + y

                    if 0 <= new_row < size and 0 <= new_col < size:
                        if matrix[new_row][new_col] == "K":
                            attacks += 1

                if best_knight < attacks:
                    best_knight = attacks
                    knight_with_most_attacks_pos = [row, col]

    if knight_with_most_attacks_pos:
        knight_row, knight_col = knight_with_most_attacks_pos
        matrix[knight_row][knight_col] = "0"
        removed_knight += 1
    else:
        break


print(removed_knight)