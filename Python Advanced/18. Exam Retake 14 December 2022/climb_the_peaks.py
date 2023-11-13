from collections import deque

days = 1

daily_portions = deque(input().split(", "))
daily_stamina = deque(input().split(", "))
mountain_peaks = []

all_peaks = deque([
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70)
])

while True:

    if len(mountain_peaks) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break

    if days > 7:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        break

    portions = daily_portions.pop()
    stamina = daily_stamina.popleft()
    current_supply = int(portions) + int(stamina)
    next_mount = all_peaks[0]

    if current_supply >= next_mount[1]:
        mountain_peaks.append(next_mount[0])
        all_peaks.popleft()

    days += 1


if mountain_peaks:
    print("Conquered peaks:")
    for m in mountain_peaks:
        print(m)

