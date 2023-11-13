rows, cols = [int(x) for x in input().split()]

matrix = []


for row in range(97, 97 + rows):
    for col in range(row, row + cols):
        print(f"{chr(row)}{chr(col)}{chr(row)}", end=" ")

    print()