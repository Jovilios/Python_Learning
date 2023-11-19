working_day = input().split("|")

energy = 100
coins = 100

for days in working_day:
    days_arg = days.split("-")
    event = days_arg[0]
    numb = int(days_arg[1])

    if event == "rest":
        if numb + energy > 100:
            print(f"You gained {(100 - energy)} energy.")
            energy = 100
            print(f"Current energy: {energy}.")
        else:
            energy += numb
            print(f"You gained {numb} energy.")
            print(f"Current energy: {energy}.")
    elif event == "order":
        if energy - 30 >= 0:
            energy -= 30
            coins += numb
            print(f"You earned {numb} coins.")
        else:
            energy += 50
            print("You had to rest!")
            continue
    else:
        if coins >= numb:
            coins -= numb
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            quit()
print("Day completed!")
print(f"Coins: {coins}")
print(f"Energy: {energy}")
