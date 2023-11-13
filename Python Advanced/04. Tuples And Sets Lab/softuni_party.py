n = int(input())

reservations = set()

for _ in range(n):
    reservation_num = input()
    reservations.add(reservation_num)

guests_reservation_num = input()

while guests_reservation_num != "END":
    if guests_reservation_num in reservations:
        reservations.remove(guests_reservation_num)
    guests_reservation_num = input()

print(len(reservations))

for num in sorted(reservations):
    print(num)