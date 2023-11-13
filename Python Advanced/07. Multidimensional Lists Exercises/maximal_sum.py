rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = float("-inf")
maximal_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        row_one = matrix[row][col:col + 3] # Slice the col from starting index to starting index + 3 exclusive
        row_two = matrix[row + 1][col:col + 3]
        row_three = matrix[row + 2][col:col + 3]

        current_sum = sum(row_one) + sum(row_two) + sum(row_three)

        if current_sum > max_sum:
            max_sum = current_sum
            maximal_matrix = [row_one, row_two, row_three]

print(f"Sum = {max_sum}")
[print(*row) for row in maximal_matrix]



