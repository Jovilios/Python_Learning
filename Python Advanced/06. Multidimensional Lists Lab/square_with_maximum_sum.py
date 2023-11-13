rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    inner_list = [int(x) for x in input().split(", ")]
    matrix.append(inner_list)

max_sum = float("-inf")
sub_matrix = []

for row in range(rows - 1):
    for col in range(cols - 1):
        cur_el = matrix[row][col]
        below_el = matrix[row+1][col]
        next_el = matrix[row][col + 1]
        diag_el = matrix[row + 1][col + 1]
        sum_el = cur_el + below_el + next_el + diag_el

        if max_sum < sum_el:
            max_sum = sum_el
            sub_matrix = [[cur_el, next_el], [below_el, diag_el]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)

