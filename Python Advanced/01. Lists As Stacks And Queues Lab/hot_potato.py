from collections import deque

kids = deque(input().split())
rotation = int(input()) - 1

while len(kids) > 1:
    kids.rotate(-rotation)
    removed_kid = kids.popleft()
    print(f"Removed {removed_kid}")

print(f"Last is {kids.popleft()}")
