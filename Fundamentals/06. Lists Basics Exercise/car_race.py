times = input().split()

middle_of_road = len(times) // 2
left_car_road = times[0:middle_of_road]
# After this line the list (times) will reverse from 1,2,3 to 3,2,1
times.reverse()
right_car_road = times[0:middle_of_road]

time_left = 0
time_right = 0

for times in left_car_road:
    time = float(times)
    if time == 0:
        time_left *= 0.8
    else:
        time_left += time

for times in right_car_road:
    time = float(times)
    if time == 0:
        time_right *= 0.8
    else:
        time_right += time

if time_left > time_right:
    print(f"The winner is right with total time: {time_right:.1f}")
else:
    print(f"The winner is left with total time: {time_left:.1f}")

