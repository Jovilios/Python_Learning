from collections import deque

stack = deque()

for _ in range(int(input())):
    commands = input().split()

    if commands[0] == "1":
        numb = int(commands[1])
        stack.append(numb)
    elif commands[0] == "2":
        if stack:
            stack.pop()
    elif commands[0] == "3":
        if stack:
            print(max(stack))
    elif commands[0] == "4":
        if stack:
            print(min(stack))

stack.reverse()

print(*stack, sep=", ")

# map_functions = {
#     1: lambda x: stack.append(x[1]),
#     2: lambda x: stack.pop() if stack else None,
#     3: lambda x: print(max(stack)) if stack else None,
#     4: lambda x: print(min(stack)) if stack else None
# }
#
#
# for _ in range(len(input())):
#     number_data = [int(x) for x in input().split()]
#     map_functions[number_data[0]](number_data)
#
#
# stack.reverse()
#
# print(*stack, sep=", ")