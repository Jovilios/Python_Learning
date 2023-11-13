from collections import deque

seats = deque(input().split(", "))
first_num = deque(input().split(", "))
second_num = deque(input().split(", "))

rotations = 0
found_seats = []


while True:

    if rotations == 10 or len(found_seats) == 3:
        break

    first = first_num.popleft()
    second = second_num.pop()
    leather = chr(int(first) + int(second))

    if f"{first}{leather}"in seats:
        found_seats.append(f"{first}{leather}")
        seats.remove(f"{first}{leather}")

    elif f"{second}{leather}" in seats:
        found_seats.append(f"{second}{leather}")
        seats.remove(f"{second}{leather}")

    else:
        first_num.append(first)
        second_num.appendleft(second)

    rotations += 1

print(f"Seat matches: {', '.join(found_seats)}")
print(f"Rotations count: {rotations}")

