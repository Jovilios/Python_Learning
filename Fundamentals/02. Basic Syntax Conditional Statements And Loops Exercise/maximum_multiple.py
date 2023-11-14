divisor = int(input())
max_number = int(input())

number = 0
for n in range(max_number + 1):
    if n % divisor == 0:
        number = n
print(number)
