from collections import deque

green_light = int(input())
free_duration = int(input())

total_cars_passed = 0

cars_waiting = deque()

command = input()

while command != "END":
    if command == "green":
        time_left = green_light

        while time_left > 0 and cars_waiting:
            car = cars_waiting.popleft()
            time = time_left + free_duration
            if len(car) > time:
                print("A crash happened!")
                print(f"{car} was hit at {car[time]}.")
                raise SystemExit

            time_left -= len(car)
            total_cars_passed += 1
    else:
        cars_waiting.append(command)
    command = input()

print("Everyone is safe.")
print(f"{total_cars_passed} total cars passed the crossroads.")