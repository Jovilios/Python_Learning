rows, cols = [int(x) for x in input().split()]

matrix = [list(input().split()) for _ in range(rows)]

identical = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        if matrix[row][col] == matrix[row + 1][col] and matrix[row][col] == matrix[row][col + 1] and matrix[row][col] == matrix[row + 1][col + 1]:
            identical += 1

print(identical)
