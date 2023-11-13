from collections import deque

time_for_tasks = deque(int(x) for x in input().split())
number_of_tasks = deque(int(x) for x in input().split())

ducks = {"Darth Vader Ducky": 0, "Thor Ducky": 0, "Big Blue Rubber Ducky": 0, "Small Yellow Rubber Ducky": 0}


while time_for_tasks and number_of_tasks:
    time = time_for_tasks.popleft()
    task = number_of_tasks.pop()

    current_time = time * task

    if 0 < current_time <= 60:
        ducks["Darth Vader Ducky"] += 1

    elif 61 <= current_time <= 120:
        ducks["Thor Ducky"] += 1

    elif 121 <= current_time <= 180:
        ducks["Big Blue Rubber Ducky"] += 1

    elif 181 <= current_time <= 240:
        ducks["Small Yellow Rubber Ducky"] += 1

    else:
        time_for_tasks.append(time)
        number_of_tasks.append(task - 2)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for duck, count in ducks.items():
    print(f"{duck}: {count}")


