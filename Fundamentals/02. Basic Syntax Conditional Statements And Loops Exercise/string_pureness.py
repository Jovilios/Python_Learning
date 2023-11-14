count = int(input())

for _ in range(count):
    word = input()

    flag = True
    for ch in word:
        if ch == "_" or ch == "," or ch == ".":
            flag = False
            break

    if flag:
        print(f"{word} is pure.")
    else:
        print(f"{word} is not pure!")
