from collections import deque

pump_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

pump_data_copy = pump_data.copy()
tank = 0
index = 0

while pump_data_copy:
    petrol, distance = pump_data_copy.popleft()

    tank += petrol

    if tank >= distance:
        tank -= distance
    else:
        pump_data.rotate(-1)
        pump_data_copy = pump_data.copy()
        index += 1
        tank = 0

print(index)