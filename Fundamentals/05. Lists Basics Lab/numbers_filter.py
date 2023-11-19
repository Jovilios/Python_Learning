lines = int(input())

list_numbers = []

COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_NEGATIVE = "negative"
COMMAND_POSITIVE = "positive"

for _ in range(lines):
    nums = int(input())
    list_numbers.append(nums)

command = input()

filtered_numbers = []

for num in list_numbers:
    filtered_pass = (
        (command == COMMAND_EVEN and num % 2 == 0) or
        (command == COMMAND_ODD and num % 2 != 0) or
        (command == COMMAND_NEGATIVE and num < 0) or
        (command == COMMAND_POSITIVE and num >= 0)
    )
    if filtered_pass:
        filtered_numbers.append(num)

print(filtered_numbers)