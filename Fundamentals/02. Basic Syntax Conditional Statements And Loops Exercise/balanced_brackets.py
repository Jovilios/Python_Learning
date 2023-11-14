n = int(input())
bracket_stack = []

for i in range(n):
    symbol = input()
    if symbol == "(":
        bracket_stack.append(symbol)
    elif symbol == ")":
        if not bracket_stack:
            print("UNBALANCED")
            break
        bracket_stack.pop()
else:
    if not bracket_stack:
        print("BALANCED")
    else:
        print("UNBALANCED")
