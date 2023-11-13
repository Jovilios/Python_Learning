rows, cols = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

result = []

for col in range(cols):
    col_sum = 0

    for row in range(rows):
        col_sum += matrix[row][col]
    result.append(col_sum)

print(*result, sep="\n")