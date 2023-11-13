size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]

max_sum = 0

for idx in range(size):
    max_sum += matrix[idx][idx]

print(max_sum)