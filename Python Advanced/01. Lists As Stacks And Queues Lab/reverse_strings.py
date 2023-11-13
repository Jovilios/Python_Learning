line = list(input())

stack = []

for el in range(len(line)):
    stack.append(line.pop())

print(''.join(stack))
