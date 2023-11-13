n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]
primary = [matrix[r][r] for r in range(n)]
secondary = [matrix[r][n - r - 1] for r in range(n)]

print(abs(sum(primary) - sum(secondary)))
