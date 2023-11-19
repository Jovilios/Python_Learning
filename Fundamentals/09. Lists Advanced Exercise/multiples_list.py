factor = int(input())
count = int(input())

arranged = []

for num in range(1, count + 1):
    arranged.append(num * factor)

print(arranged)
