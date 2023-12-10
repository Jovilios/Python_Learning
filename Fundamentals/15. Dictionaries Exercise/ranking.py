contest_and_pass = {}
contest_by_user = {}

while True:
    line = input()
    if line == "end of contests":
        break
    contest, password = line.split(":")
    contest_and_pass[contest] = password

while True:
    line = input()
    if line == "end of submissions":
        break
    contest, password, username, points = line.split("=>")
    points = int(points)

    if contest in contest_and_pass and password == contest_and_pass[contest]:
        if username not in contest_by_user:
            contest_by_user[username] = {}
        if contest in contest_by_user[username] and points < contest_by_user[username][contest]:
            continue
        contest_by_user[username][contest] = points


# Calculate total points and find best candidate
best_candidate = None
best_points = 0
for username, user_data in contest_by_user.items():
    total_points = sum(user_data.values())
    if total_points > best_points:
        best_candidate = username
        best_points = total_points

# Print best candidate
print(f"Best candidate is {best_candidate} with total {best_points} points.")
print("Ranking:")

# Print all students ordered by name
for username in sorted(contest_by_user.keys()):
    print(username)
    for contest, points in sorted(contest_by_user[username].items(), key=lambda x: (-x[1], x[0])):
        print(f"#  {contest} -> {points}")
