from collections import deque

BOX_SIZE = 50
filled_boxes = 0

eggs_size = deque(int(x) for x in input().split(", "))
paper_size = deque(int(x) for x in input().split(", "))

while eggs_size and paper_size:

    if eggs_size[0] <= 0:
        eggs_size.popleft()
        continue

    elif eggs_size[0] == 13:
        eggs_size.popleft()
        paper_size[0], paper_size[-1] = paper_size[-1], paper_size[0]
        continue

    egg = eggs_size.popleft()
    paper = paper_size.pop()

    if egg + paper <= BOX_SIZE:
        filled_boxes += 1
    else:
        continue

if filled_boxes <= 0:
    print("Sorry! You couldn't fill any boxes!")
else:
    print(f"Great! You filled {filled_boxes} boxes.")
if eggs_size:
    print(f"Eggs left: {', '.join(str(x) for x in eggs_size)}")
if paper_size:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper_size)}")