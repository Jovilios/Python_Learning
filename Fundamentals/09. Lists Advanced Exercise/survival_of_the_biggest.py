nums = input().split()

list_of_nums = []

for num in nums:
    list_of_nums.append(int(num))

nums_to_remove = int(input())

for _ in range(nums_to_remove):
    list_of_nums.remove(min(list_of_nums))

result = ", ".join(str(items) for items in list_of_nums)

print(result)

