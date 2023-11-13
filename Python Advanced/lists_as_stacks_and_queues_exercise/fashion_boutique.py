from collections import deque

clothes = deque([int(x) for x in input().split()])
capacity_for_one_rack = int(input())

racks = 1
current_capacity = capacity_for_one_rack

while clothes:
    cloth = clothes.pop()

    if current_capacity >= cloth:
        current_capacity -= cloth
    else:
        racks += 1
        current_capacity = capacity_for_one_rack - cloth

print(racks)