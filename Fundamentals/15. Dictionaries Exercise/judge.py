contests = {}
users = {}

while True:

    line = input()
    if line == "no more time":
        break

    username, contest, points = line.split(" -> ")
    points = int(points)

    if contest not in contests:
        contests[contest] = {}

    if username not in contests[contest]:
        contests[contest][username] = points
        if username not in users:
            users[username] = 0
        users[username] += points

    elif contests[contest][username] < points:
        users[username] += points - contests[contest][username]
        contests[contest][username] = points

for contest, participants in contests.items():
    print(f"{contest}: {len(participants)} participants")
    for i, (username, points) in enumerate(sorted(participants.items(), key=lambda x: (-x[1], x[0]))):
        print(f"{i + 1}. {username} <::> {points}")

print("Individual standings:")
for i, (username, points) in enumerate(sorted(users.items(), key=lambda x: (-x[1], x[0]))):
    print(f"{i + 1}. {username} -> {points}")