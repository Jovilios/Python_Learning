size = int(input())

matrix = []

for _ in range(size):
    inter_list = list(input())
    matrix.append(inter_list)

searched_symbol = input()

position = None

for row in range(size):
    if position:
        break
    for col in range(size):
        if matrix[row][col] == searched_symbol:
            position = (row, col)
            break
if position:
    print(position)
else:
    print(f"{searched_symbol} does not occur in the matrix")
