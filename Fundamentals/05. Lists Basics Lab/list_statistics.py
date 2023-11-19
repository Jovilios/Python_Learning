num = int(input())

positives_list = []
negatives_list = []
sum = 0

for _ in range(num):
    number = int(input())
    if number >= 0:
        positives_list.append(number)
    else:
        negatives_list.append(number)
        sum += number

print(positives_list)
print(negatives_list)
print(f"Count of positives: {len(positives_list)}")
print(f"Sum of negatives: {sum}")
