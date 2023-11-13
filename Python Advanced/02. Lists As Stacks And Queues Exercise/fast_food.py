from collections import deque

food = int(input())

orders = deque([int(x) for x in input().split()])

if orders:
    print(max(orders))

for i in range(len(orders)):
    if food < orders[0]:
        print(f"Orders left: {' '.join(str(x) for x in orders)}")
        break
    food -= orders.popleft()

else:
    print("Orders complete")

