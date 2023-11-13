rows, cols = [int(x) for x in input().split(", ")]

matrix = []
max_sum = 0

for row in range(rows):
    lines = [int(x) for x in input().split(", ")]
    max_sum += sum(lines)
    matrix.append(lines)


print(max_sum)
print(matrix)