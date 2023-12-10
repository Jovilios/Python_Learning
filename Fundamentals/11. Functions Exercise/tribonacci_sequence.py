def tri_seq(num):
    if num == 1:
        print("1")
    elif int(num) == 2:
        print("1 1")
    elif int(num) == 3:
        print("1 1 2")
    else:
        idx = [0] * num
        idx[0] = 1
        idx[1] = 1
        idx[2] = 2
        for i in range(3, num):
            idx[i] = idx[i - 1] + idx[i - 2] + idx[i - 3]
        print(*idx)


numb = int(input())
tri_seq(numb)
