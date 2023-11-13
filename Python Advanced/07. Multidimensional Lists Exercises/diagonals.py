size = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(size)]
rotated_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0])-1,-1,-1)]

max_sum_primary = 0
max_sum_secondary = 0

primary_diagonal = []
secondary_diagonal = []

for idx in range(size):
    max_sum_primary += matrix[idx][idx]
    max_sum_secondary += rotated_matrix[idx][idx]
    primary_diagonal.append(matrix[idx][idx])
    secondary_diagonal.append(rotated_matrix[idx][idx])


print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {max_sum_primary}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {max_sum_secondary}")


# n = int(input())
#
# matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]
# primary = [matrix[r][r] for r in range(n)]
# secondary = [matrix[r][n - r - 1] for r in range(n)]
#
# print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
# print(f"Secondary diagonal: {', '.join(str(x) for x in secondary)}. Sum: {sum(secondary)}")