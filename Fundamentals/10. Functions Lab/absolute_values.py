sequence_of_numbers = input().split()

number = []

for num in sequence_of_numbers:
    number.append(abs(float(num)))

print(number)


# print([abs(float(num)) for num in input().split()])
