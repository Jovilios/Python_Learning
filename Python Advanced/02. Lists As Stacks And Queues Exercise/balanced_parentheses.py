from collections import deque

parentheses = deque(input())

open_ = deque()

while parentheses:

    current_parent = parentheses.popleft()

    if current_parent in "({[":
        open_.append(current_parent)

    elif not open_:
        print("NO")
        break

    else:
        if f"{open_.pop() + current_parent}" not in "(){}[]":
            print("NO")
            break

else:
    print("YES")