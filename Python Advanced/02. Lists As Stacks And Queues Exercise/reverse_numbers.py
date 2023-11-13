from collections import deque

nums = deque((input().split()))

while nums:
    print(nums.pop(), end=" ")

