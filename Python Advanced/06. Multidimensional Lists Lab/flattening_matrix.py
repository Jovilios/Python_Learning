rows = int(input())

matrix = []

for i in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix.extend(row)
    # matrix.append(row)

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=" ")

print(matrix, sep=", ")